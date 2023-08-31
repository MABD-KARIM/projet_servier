import pandas as pd

def load_data_trials():
    """
    Charge les données des essais cliniques depuis les fichiers CSV
    """
    trials_df = pd.read_csv("../data/raw/clinical_trials.csv")
    return trials_df