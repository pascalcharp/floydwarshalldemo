from Graphe import Graphe

class MoteurFloydWarshall:
    def __init__(self, graphe):
        self.graphe = graphe
        self.cardinal = graphe.getCardinal()

        self.valuation = [[] for _ in range(self.cardinal)]
        self.predecesseurs = [[] for _ in range(self.cardinal)]

        self.construireMatriceValuation()
        self.construireMatricePredecesseurs()

        self.printReport("Initial")

    def construireMatriceValuation(self):
        for i in range(self.cardinal):
            for j in range(self.cardinal):
                if i == j:
                    self.valuation[i].append(0)
                elif self.graphe.getDistance(i, j) is not None:
                    self.valuation[i].append(self.graphe.getDistance(i, j))
                else:
                    self.valuation[i].append(float('inf'))

    def construireMatricePredecesseurs(self):
        for i in range(self.cardinal):
            for j in range(self.cardinal):
                if self.graphe.getDistance(i, j) is not None:
                    self.predecesseurs[i].append(i)
                else:
                    self.predecesseurs[i].append(None)

    def printMatrice(self, matrice):
        for i in range(self.cardinal):
            for j in range(self.cardinal):
                if matrice[i][j] is None:
                    print("-      ", end="")
                else:
                    print(f"{matrice[i][j]:<-7}", end="")
            print("")

    def printReport(self, k):
        print(f"Floyd-Warshall, sommet intermédiaire = {k}")
        print(f"Matrice de valuation: ")
        self.printMatrice(self.valuation)
        print(f"Matrice des prédécesseurs:")
        self.printMatrice(self.predecesseurs)
        print("\n\n\n")

    def floydWarshall(self):
        for k in range(self.cardinal):
            for i in range(self.cardinal):
                for j in range(self.cardinal):
                    temp = self.valuation[i][k] + self.valuation[k][j]
                    if temp < self.valuation[i][j]:
                        self.valuation[i][j] = temp
                        self.predecesseurs[i][j] = k
            self.printReport(k)

if __name__ == "__main__":
    monGraphe = Graphe(4)
    monGraphe.ajouterArete(0, 1, 1.0)
    monGraphe.ajouterArete(0, 3, 8.0)
    monGraphe.ajouterArete(1, 2, 4.0)
    monGraphe.ajouterArete(2, 1, 7.0)
    monGraphe.ajouterArete(2, 3, 9.0)
    monGraphe.ajouterArete(3, 1, 2.0)
    monGraphe.ajouterArete(3, 0, 0.0)


    solver = MoteurFloydWarshall(monGraphe)
    solver.floydWarshall()

