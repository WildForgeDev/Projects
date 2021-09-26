from collections import deque, namedtuple


# Set known costs of unknown vertices to infinity
inf = float('inf')
Edge = namedtuple('Edge', 'start, end, cost')

# define edge function to create edges of graph with costs.
def make_edge(start, end, cost=1):
  return Edge(start, end, cost)

# define graph class 
class Graph:
    def __init__(self, edges):
        self.edges = [make_edge(*edge) for edge in edges]

    @property
    #Create vertices method to sum the start and end edges of the graph.
    def vertices(self):
        return set(
            sum(
                ([edge.start, edge.end] for edge in self.edges), []
            )
        )
    #Create node pairs method to get the node pairs to remove from the Dijkstra algorithm once visited.
    def get_node_pairs(self, n1, n2, both_ends=True):
        if both_ends:
            node_pairs = [[n1, n2], [n2, n1]]
        else:
            node_pairs = [[n1, n2]]
        return node_pairs
# Define remove edge method in order to remove an edges from visited edges after nodes are selected.
    def remove_edge(self, n1, n2, both_ends=True):
        node_pairs = self.get_node_pairs(n1, n2, both_ends)
        edges = self.edges[:]
        for edge in edges:
            if [edge.start, edge.end] in node_pairs:
                self.edges.remove(edge)
# Define method to add edges to the edge list of visited nodes 
    def add_edge(self, n1, n2, cost=1, both_ends=True):
        node_pairs = self.get_node_pairs(n1, n2, both_ends)
        for edge in self.edges:
            if [edge.start, edge.end] in node_pairs:
                return ValueError('Edge {} {} already exists'.format(n1, n2))

        self.edges.append(Edge(start=n1, end=n2, cost=cost))
        if both_ends:
            self.edges.append(Edge(start=n2, end=n1, cost=cost))

    @property
    # Create the adjacent method to visit and find each adjacent node and their costs.
    def adjacent(self):
        adjacent = {vertex: set() for vertex in self.vertices}
        for edge in self.edges:
            adjacent[edge.start].add((edge.end, edge.cost))

        return adjacent
    # Create Dijkstra method to demonstrate the Dijkstra algorithm. Start with the root node and visit the less
    # less costly vertices first until all nodes are visited and return the shortest path from a to z.
    def dijkstra(self, source, dest):
        assert source in self.vertices, 'Such source node doesn\'t exist'
        distances = {vertex: inf for vertex in self.vertices}
        previous_vertices = {
            vertex: None for vertex in self.vertices
        }
        distances[source] = 0
        vertices = self.vertices.copy()

        while vertices:
            current_vertex = min(
                vertices, key=lambda vertex: distances[vertex])
            vertices.remove(current_vertex)
            if distances[current_vertex] == inf:
                break
            for neighbour, cost in self.adjacent[current_vertex]:
                new_route = distances[current_vertex] + cost
                if new_route < distances[neighbour]:
                    distances[neighbour] = new_route
                    previous_vertices[neighbour] = current_vertex

        path, current_vertex = deque(), dest
        while previous_vertices[current_vertex] is not None:
            path.appendleft(current_vertex)
            current_vertex = previous_vertices[current_vertex]
        if path:
            path.appendleft(current_vertex)
        return path

# create graph structure in order to perfrom the dijkstra method on the graph and find the shortes path between a and z.
graph = Graph([
    ('27','35', 88), ('35','27', 88), ('27','14', 13), ('14','27', 13),
    ('27','10', 1), ('10','27', 1), ('14','42', 98), ('42','14', 98),
    ('27','10', 1), ('10','27', 1), ('14','42', 98), ('42','14', 98),
    ('14','19', 41), ('19','14', 41), ('19','42', 14), ('42','19', 14),
    ('42','35', 95), ('35','42', 95), ('10','35', 77), ('35','10', 77),
    ('35','31', 7), ('31','35', 7), ('31','42', 68), ('42','31', 68)])

    

print(graph.dijkstra("27", "42"))