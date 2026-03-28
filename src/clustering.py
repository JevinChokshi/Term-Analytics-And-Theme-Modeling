import numpy as np
from sklearn.cluster import AgglomerativeClustering
from sklearn.metrics.pairwise import cosine_similarity

def hybrid_clustering(terms, gene_sets, embeddings):
    n = len(terms)

    g_sim = np.zeros((n, n))

    for i in range(n):
        for j in range(n):
            union = len(gene_sets[i] | gene_sets[j])
            g_sim[i, j] = len(gene_sets[i] & gene_sets[j]) / union if union else 0

    s_sim = cosine_similarity(embeddings)

    hybrid_sim = 0.6 * g_sim + 0.4 * s_sim

    clusters = AgglomerativeClustering(
        metric="precomputed",
        linkage="average",
        distance_threshold=0.5,
        n_clusters=None
    ).fit_predict(1 - hybrid_sim)

    return clusters, hybrid_sim