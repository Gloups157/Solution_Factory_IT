from models.graph import Graph
from models.node import Node

def depth_first_search(graph: Graph, starting_node: Node) -> bool:
    return dfs_aux(starting_node, set(), len(graph.nodes))

def dfs_aux(node: Node, visited: set[Node], graph_nodes_len: int) -> bool:
    visited.add(node)
    if graph_nodes_len == len(visited):
        return True
    for n in node.neighbors:
        if n not in visited:
            if dfs_aux(n, visited, graph_nodes_len):
                return True
    return False
