"""
Contains representations of 3 directed graphs

Functions:
Generates a complete undirected graph with given number of nodes
Computes the in-degrees for nodes of a directed graph
Computes the in-degree distribution of a directed graph
"""

from collections import Counter

# would normally write sets as {1, 2} but the syntax is not supported in testing environment

EXAMPLE_GRAPH_0 = {
    0: set([1, 2]),
    1: set(),
    2: set(),
}

EXAMPLE_GRAPH_1 = {
    0: set([1, 4, 5]),
    1: set([2, 6]),
    2: set([3]),
    3: set([0]),
    4: set([1]),
    5: set([2]),
    6: set(),
}

EXAMPLE_GRAPH_2 = {
    0: set([1, 4, 5]),
    1: set([2, 6]),
    2: set([3, 7]),
    3: set([7]),
    4: set([1]),
    5: set([2]),
    6: set(),
    7: set([3]),
    8: set([1, 2]),
    9: set([0, 3, 4, 5, 6, 7]),
}


def make_complete_graph(num_nodes):
    """Creates a complete graph with the given number of nodes

    :param num_nodes: number of nodes in graph
    :return: dictionary representing adjacency list
    """

    graph = {}

    if num_nodes < 1:
        return graph

    # Because any list, dictionary, or set operation would take O(n) to remove
    #   an item, it doesn't help to simply assign a predefined list with the current node removed.

    for node in xrange(num_nodes):
        connections = [i for i in range(num_nodes) if i != node]  # exclude current node
        graph[node] = set(connections)

    return graph


def compute_in_degrees(digraph):
    """Takes a digraph (represented as a dictionary) and computes the in-degrees
    for the nodes in the graph. The function returns a dictionary with the same
    set of keys (nodes) as digraph whose corresponding values are the number of
    edges whose head matches a particular node.

    :param digraph:
    :return:
    """

    in_degrees = Counter()

    for node, connections in digraph.iteritems():
        if node not in in_degrees:  # all original nodes must be represented in result
            in_degrees[node] = 0
        for connection in connections:
            in_degrees[connection] += 1

    return in_degrees


def in_degree_distribution(digraph):
    """Takes a digraph (represented as a dictionary) and computes the unnormalized
    distribution of the in-degrees of the graph. The function returns a dictionary
    whose keys correspond to in-degrees of nodes in the graph. The value associated
    with each particular in-degree is the number of nodes with that in-degree. In-degrees
    with no corresponding nodes in the graph are not included in the dictionary.

    :param digraph:
    :return:
    """

    distribution = Counter()

    in_degrees = compute_in_degrees(digraph)

    for count in in_degrees.itervalues():
        distribution[count] += 1

    return distribution
