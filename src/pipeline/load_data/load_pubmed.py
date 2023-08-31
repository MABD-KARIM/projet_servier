import pandas as pd
import json

def load_pubmed_json():
    """
    Charge les données des publications depuis un fichier JSON et les convertit en DataFrame.
    
    Paramètres:
        filepath (str): Chemin d'accès au fichier JSON.
        
    Retourne:
        DataFrame: DataFrame contenant les données chargées ou None en cas d'erreur.
    """
    
    try:
        with open("../data/raw/pubmed.json", 'r') as f:
            data_str = f.read().strip().strip("[").strip("]").strip()
            
            # Supprime la virgule à la fin si elle est présente
            if data_str.endswith(","):
                data_str = data_str[:-1]
                
            # Remet les crochets de début et de fin
            data_str = "[" + data_str + "]"
            
            # Charge la chaîne comme un objet JSON
            data = json.loads(data_str)
            
            return pd.DataFrame(data)
            
    except json.JSONDecodeError:
        print("Erreur dans le fichier JSON. Vérifiez le format du fichier.")
        return None
    except FileNotFoundError:
        print(f"Le fichier n'a pas été trouvé.")
        return None
    except Exception as e:
        print(f"Une erreur inattendue s'est produite : {e}")
        return None

def load_pubmed_csv():
    """
    Charge les données des publications depuis un fichier CSV.
    
    Paramètres:
        filepath (str): Chemin d'accès au fichier CSV.
        
    Retourne:
        DataFrame: DataFrame contenant les données chargées.
    """
    
    pubmed_csv = pd.read_csv("../data/raw/pubmed.csv")
    return pubmed_csv

def load_merge(df1, df2):
    """
    Fusionne deux DataFrames en un seul.
    
    Paramètres:
        df1 (DataFrame): Premier DataFrame à fusionner.
        df2 (DataFrame): Deuxième DataFrame à fusionner.
        
    Retourne:
        DataFrame: DataFrame résultant de la fusion des deux DataFrames.
    """
    
    result = pd.concat([df1, df2], ignore_index=True)
    return result
