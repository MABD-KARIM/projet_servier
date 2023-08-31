import json
from collections import Counter

def get_top_journal():
    """
    Cette fonction lit un fichier JSON contenant des données sur les médicaments et leurs mentions
    dans différents journaux. Elle retourne le nom du journal qui mentionne le plus de médicaments différents.
    """
    
    # Initialisation d'une liste pour stocker les occurrences de chaque journal.
    journal_recurrence = list()

    # Ouvrir et lire le fichier JSON pour charger les données.
    with open("../data/output/graph.json", 'r') as f:
        data = json.load(f)

    # Parcourir chaque entrée de médicament dans les données.
    for entry in data:
        
        # Utiliser un set pour éviter les doublons de noms de journaux pour un médicament donné.
        journals = set()
        
        # Parcourir chaque mention de journal pour le médicament en cours.
        for journal in entry["journal_mentions"]:
            journals.add(journal["journal_id"])
        
        # Étendre la liste des occurrences de journaux avec les noms de journaux uniques pour ce médicament.
        journal_recurrence.extend(journals)

    # Compter les occurrences de chaque journal dans la liste.
    counting = Counter(journal_recurrence)
    
    # Trouver et retourner le journal le plus fréquemment mentionné.
    result = counting.most_common(1)[0][0]
    return result

if __name__ == "__main__":
    # Exécuter la fonction et afficher le résultat.
    print(get_top_journal())
