import heapq
import math
from typing import List

from models.graph import Graph
from models.node import Node
from models.edge import Edge

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

def kruskal(graph: Graph) -> tuple[List[Edge], int]:
    parent: List[int] = []
    for i in range(len(graph.nodes)):
        parent.append(i)
    tree: List[Edge] = []
    total_time: int = 0

    sorted_edges = sorted(graph.edges, key=lambda edge: edge.time)
    for edge in sorted_edges:
        root1 = find_root(parent, edge.first_node.num)
        root2 = find_root(parent, edge.second_node.num)
        if root1 != root2:
            parent[root1] = root2
            tree.append(edge)
            total_time += edge.time
    return tree, total_time

def find_root(parent: List[int], num: int) -> int:
    while parent[num] != num:
        num = parent[num]
    return num

def dijkstra(graph: Graph, starting_node: Node, ending_node: Node) -> tuple[float, List[Node]]:
    n = len(graph.nodes)
    times = [math.inf] * n
    previous_nodes = [None] * n

    times[starting_node.num] = 0
    queue = [(0, starting_node.num)]

    while queue:
        current_time, current_num = heapq.heappop(queue)
        if current_num == ending_node.num:
            break
        if current_time > times[current_num]:
            continue
        # Need to implement the logic to explore neighbors

    path = []
    current_num = ending_node.num
    while current_num is not None:
        path.append(graph.nodes[current_num])
        current_num = previous_nodes[current_num]

    return times[ending_node.num], path