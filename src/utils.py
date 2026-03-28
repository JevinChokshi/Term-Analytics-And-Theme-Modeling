import os
from collections import defaultdict

def map_submodule_files(folder):
    sub_files = defaultdict(list)

    for f in os.listdir(folder):
        if f.startswith("submodule_") and (
            f.endswith("GO_BP.csv") or f.endswith("REACTOME.csv")
        ):
            parts = f.split("_")
            sub_id = "_".join(parts[:2])
            sub_files[sub_id].append(f)

    return sub_files