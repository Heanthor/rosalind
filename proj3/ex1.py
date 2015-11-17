filename = "ex1.txt"


# read input from file
# expected format:
#   k
#   text
# output:
#   tuple k, text
def readdat(filename, read_nums):
    with open(filename, 'r') as f:
        if read_nums:
            k, d = map(int, f.readline().strip().split(" "))

        kmers = f.read().strip().replace("\r", "").split("\n")
    return k, d, kmers


class PathNode(object):

    def __init__(self, data, prev, next):
        self.data = data
        self.prev = prev
        self.next = next


# a doubly linked list, containing a path from node to node
class Path(object):

    head = None
    tail = None

    def add_node(self, data):
        new_node = PathNode(data, None, None)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            new_node.prev = self.tail
            new_node.next = None
            self.tail.next = new_node
            self.tail = new_node



# a class to represent nodes in a debruijn graph
# slots:
#   _label: the k-1 mer label
#   _targets: list of target nodes for outgoing edges
#   _start: start node?
#   _end: end node?
class Node:
    # initialize node with label and empty targets list
    def __init__(self, label):
        self._label = label
        self._targets = []
        self._start = False
        self._end = False

    # get a string representation of node
    # "label -> <comma_separated_list_of_target_labels>"
    def __repr__(self):
        targets = [target._label for target in self._targets]
        targets = ",".join(targets)
        return self._label + " -> " + targets

    # add target node to target list
    def add_target(self, target):
        self._targets.append(target)

    # return the number of targets for this node
    def num_targets(self):
        return len(self._targets)

    # marks this node as a start node
    def set_start(self):
        self._start = True

    # marks this node as an end node
    def set_end(self):
        self._end = True

    def get_label(self):
        return self._label

    def is_end(self):
        return self._end


# a class representing a Debruijn graph
# slots:
#   _nodes: a dictionary, keys are node labels, values are Node objects
class Graph:
    # intialize with empty dictionary
    def __init__(self):
        self._nodes = {}

    # check if node with given label is in the node dictionary
    def __contains__(self, label):
        return label in self._nodes

    # return the node corresponding to given label
    def __getitem__(self, label):
        return self._nodes[label]

    # iterate over nodes in graph
    def __iter__(self):
        return self._nodes.itervalues()

    # string representation of graph
    # calls __repr__ method for each node,
    # sorts resulting strings
    # returns newline separated strings
    def __repr__(self):
        nodes = [node.__repr__() for node in self if node.num_targets() > 0]
        return "\n".join(sorted(nodes))

    # add node to graph with given label
    # does not check if node with given label is already
    # in the graph
    def add_node(self, label):
        self._nodes[label] = Node(label)

    # add an edge between nodes with given source and target labels
    # adds nodes to graph with corresponding label if needed
    def add_edge(self, source_label, target_label):
        if not source_label in self:
            self.add_node(source_label)
        if not target_label in self:
            self.add_node(target_label)
        self[source_label].add_target(self[target_label])

    # get the start node of the graph
    def get_start(self):
        for node in self._nodes:
            if self._nodes[node]._start:
                return node

    def get_edges(self, label):
        return self[label]._targets

    # get the end node of the graph
    def get_end(self):
        for node in self._nodes:
            if self._nodes[node]._end:
                return node


# build debruijn graph, i.e., k-mer overlap graph
# from given set of kmers
#
# input:
#   kmers: list of kmers
# output:
#   an object of class Graph
def build_graph(kmers):
    # initalize graph object
    graph = Graph()

    count = 0
    # add an edge for each kmer in list
    for kmer in kmers:
        prefix_string, suffix_string = kmer.split("|")
        source_label = prefix_string[:-1] + "|" + suffix_string[:-1]
        target_label = prefix_string[1:] + "|" + suffix_string[1:]

        # use the add edge method in graph class
        graph.add_edge(source_label, target_label)
    return graph


# add start and end labels to nodes
def set_start_end(graph):
    targeted_nodes = set()

    # the end node will have no targets
    for node in graph._nodes:
        tmp = graph[node]
        if len(tmp._targets) == 0:
            tmp.set_end()
        else:
            # record all nodes that have been targeted by other nodes, for start
            [targeted_nodes.add(x) for x in tmp._targets]

    # the start node will not be targeted by any node
    for node in graph._nodes:
        tmp = graph[node]

        if tmp not in targeted_nodes:
            tmp.set_start()
            break

    return graph


# creates a cycle in the graph, making an edge between the end node and the start node
def create_cycle(graph):
    graph.add_edge(graph.get_end(), graph.get_start())

    return graph


def find_cycle(graph):
    start = graph.get_start()
    cycle = Path()  # start with start node
    cycle.add_node(graph[start])
    multiple_edges = []
    current_node = None

    while current_node != start:
        # first time only
        if current_node is None:
            current_node = start

        if len(graph.get_edges(current_node)) > 1:
            # node has multiple outgoing edges, so it will have to be backtracked to
            multiple_edges.append(current_node)

        next_node = graph[current_node]._targets[0]  # gets first edge away from node
        cycle.add_node(next_node)

        current_node = next_node._label

        if graph[current_node].is_end():
            break

    return cycle


def reconstruct_string(cycle, d):
    nodes = []
    current = cycle.head

    while current is not None:
        nodes.append(current.data)
        current = current.next

    first_strings = [x._label.split("|")[0] for x in nodes]
    second_strings = [x._label.split("|")[1] for x in nodes]

    genome = first_strings[0]  # starting string

    for i in xrange(1, d + 2):  # fill d spaces in gap between first two kmers
        genome += first_strings[i][-1:]

    genome += second_strings[0]  # now, can build genome from second strings only

    for string in second_strings[1:]:
        genome += string[-1:]

    return genome


def main(filename):
    k, n, pairs = readdat(filename, True)
    graph = build_graph(pairs)
    graph = set_start_end(graph)
    graph = create_cycle(graph)
    cycle = find_cycle(graph)
    genome = reconstruct_string(cycle, n)

    print genome



def main2(filename, k, n):
    a, b, pairs = readdat(filename, False)
    graph = build_graph(pairs)
    graph = set_start_end(graph)
    graph = create_cycle(graph)
    cycle = find_cycle(graph)
    genome = reconstruct_string(cycle, n)

    return genome

main(filename)
# # this is here so this plays nicely with ipython %loadpy magic
# if __name__ == '__main__' and 'get_ipython' not in dir():
#     filename = sys.argv[1]
#     main(filename)
