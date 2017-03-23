#!/usr/bin/python3.1
#shortest_path.py


# Usage
# Create a file according to Graph() instructions below.
# Run this program with the previous file name, first
# node and end node.


__author__ = 'José Lopes O. Júnior'
__version__ = '1.0.0'
__license__ = 'GPLv3+'


from sys import argv


class Arc(object):
    """An arc between 2 nodes.
    cost is the path cost between them.
    """

    def __init__(self, cost=65536):
        self.cost = cost

    def __str__(self):
        return '({0:05})'.format(self.cost)

class Graph(object):
    """The Graph itself.

    Stores a graph in a matrix like:
          node1 node2 node3
    node1    c1    c2    c3
    node2    c4    c5    c6
    node3    c7    c8    c9
    
    For node1, line 1, for example, cost between
    node1-node1 is c1, between node1-node2 is c2,
    node1-node3 is c3.  When you need to describe 
    an infinity cost, use letter 'i'.  All other
    costs must be numbers.

    This matrix is imported from a file
    with a sintax like:
    i c2 c3
    c4 i c6
    c7 c8 i

    When it is imported, the feed method
    turns i to self.infinity.

    """

    def __init__(self, graph, infinity=65536):
        self.infinity = infinity
        self.graph = self.feed(graph)
        self.maxnodes = len(self.graph[0])

    def feed(self, sfile):
        """Fills self.graph with values in the given file."""

        graph, line_number = [], -1

        with open(sfile, 'r') as sf:
            for line in sf.readlines():
                graph.append([])
                line_number += 1
                records = line.split()

                for record in records:
                    if record == 'i':
                        graph[line_number].append(Arc(self.infinity))
                    else:
                        graph[line_number].append(Arc(int(record)))

        return graph

    def __str__(self):
        ret = ''

        for line in range(self.maxnodes):
            ret += '\n'

            for column in range(self.maxnodes):
                ret += str(self.graph[line][column]) + '\t'

        ret += '\n'

        return ret

    def shortest_path(self, source):
        """Dijkstra's algorithm."""

        visited, length, predecessor = [], [], []

        for index in range(self.maxnodes):
            visited.append(False)
            length.append(self.infinity)
            predecessor.append(None)

        current, next = source, source
        visited[source] = True
        length[source] = 0

        while 1:
            next_length = self.infinity

            # Calculates neighbor's costs.
            position = 0
            for index in self.graph[current]:  # Checks all node's archs
                if index.cost != self.infinity:  # Is adjacent
                    if length[position] > length[current]:
                        length[position] = length[current] + index.cost
                        predecessor[position] = current
                position += 1

            # Who's next?
            position = 0
            for index in visited:
                if not index:
                    if length[position] < next_length:
                        next = position
                        next_length = length[next]
                position += 1

            if next_length != self.infinity:
                visited[next] = True
                current = next

            else:
                break  # Done

        return [length, predecessor]

    def follow_path(self, source, target):
        """Finds and returns the shortest path."""

        predecessor = self.shortest_path(source)[1]

        path = []
        while (target != source):
            path.append(target)

            if predecessor[target] is None:  # If returning to source
                target = source
            else:
                target = predecessor[target]

        path.append(source)
        path.reverse()

        return path


#
# Main
# 

if __name__ == '__main__':
    try:
        print(Graph(argv[1]).follow_path(int(argv[2]), int(argv[3])))

    except IndexError:
        print('Usage: $ {0} file source target'.format(argv[0]))

