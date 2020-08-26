import re
from typing import List, Tuple, Union
from dataclasses import dataclass


# Class describing the node of the graph
@dataclass
class Node:
    # Additional information (name of city)
    data: str
    # The index at which this node stores in the graph
    index: int = None

    def __str__(self):
        return self.data


class Graph:

    def __init__(self, col: int, row: int, nodes: List[Node] = [], max_cost: int = 200000):
        # Adjacency matrix
        self.adj_matrix = [[0] * col for _ in range(row)]
        self.nodes = nodes
        self.max_cost = max_cost
        # Set the indexes for the nodes
        for i in range(len(self.nodes)):
            self.nodes[i].index = i

    @classmethod
    def from_nodes(cls, nodes: List[Node]):
        length = len(nodes)
        return cls(length, length, nodes)

    def __str__(self):
        return "\n".join([str(i) for i in self.adj_matrix])

    def connect_dir(self, source_node: Node, destination_node: Node, weight: int = 1):
        """The method sets a unidirectional edge between the nodes"""
        self.adj_matrix[source_node.index][destination_node.index] = weight

    def connect(self, node1: Node, node2: Node, weight: int = 1):
        """The method sets a bi-directional edge between the nodes"""
        self.connect_dir(node1, node2, weight)
        self.connect_dir(node2, node1, weight)

    def get_neighbors(self, node_index: int) -> List[Tuple[Node, int]]:
        """The method returns a list of neighboring nodes with a weights"""
        return [(self.nodes[col_num], self.adj_matrix[node_index][col_num])
                for col_num in range(len(self.adj_matrix[node_index])) if self.adj_matrix[node_index][col_num] != 0]

    def min_cost(self, source_node: Node, destination_node: Node) -> float:
        """The method returns the minimum price for a route from one node to another."""
        short_ways = self.dijkstra(source_node)
        destination_way = short_ways[destination_node.index]
        return destination_way[0]

    def dijkstra(self, source_node: Node) -> List[List[Union[float, List[Node]]]]:
        """
        A method that executes Dijkstra's algorithm and returns a list whose index matches the index of the node
        to which the path built. The index contains an array that consists of the price and the route (nodes list).
        """

        # An array keeps track of the distance from one to any node in self.nodes
        # Index 0 = Distance, Index 1 = Node Jumps
        dist = [[float("inf"), [self.nodes[source_node.index]]] for _ in range(len(self.nodes))]
        # All nodes initialized to infinity except for the start node
        dist[source_node.index][0] = 0
        # Index queue from indexes of all nodes
        queue = [i for i in range(len(self.nodes))]
        # A set of the currently seen indexes.
        seen_nodes = set()

        while len(queue) > 0:
            current_dist, current_node_index = float("inf"), None

            for node_index in queue:
                # Gets a node that has not been checked to be at the minimum distance from the source
                if dist[node_index][0] < current_dist and node_index not in seen_nodes:
                    current_dist = dist[node_index][0]
                    current_node_index = node_index

            queue.remove(current_node_index)
            seen_nodes.add(current_node_index)

            neighbors = self.get_neighbors(current_node_index)
            # For each link path, update the path and total distance from the source node
            # if the total distance is less than the current distance in the dist array
            for (source_node, weight) in neighbors:
                tot_dist = weight + current_dist

                if tot_dist == self.max_cost:
                    raise MaximumCostError(self.max_cost)

                if tot_dist < dist[source_node.index][0]:
                    dist[source_node.index][0] = tot_dist
                    dist[source_node.index][1] = [*dist[current_node_index][1], source_node]
        return dist


def quick_test():
    gdansk = Node("Gdansk")
    bydgoszcz = Node("Bydgoszcz")
    torun = Node("Torun")
    warszawa = Node("Warszawa")

    graph = Graph.from_nodes([gdansk, bydgoszcz, torun, warszawa])

    graph.connect(gdansk, bydgoszcz, 1)
    graph.connect(gdansk, torun, 3)
    graph.connect(bydgoszcz, torun, 1)
    graph.connect(bydgoszcz, warszawa, 4)
    graph.connect(torun, warszawa, 1)

    print(graph)
    print(graph.min_cost(gdansk, warszawa))
    print(graph.min_cost(bydgoszcz, warszawa))


class ValidationError(Exception):
    pass


class MaximumCostError(Exception):

    def __init__(self, max_cost):
        self.message = f"Maximum cost raised ({max_cost})!"


def main():
    tests_number: int = int(input("The number of tests <= 10: "))

    if tests_number > 10 or tests_number <= 0:
        raise ValidationError("The number of tests must be <= 10000 and > 0!")

    for _ in range(tests_number):
        cities_number: int = int(input("the number of cities <= 10000: "))

        if cities_number > 10000 or cities_number <= 0:
            raise ValidationError("The number of cities must be <= 10000 and > 0!")

        nodes = [Node(str(i)) for i in range(cities_number)]
        cities = {}
        graph = Graph.from_nodes(nodes)

        for i in range(cities_number):
            city_name: str = input("City name: ")
            city_pattern = re.compile("^[a-z]$")
            if len(city_name) > 10 or not city_pattern.match(city_name):
                raise ValidationError("The name of a city is a string containing characters a,...,z "
                                      "and is at most 10 characters long.")

            nodes[i].data = city_name
            cities[city_name] = nodes[i]

            neighbors_number: int = int(input("The number of neighbors: "))
            for _ in range(neighbors_number):
                data = input(">> ")
                neighbor_data = data.split(" ")
                neighbor_index, weight = [int(s) for s in neighbor_data]

                graph.connect_dir(nodes[i], nodes[neighbor_index - 1], weight)

        paths_number: int = int(input("The number of paths to find <= 100: "))

        if cities_number > 100 or cities_number <= 0:
            raise ValidationError("The number of paths to find must be <= 10000 and > 0!")

        paths = [input(f"Path #{i + 1}: ") for i in range(paths_number)]

        print("\nResult: ")
        for path in paths:
            cities_names = path.split()
            source_city, destination_node = cities[cities_names[0]], cities[cities_names[1]]
            result = graph.min_cost(source_city, destination_node)
            print(f"{path}: {result}")


if __name__ == '__main__':
    try:
        main()
    except ValueError:
        print("Invalid input!")
    except ValidationError as e:
        print(e)
    except MaximumCostError as e:
        print(e)
