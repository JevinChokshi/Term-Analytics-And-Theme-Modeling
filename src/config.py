import os

# Paths
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
DATA_FOLDER = os.path.join(BASE_DIR, "data")
ORA_FOLDER = os.path.join(DATA_FOLDER, "ORA_files")
OUTPUT_FOLDER = os.path.join(BASE_DIR, "outputs")

SUB_MEMBERSHIP_FILE = os.path.join(DATA_FOLDER, "submodule_membership.csv")

os.makedirs(OUTPUT_FOLDER, exist_ok=True)

# Parameters
PVALUE_CUTOFF = 0.05
VALID_DISEASES = ["cancer", "diabetes", "immune", "neuro", "aging"]

# Visualization
NATURE_PALETTE = ["#E64B35FF", "#4DBBD5FF", "#00A087FF", "#3C5488FF", "#F39B7FFF"]

# Theme anchors
THEME_LABELS = [
    "cell cycle, mitotic proliferation and DNA replication",
    "DNA repair, chromatin remodeling and genomic integrity",
    "immune activation, interferon response and leukocyte signaling",
    "cytokine signaling, inflammatory response and chemotaxis",
    "metabolic homeostasis, glucose and lipid regulation",
    "mitochondrial energetics, oxphos and redox balance",
    "protein proteostasis, autophagy and ubiquitin system",
    "apoptotic signaling and programmed cell death",
    "synaptic signaling, neurotransmitters and neuronal development",
    "axon guidance, glial function and neuroinflammation",
    "cellular senescence, telomere stress and aging"
]

# Disease keywords
DISEASE_SIGNATURES = {
    "cancer": ["neoplasm", "carcinoma", "tumor", "cancer", "oncogene", "cell cycle"],
    "immune": ["autoimmune", "inflammation", "infection", "immune", "interferon", "virus"],
    "diabetes": ["diabetes", "metabolic", "insulin", "lipid", "glucose", "cardiovascular"],
    "neuro": ["alzheimer", "parkinson", "neuro", "brain", "synaptic", "axon"],
    "aging": ["longevity", "senescence", "proteostasis", "telomere", "autophagy", "aging"]
}