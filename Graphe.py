class Graphe:
    def __init__(self, n):

        self.adjacents = [[] for _ in range(n)]
        self.cardinal = n

    def getDistance(self, source, destination):
        for (dest, dist) in self.adjacents[source]:
            if dest == destination:
                return dist
        return None

    def ajouterArete(self, source, destination, distance):
        self.adjacents[source].append((destination, distance))

    def getCardinal(self):
        return self.cardinal

    def getAdjacentsPourSommet(self, source):
        return self.adjacents[source]

if __name__ == "__main__":
    monGraphe = Graphe(4)
    monGraphe.ajouterArete(0, 1, 1.0)
    monGraphe.ajouterArete(0, 2, 1.5)
    pass