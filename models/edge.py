from models.node import Node

class Edge:
    def __init__(self, first: Node, second: Node, time: int):
        self.first_node: Node = first
        self.second_node: Node = second
        self.time: int = time # in second

    def print_edge(self):
        print(f"{self.first_node.num} {self.second_node.num} {self.time}")