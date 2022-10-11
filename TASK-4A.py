
from collections import defaultdict

graphTer = {
    '6' : ['11' , '3' ],
    '11' : ['8','1'],
    '8' : [],
    '1' : ['5'],
    '5' : [],
    '3' : ['12','9'],
    '12' : ['2','15'],
    '9' : ['7'],
    '2' : ['19','4'],
    '15' : [],
    '7' : [],
    '19' : [],
    '4' : ['17','13'],
    '17': [],
    '13' : ['31'],
    '31' : []
}
print(graphTer)
visited = [] # List for visited nodes.
queue = []     #Initialize a queue
visitedSet = set()

class Graph():
    def __init__(self):
        self.edges = defaultdict(list)
        self.weights = {}

    def add_edge(self, from_node, to_node, weight):
        # Note: assumes edges are bi-directional
        self.edges[from_node].append(to_node)
        self.edges[to_node].append(from_node)
        self.weights[(from_node, to_node)] = weight
        self.weights[(to_node, from_node)] = weight


graph = Graph()
edges = [
    ('A', 'B', 6),
    ('B', 'D', 11),
    ('B', 'E', 1),
    ('E', 'H', 5),
    ('A', 'C', 3),
    ('C', 'F', 12),
    ('C', 'G', 9),
    ('F', 'I', 2),
    ('F', 'J', 15),
    ('I', 'L', 19),
    ('J', 'M', 4),
    ('M', 'N', 17),
    ('M', 'O', 13),
    ('O', 'P', 31),
    ('G', 'K', 7),
]

for edge in edges:
    graph.add_edge(*edge)

def breadthFirst(visited, queue, graphTer, node):

    print("This is the breadth First traverse : ")

    visited.append(node)
    queue.append(node)

    while queue:
        k = queue.pop(0)
        print (k  , end = " ->")

        for nextnodes in graphTer[k]:
            if nextnodes not in visited:
                visited.append(nextnodes)
                queue.append(nextnodes)
    return

def deapthFirst(visited, graph, node):  #function for dfs
    if node not in visited:
        print (node)
        visited.add(node)
        for x in graph[node]:
            deapthFirst(visited, graph, x)

def AStar(graph,initial,end):
    # shortest paths is a dict of nodes
    # whose value is a tuple of (previous node, weight)
    print("De bug")
    shortest_paths = {initial: (None, 0)}
    current_node = initial
    visited = set()

    while current_node != end:
        visited.add(current_node)
        destinations = graph.edges[current_node]
        weight_to_current_node = shortest_paths[current_node][1]

        for next_node in destinations:
            weight = graph.weights[(current_node, next_node)] + weight_to_current_node
            if next_node not in shortest_paths:
                shortest_paths[next_node] = (current_node, weight)
            else:
                current_shortest_weight = shortest_paths[next_node][1]
                if current_shortest_weight > weight:
                    shortest_paths[next_node] = (current_node, weight)

        next_destinations = {node: shortest_paths[node] for node in shortest_paths if node not in visited}
        if not next_destinations:
            return "Route Not Possible"
        # next node is the destination with the lowest weight
        current_node = min(next_destinations, key=lambda k: next_destinations[k][1])

    # Work back through destinations in shortest path
    path = []
    while current_node is not None:
        path.append(current_node)
        next_node = shortest_paths[current_node][0]
        current_node = next_node
    # Reverse path
    path = path[::-1]
    return path

    # snd has present distances from start to all other nodes
    # the default value is +infinity
    snd = {}


def main():
    print("Welcome to the traverse thingy ")
    searchednode = input("choose what number you are trying to traverse to  \n")
    searchednodeAlp = input("choose what letter you are trying to traverse to  \n")
    breadthFirst(visited,queue,graphTer, searchednode)
    print("\n This is the Depth First traverse : ")
    deapthFirst(visitedSet,graphTer,searchednode)
    #AStar(graph,'A','P')


if __name__ == '__main__':
    main()