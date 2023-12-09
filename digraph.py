class Digraph:
    def __init__(self, size):
        self.size = size
        self.adj = [[] for _ in range(size)]

    def add_edge(self, i, j):
        self.adj[i - 1].append(j)

    def remove_edge(self, i, j):
        print("remove {} {}".format(i, j))
        self.adj[i - 1].remove(j)


# Kahn’s algorithm
def topsort(graph):
    T = []
    pred_count = [0] * graph.size
    for n in range(graph.size):
        for m in graph.adj[n]:
            pred_count[m - 1] += 1
    S = [m for m in range(1, graph.size + 1) if not pred_count[m - 1]]

    while S:
        n = S.pop()
        T.append(n)
        while graph.adj[n - 1]:
            m = graph.adj[n - 1][0]
            graph.remove_edge(n, m)
            pred_count[m - 1] -= 1
            if not pred_count[m - 1]:
                S.append(m)

    for n in range(graph.size):
        if graph.adj[n]:
            print(graph.adj[n])
            raise Exception("Not a DAG")

    return T


graph = Digraph(10)
graph.add_edge(1, 4)
graph.add_edge(2, 3)
graph.add_edge(3, 8)
graph.add_edge(4, 10)
graph.add_edge(5, 6)
graph.add_edge(7, 5)
graph.add_edge(9, 3)
graph.add_edge(9, 7)
graph.add_edge(10, 7)
print(topsort(graph))
