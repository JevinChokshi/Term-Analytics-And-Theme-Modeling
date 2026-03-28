import warnings
warnings.filterwarnings("ignore")

import matplotlib.pyplot as plt
import seaborn as sns

from src.config import *
from src.models import load_embedding_model, initialize_topic_model
from src.validator import MyGeneValidator
from src.pipeline import run_pipeline

import os
os.environ["TF_ENABLE_ONEDNN_OPTS"] = "0"

def main():

    model, theme_embs = load_embedding_model()
    topic_model = initialize_topic_model(ORA_FOLDER)
    validator = MyGeneValidator()

    df_res = run_pipeline(model, theme_embs, topic_model, validator)

    df_res.to_csv(f"{OUTPUT_FOLDER}/fraction_themes.csv", index=False)

    # Plot
    plt.figure(figsize=(10, 6))
    sns.set_context("paper")

    df_plot = df_res.set_index("submodule")[VALID_DISEASES]
    df_plot.plot(kind="bar", stacked=True)

    plt.title("Disease Signature Distribution Across Submodules")
    plt.ylim(0, 1)

    sns.despine()
    plt.tight_layout()

    plt.savefig(f"{OUTPUT_FOLDER}/submodule_fractions.png", dpi=300)

    print("Pipeline completed successfully.")

if __name__ == "__main__":
    main()