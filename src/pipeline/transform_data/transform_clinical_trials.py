import pandas as pd
from random import randint
import numpy as np

def drop_titles_with_anomalie(df):
    """
    Supprime les lignes où le champ 'scientific_title' est vide ou composé uniquement d'espaces.
    
    Paramètres :
    df (DataFrame) : DataFrame original contenant les données sur les essais cliniques.
    
    Retour :
    DataFrame : Nouveau DataFrame sans les lignes avec des titres scientifiques manquants ou vides.
    """
    result = df[df.scientific_title.str.strip() != ""]
    return result

def correct_id_na(df):
    """
    Remplace les valeurs manquantes dans la colonne 'id' par un identifiant unique généré aléatoirement.
    
    Paramètres :
    df (DataFrame) : DataFrame original contenant les données sur les essais cliniques.
    
    Retour :
    DataFrame : Nouveau DataFrame avec les valeurs manquantes dans la colonne 'id' remplacées.
    """
    existing_ids = set(df['id'].dropna())
    
    def generate_unique_id(ids):
        """
        Génère un nouvel identifiant unique qui n'existe pas dans l'ensemble existing_ids.
        
        Paramètres :
        ids (set) : Ensemble des identifiants existants.
        
        Retour :
        str : Nouvel identifiant unique.
        """
        while True:
            id = 'NCT' + str(randint(10000000, 99999999))
            if id not in ids:
                existing_ids.add(id)
                return id
                
    missing_ids = df['id'].isna()
    df.loc[missing_ids, 'id'] = [generate_unique_id(existing_ids) for _ in range(sum(missing_ids))]
    return df

def cast_date(df):
    """
    Transforme les valeurs dans la colonne 'date' au format standard YYYY-MM-DD.
    
    Paramètres :
    df (DataFrame) : DataFrame original contenant les données sur les essais cliniques.
    
    Retour :
    DataFrame : Nouveau DataFrame avec les dates transformées.
    """
    def transform(date_str):
        """
        Tente de transformer la chaîne de date en un objet datetime, sinon retourne NaN.
        
        Paramètres :
        date_str (str) : Chaîne de caractères contenant la date à transformer.
        
        Retour :
        str ou np.nan : Date transformée au format 'YYYY-MM-DD' ou np.nan si la transformation échoue.
        """
        try:
            return pd.to_datetime(date_str).strftime('%Y-%m-%d')
        except Exception:
            return np.nan
    
    df["date"] = df["date"].apply(transform)
    return df

def correct_journal_na(df):
    """
    Remplace les valeurs manquantes dans la colonne 'journal' par la chaîne "Missing Journal".
    
    Paramètres :
    df (DataFrame) : DataFrame original contenant les données sur les essais cliniques.
    
    Retour :
    DataFrame : Nouveau DataFrame avec les valeurs manquantes dans la colonne 'journal' remplacées.
    """
    missing_journals = df["journal"].isna()
    df.loc[missing_journals, "journal"] = "Missing Journal"
    return df
