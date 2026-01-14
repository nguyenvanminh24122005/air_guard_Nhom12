import os
from pathlib import Path
import papermill as pm

PROJECT_ROOT = Path(__file__).resolve().parent
os.makedirs(PROJECT_ROOT / "notebooks/runs", exist_ok=True)

KERNEL = "beijing_env"

# 1) Preprocessing + EDA
pm.execute_notebook(
    str(PROJECT_ROOT / "notebooks/preprocessing_and_eda.ipynb"),
    str(PROJECT_ROOT / "notebooks/runs/preprocessing_and_eda_run.ipynb"),
    parameters=dict(
        USE_UCIMLREPO=False,
        RAW_ZIP_PATH=str(PROJECT_ROOT / "data/raw/PRSA2017_Data_20130301-20170228.zip"),
        OUTPUT_CLEANED_PATH=str(PROJECT_ROOT / "data/processed/cleaned.parquet"),
        LAG_HOURS=[1, 3, 24],
    ),
    kernel_name=KERNEL,
)

# 2) Semi-supervised dataset preparation
pm.execute_notebook(
    str(PROJECT_ROOT / "notebooks/semi_dataset_preparation.ipynb"),
    str(PROJECT_ROOT / "notebooks/runs/semi_dataset_preparation_run.ipynb"),
    parameters=dict(
        CLEANED_PATH=str(PROJECT_ROOT / "data/processed/cleaned.parquet"),
        OUTPUT_SEMI_DATASET_PATH=str(PROJECT_ROOT / "data/processed/dataset_for_semi.parquet"),
        CUTOFF="2017-01-01",
        LABEL_MISSING_FRACTION=0.95,
        RANDOM_STATE=42,
    ),
    kernel_name=KERNEL,
)
