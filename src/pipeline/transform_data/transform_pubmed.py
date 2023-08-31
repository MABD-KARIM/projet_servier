import pandas as pd
import numpy as np

def correct_pubmed_id(df):
    """
    Convertit la colonne 'id' en entiers et remplace les valeurs manquantes par max(id) + 1.
    
    Paramètres :
    df (DataFrame) : DataFrame original contenant les données de PubMed.
    
    Retour :
    DataFrame : Nouveau DataFrame avec la colonne 'id' corrigée.
    """
    
    # Convertit la colonne 'id' en numérique où c'est possible, sinon met NaN
    df['id'] = pd.to_numeric(df['id'], errors='coerce')
    
    # Trouve la valeur maximale dans la colonne 'id'
    max_id = df['id'].max()
    
    # Remplace les valeurs NaN ou manquantes dans 'id' par max_id + 1
    missing_ids = df['id'].isna()
    if max_id is np.nan:
        max_id = 0  # Si tous les IDs sont manquants, commence avec 1
    df.loc[missing_ids, 'id'] = [max_id + 1 + i for i in range(sum(missing_ids))]
    
    # Convertit toute la colonne en entiers
    df['id'] = df['id'].astype(int)
    
    return df


