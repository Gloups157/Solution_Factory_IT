from typing import List
from models.node import Node
from models.edge import Edge
from models.station import Station

class Graph:
    def __init__(self, nodes: List[Node], edges: List[Edge], stations: List[Station]):
        self.nodes: List[Node] = nodes
        self.edges: List[Edge] = edges
        self.stations: List[Station] = stations

