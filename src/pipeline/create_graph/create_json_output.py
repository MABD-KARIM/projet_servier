import pandas as pd
import json

def create_drug_graph(drugs_df, pubmed_df, clinical_trials_df):
    """
    Crée un graphe de liaison entre les différents médicaments, les publications PubMed,
    les essais cliniques et les journaux associés.

    Paramètres :
    - drugs_df (DataFrame) : DataFrame contenant les codes et noms des médicaments.
    - pubmed_df (DataFrame) : DataFrame contenant les informations des publications PubMed.
    - clinical_trials_df (DataFrame) : DataFrame contenant les informations des essais cliniques.

    Sortie :
    Un fichier JSON est sauvegardé, qui contient les informations de liaison.
    """

    # Structure de données pour contenir le graphe
    graph = []

    # Remplir la liste des médicaments et créer les liens
    for _, drug_row in drugs_df.iterrows():
        # Initialiser le dictionnaire pour chaque médicament
        drug = {
            "atccode": drug_row["atccode"],
            "name": drug_row["drug"],
            "pubmed_mentions": [],
            "clinical_trial_mentions": [],
            "journal_mentions": []  # Maintenant une liste de dictionnaires
        }
        
        # Recherche des mentions dans PubMed
        for _, pubmed_row in pubmed_df.iterrows():
            if drug_row["drug"].lower() in pubmed_row["title"].lower():
                # Ajouter la mention PubMed
                pubmed_mention = {
                    "pubmed_id": pubmed_row["id"],
                    "date": pubmed_row["date"]
                }
                drug["pubmed_mentions"].append(pubmed_mention)
                
                # Ajouter la mention du journal
                journal_mention = {"journal_id": pubmed_row["journal"], "date": pubmed_row["date"]}
                drug["journal_mentions"].append(journal_mention)
                
        # Recherche des mentions dans les essais cliniques
        for _, trial_row in clinical_trials_df.iterrows():
            if drug_row["drug"].lower() in trial_row["scientific_title"].lower():
                # Ajouter la mention d'essai clinique
                clinical_trial_mention = {
                    "clinical_trial_id": trial_row["id"],
                    "date": trial_row["date"]
                }
                drug["clinical_trial_mentions"].append(clinical_trial_mention)
                
                # Ajouter la mention du journal
                journal_mention = {"journal_id": trial_row["journal"], "date": trial_row["date"]}
                drug["journal_mentions"].append(journal_mention)
                    
        # Ajouter le médicament au graphe
        graph.append(drug)

    # Convertir en JSON et sauvegarder
    with open("../data/output/graph.json", "w") as f:
        json.dump(graph, f, indent=4)

    print("Graphe sauvegardé dans graph.json")
