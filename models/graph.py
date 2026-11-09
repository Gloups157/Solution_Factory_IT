from typing import List, Tuple
from models.node import Node
from models.edge import Edge
from models.station import Station

class Graph:
    def __init__(self, nodes: List[Node], edges: List[Edge], stations: List[Station]):
        self.nodes: List[Node] = nodes
        self.edges: List[Edge] = edges
        self.stations: List[Station] = stations
        self.adjacency: List[List[Tuple[int, int]]] = [[] for _ in nodes]
        for edge in edges:
            self.adjacency[edge.first_node.num].append((edge.second_node.num, edge.time))
            self.adjacency[edge.second_node.num].append((edge.first_node.num, edge.time))


