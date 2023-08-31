import pandas as pd

def load_data_drugs():
    """
    Charge les données des médicaments depuis les fichiers CSV
    """
    drugs_df = pd.read_csv("../data/raw/drugs.csv")
    return drugs_df