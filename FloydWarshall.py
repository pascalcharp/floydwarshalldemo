from Graphe import Graphe

class MoteurFloydWarshall:
    """Classe servant à appliquer l'algorithme de Floyd-Warshall sur un graphe"""

    def __init__(self, graphe):
        """L'objet doit d'abord être construit en lui passant le graphe à analyser."""
        self.graphe = graphe
        self.cardinal = graphe.getCardinal()

        self.valuation = [[] for _ in range(self.cardinal)]
        self.predecesseurs = [[] for _ in range(self.cardinal)]

        self.construireMatriceValuation()
        self.construireMatricePredecesseurs()

        self.printReport("Initial", [])

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

    def printMatrice(self, matrice, updated):
        for i in range(self.cardinal):
            for j in range(self.cardinal):
                if (i, j) in updated:
                    prefix = "\033[92m"
                else:
                    prefix = ""
                if matrice[i][j] is None:
                    print("-      ", end="")
                else:
                    print(f"{prefix}{matrice[i][j]:<-7}\033[0m", end="")
            print("")

    def printReport(self, k, updated):
        print(f"Floyd-Warshall, sommet intermédiaire = {k}")
        print(f"Matrice de valuation: ")
        self.printMatrice(self.valuation, updated)
        print(f"Matrice des prédécesseurs:")
        self.printMatrice(self.predecesseurs, updated)
        print("\n\n\n")

    def floydWarshall(self):
        """Une fois construit, permet d'exécuter l'algorithme, en affichant à chaque itération l'état
        des matrices de valuation et des prédécesseurs."""
        for k in range(self.cardinal):
            updated = []
            for i in range(self.cardinal):
                for j in range(self.cardinal):
                    temp = self.valuation[i][k] + self.valuation[k][j]
                    if temp < self.valuation[i][j]:
                        updated.append((i, j))
                        self.valuation[i][j] = temp
                        self.predecesseurs[i][j] = k
            self.printReport(k, updated)

if __name__ == "__main__":

    # Exemple d'exécution tiré des notes de cours

    # Étape 1: construire un graphe
    monGraphe = Graphe(4)
    monGraphe.ajouterArete(0, 1, 1.0)
    monGraphe.ajouterArete(0, 3, 8.0)
    monGraphe.ajouterArete(1, 2, 4.0)
    monGraphe.ajouterArete(2, 1, 7.0)
    monGraphe.ajouterArete(2, 3, 9.0)
    monGraphe.ajouterArete(3, 1, 2.0)
    monGraphe.ajouterArete(3, 0, 0.0)


    # Étape 2: construire le moteur Floyd-Warshall avec le graphe
    solver = MoteurFloydWarshall(monGraphe)

    # Étape 3: exécuter l'algorithme
    solver.floydWarshall()

