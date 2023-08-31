if __name__ == "__main__":
    # Import des fonctions depuis différents modules
    from pipeline.load_data.load_drugs import load_data_drugs
    from pipeline.load_data.load_clinical_trials import load_data_trials
    from pipeline.load_data.load_pubmed import load_pubmed_json, load_pubmed_csv, load_merge
    from pipeline.transform_data.transform_clinical_trials import drop_titles_with_anomalie, correct_id_na, correct_journal_na, cast_date
    from pipeline.transform_data.transform_pubmed import correct_pubmed_id
    from pipeline.create_graph.create_json_output import create_drug_graph
    
    # Chargement des données de médicaments
    drugs = load_data_drugs()
    
    # Chargement des données des essais cliniques
    trials = load_data_trials()
    
    # Chargement des données PubMed à partir d'un fichier CSV
    pubmed_csv = load_pubmed_csv()
    
    # Chargement des données PubMed à partir d'un fichier JSON
    pubmed_json = load_pubmed_json()
    
    # Fusion des données PubMed CSV et JSON
    pubmed = load_merge(pubmed_csv, pubmed_json)
    
    # Nettoyage et transformation des données des essais cliniques
    trials = drop_titles_with_anomalie(trials)
    trials = correct_id_na(trials)
    trials = correct_journal_na(trials)
    trials = cast_date(trials)
    
    # Nettoyage et transformation des données PubMed
    pubmed = correct_pubmed_id(pubmed)
    pubmed = cast_date(pubmed)
    
    # Création du graphe de liaison et sauvegarde dans un fichier JSON
    create_drug_graph(drugs, pubmed, trials)
