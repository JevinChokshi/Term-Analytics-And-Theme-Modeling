import requests
from .config import VALID_DISEASES, DISEASE_SIGNATURES

class MyGeneValidator:
    def __init__(self):
        self.cache = {}

    def get_validation_distribution(self, gene_ids):
        ids_str = [str(g) for g in gene_ids if g]
        to_query = [g for g in ids_str if g not in self.cache]

        for i in range(0, len(to_query), 500):
            batch = to_query[i:i+500]
            try:
                resp = requests.post(
                    "https://mygene.info/v3/gene",
                    data={'ids': ','.join(batch), 'fields': 'disgenet,pharos'}
                ).json()

                for item in resp:
                    meta = ""
                    if 'disgenet' in item:
                        meta += str(item['disgenet'])
                    if 'pharos' in item:
                        meta += str(item['pharos'])

                    self.cache[item['query']] = meta.lower()
            except:
                continue

        scores = {d: 0.0 for d in VALID_DISEASES}

        for g in ids_str:
            meta = self.cache.get(g, "")
            for d, kws in DISEASE_SIGNATURES.items():
                if any(k in meta for k in kws):
                    scores[d] += 1

        total = sum(scores.values())
        return {d: (v / total if total > 0 else 0.2) for d, v in scores.items()}