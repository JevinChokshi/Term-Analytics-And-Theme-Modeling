import os
import pandas as pd
from sentence_transformers import SentenceTransformer
from bertopic import BERTopic
from .config import THEME_LABELS

def load_embedding_model():
    print("Loading BioBERT...")
    model = SentenceTransformer(
        "pritamdeka/BioBERT-mnli-snli-scinli-scitail-mednli-stsb"
    )
    theme_embs = model.encode(THEME_LABELS)
    return model, theme_embs


def initialize_topic_model(folder):
    all_terms = []

    for f in os.listdir(folder):
        if f.endswith(".csv") and "submodule_" in f:
            try:
                df = pd.read_csv(os.path.join(folder, f))
                all_terms.extend(df["Term_Name"].tolist())
            except:
                continue

    topic_model = BERTopic(verbose=False)
    topic_model.fit(all_terms)

    return topic_model