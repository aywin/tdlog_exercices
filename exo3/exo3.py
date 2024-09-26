def processLines(lines) -> str:
    # Lecture des données d'entrée
    N = int(lines[0])  # Nombre de sprints
    backlog = int(lines[1])  # Nombre de tâches initiales dans le backlog
    
    # Boucle sur les sprints pour mettre à jour le backlog
    for i in range(2, N + 2):
        V, U = map(int, lines[i].split())  # V = tâches validées, U = modifications du backlog
        backlog -= V  # Soustraire les tâches validées du backlog
        backlog += U  # Ajouter ou soustraire les modifications du backlog
    
    # Vérifier si le backlog est vide
    if backlog == 0:
        return "OK"
    else:
        return "KO"

# Exemple d'utilisation
lines = [
    "3",  # Nombre de sprints
    "5",  # Nombre de tâches initiales
    "2 1",  # 2 tâches validées, 1 tâche ajoutée
    "1 -2",  # 1 tâche validée, 2 tâches supprimées
    "2 0"  # 2 tâches validées, 0 ajout ou suppression
]
print(processLines(lines))  # Sortie attendue : OK
