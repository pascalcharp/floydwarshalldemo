class Graphe:
    """Classe servant à modéliser un graphe en utilisant des listes d'adjacences.  Chaque sommet
    est codé par un nombre entier positif consécutif partant de 0."""

    def __init__(self, n):
        """Constructeur: prend un seul paramètre, soit le nombre de sommets du graphe."""

        self.adjacents = [[] for _ in range(n)]
        self.cardinal = n

    def getDistance(self, source, destination):
        """Retournera la distance de l'arête entre source et destination.  Comportement non défini
        si source ou destination sont non-valides, ou si l'arête demandée n'existe pas."""
        for (dest, dist) in self.adjacents[source]:
            if dest == destination:
                return dist
        return None

    def ajouterArete(self, source, destination, distance):
        """Ajoute une arête entre source et destination ayant une distance donnée.  Si une arête existe
        déjà, ou si source ou destination sont non valides, le comportement sera non défini."""
        self.adjacents[source].append((destination, distance))

    def getCardinal(self):
        """Retourne le nombre de sommets"""
        return self.cardinal

    def getAdjacentsPourSommet(self, source):
        """Retourne une liste de tuples (destination, distance) à partir de source."""
        return self.adjacents[source]

if __name__ == "__main__":
    monGraphe = Graphe(4)
    monGraphe.ajouterArete(0, 1, 1.0)
    monGraphe.ajouterArete(0, 2, 1.5)
    pass