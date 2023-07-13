# Cours IFT-2008: démo pour l'algorithme de Floyd-Warshall
## Contenu et instructions
- Graphe.py: une classe graphe utilisant des listes d'adjacences.  Très minimaliste, aucune validation n'est faite.  
Chaque sommet est codé par un entier non-signé allant de 0 à N-1 où N est le nombre de sommets.  On construit un graphe 
en passant au constructeur le nombre requis de sommets.  Il faut ensuite utiliser la méthode ajouterArete pour construire
manuellement le graphe.

- FloydWarshall.py: une classe servant à implanter l'algorithme de Floyd-Warshall sur la classe Graphe. 
  - Il faut d'abord construire un objet de la classe Graphe en lui passant le nombre requis de sommets, puis ensuite
  ajouter manuellement les arêtes requises avec la méthode ajouterArete.
  - Il faut ensuite initialiser un objet de la classe MoteurFloydwarshall en lui passant le graphe en paramètre. 
  - Ensuite il faut appeler la méthode floydWarshall sur cet objet afin de faire rouler l'algorithme. La matrice de valuation
  ainsi que la matrice des prédécesseurs sera affichée pour chaque itération, avec les éléments nouvellement mis à jour
  affichés en vert.
