import pytest
import pandas as pd
from pipeline.load_data.load_drugs import load_data_drugs
from pipeline.load_data.load_clinical_trials import load_data_trials
from pipeline.load_data.load_pubmed import load_pubmed_json, load_pubmed_csv, load_merge
from pipeline.transform_data.transform_clinical_trials import drop_titles_with_anomalie, correct_id_na, correct_journal_na, cast_date
from pipeline.transform_data.transform_pubmed import correct_pubmed_id
from pipeline.create_graph.create_json_output import create_drug_graph

# Teste si le chargement des données médicamenteuses fonctionne correctement
def test_load_data_drugs():
    drugs_df = load_data_drugs() 
    assert not drugs_df.empty
    print("test_load_data_drugs: OK")

# Teste si le chargement des données des essais cliniques fonctionne correctement
def test_load_data_trials():
    trials_df = load_data_trials()
    assert not trials_df.empty
    print("test_load_data_trials: OK")

# Teste si les titres contenant des anomalies sont correctement supprimés
def test_drop_titles_with_anomalie():
    trials_df = pd.DataFrame({
        'id': ['NCT001', 'NCT002', 'NCT003'],
        'title': ['Valid Title', 'Anomalie Title', 'Another Valid Title'],
        'date': ['01/01/2020', '01/01/2020', '02/01/2020'],
        'journal': ['Journal A', 'Journal A', 'Journal B']
    })
    filtered_df = drop_titles_with_anomalie(trials_df)
    assert 'Anomalie Title' not in filtered_df['title'].values
    print("test_drop_titles_with_anomalie: OK")

# Teste si les valeurs manquantes dans la colonne 'id' sont correctement traitées
def test_correct_id_na():
    trials_df = pd.DataFrame({
        'id': ['NCT001', None, 'NCT003'],
        'title': ['Valid Title', 'Another Title', 'Another Valid Title'],
        'date': ['01/01/2020', '01/01/2020', '02/01/2020'],
        'journal': ['Journal A', 'Journal A', 'Journal B']
    })
    corrected_df = correct_id_na(trials_df)
    assert corrected_df['id'].isna().sum() == 0
    print("test_correct_id_na: OK")

# Teste si la colonne 'date' est correctement convertie au format datetime
def test_cast_date():
    pubmed_df = pd.DataFrame({
        'id': [1, 2],
        'title': ['Title A', 'Title B'],
        'date': ['01/01/2020', '02/01/2020'],
        'journal': ['Journal A', 'Journal B']
    })
    casted_df = cast_date(pubmed_df)
    assert pd.api.types.is_datetime64_any_dtype(casted_df['date'])
    print("test_cast_date: OK")

# Fonction principale pour exécuter tous les tests
def main():
    pytest.main()

# Point d'entrée du script de test
if __name__ == '__main__':
    main()

