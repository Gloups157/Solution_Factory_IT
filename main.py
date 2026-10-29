from typing import List

from models.graph import Graph
from models.node import Node
from models.edge import Edge
from models.station import Station
from  algos.data_loader import *
from algos.algos import depth_first_search, kruskal

def main():
    nodes, edges = load_metro_data()
    stations = load_stations_data()

    graph = Graph(nodes, edges, stations)
    print(depth_first_search(graph, graph.nodes[100]))

    tree, total_time = kruskal(graph)
    print(len(tree), total_time)

if __name__ == '__main__':
    main()
