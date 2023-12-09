class Digraph:
    """
    A directed acyclic graph (DAG) represented as an adjacency list.
    """

    def __init__(self, size: int):
        """
        Initializes a new Digraph with the specified size.

        Args:
            size: The number of vertices in the graph.
        """
        self.size = size
        self.adj = [[] for _ in range(size)]

    def add_edge(self, i: int, j: int):
        """
        Adds a directed edge from vertex i to vertex j.

        Args:
            i: The source vertex.
            j: The destination vertex.
        """
        self.adj[i - 1].append(j)

    def remove_edge(self, i: int, j: int):
        """
        Removes a directed edge from vertex i to vertex j.

        Args:
            i: The source vertex.
            j: The destination vertex.
        """
        print(f"remove {i} {j}")
        self.adj[i - 1].remove(j)


# Kahn’s algorithm
def topsort(graph: Digraph) -> list:
    """
    Implements Kahn's algorithm to perform topological sorting on a DAG.

    Args:
        graph: The Digraph object.

    Returns:
        A list of vertices in topological order.
    """
    T = []  # List of topologically sorted vertices
    pred_count = [0] * graph.size  # Number of incoming edges for each vertex
    for n in range(graph.size):
        for m in graph.adj[n]:
            pred_count[
                m - 1
            ] += 1  # Increment the number of incoming edges for each neighbor

    S = [
        m for m in range(1, graph.size + 1) if not pred_count[m - 1]
    ]  # Initialize the queue with vertices with no incoming edges

    while S:
        n = S.pop()  # Remove a vertex from the queue
        T.append(n)  # Add the vertex to the topological order
        while graph.adj[n - 1]:  # Iterate through outgoing edges of the current vertex
            m = graph.adj[n - 1][0]  # Remove the first outgoing edge
            graph.remove_edge(n, m)  # Remove the edge from the graph
            pred_count[
                m - 1
            ] -= 1  # Decrement the number of incoming edges for the neighbor
            if not pred_count[
                m - 1
            ]:  # Add the neighbor to the queue if it has no incoming edges anymore
                S.append(m)

    for n in range(graph.size):  # Check if there are any cycles in the graph
        if graph.adj[n]:
            print(graph.adj[n])
            raise Exception("Not a DAG")  # Raise an exception if a cycle is detected

    return T


graph = Digraph(10)  # Create a Digraph object with 10 vertices
graph.add_edge(1, 4)  # Add edges to the graph
graph.add_edge(2, 3)
graph.add_edge(3, 8)
graph.add_edge(4, 10)
graph.add_edge(5, 6)
graph.add_edge(7, 5)
graph.add_edge(9, 3)
graph.add_edge(9, 7)
graph.add_edge(10, 7)

try:
    print(topsort(graph))  # Print the topological order
except Exception as e:
    print(f"Exception: {e}")  # Handle any exceptions
