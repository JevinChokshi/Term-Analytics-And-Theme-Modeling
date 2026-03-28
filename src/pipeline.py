import os
import numpy as np
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from .config import *
from .clustering import hybrid_clustering
from .utils import map_submodule_files

def run_pipeline(model, theme_embs, topic_model, validator):

    membership = pd.read_csv(SUB_MEMBERSHIP_FILE)
    sub_gene_map = membership.groupby("cluster")["gene"].apply(list).to_dict()

    sub_files = map_submodule_files(ORA_FOLDER)

    results = []

    for sub_id in sorted(sub_files.keys()):

        parts = sub_id.split("_")
        if len(parts) < 2 or not parts[1].isdigit():
            continue

        dfs = [pd.read_csv(os.path.join(ORA_FOLDER, f)) for f in sub_files[sub_id]]
        df = pd.concat(dfs).dropna(subset=["Term_Name"])
        df = df[df["Adjusted P-value"] < PVALUE_CUTOFF]

        if len(df) < 3:
            continue

        gene_sets = df["Genes"].apply(lambda x: set(str(x).split(";"))).tolist()
        terms = df["Term_Name"].tolist()

        embeddings = model.encode(terms, show_progress_bar=False)

        clusters, _ = hybrid_clustering(terms, gene_sets, embeddings)

        topics, _ = topic_model.transform(terms)

        sub_themes, sub_weights = [], []

        for cid in set(clusters):
            idx = np.where(clusters == cid)[0]

            weights = np.clip(-np.log10(df.iloc[idx]["Adjusted P-value"]), 0, 15)
            centroid = np.average(embeddings[idx], axis=0, weights=weights)

            theme_idx = cosine_similarity([centroid], theme_embs)[0].argmax()

            sub_themes.append(THEME_LABELS[theme_idx])
            sub_weights.append(weights.sum())

        # Inference
        inf_dist = {d: 0.0 for d in VALID_DISEASES}

        for t, w in zip(sub_themes, sub_weights):
            for d, kws in DISEASE_SIGNATURES.items():
                if any(k in t.lower() for k in kws):
                    inf_dist[d] += w

        total = sum(inf_dist.values())
        v_inference = {d: (v / total if total else 0.2) for d, v in inf_dist.items()}

        raw_id = int(parts[1])
        v_validation = validator.get_validation_distribution(sub_gene_map.get(raw_id, []))

        agreement = cosine_similarity(
            [list(v_inference.values())],
            [list(v_validation.values())]
        )[0][0]

        results.append({
            "submodule": sub_id,
            **v_inference,
            "agreement_score": agreement
        })

    return pd.DataFrame(results)