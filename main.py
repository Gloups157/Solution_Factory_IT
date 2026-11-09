from models.graph import Graph
from algos.data_loader import *
from algos.algos import depth_first_search, kruskal, dijkstra_between_nodes, dijkstra_between_stations

def main():
    nodes, edges = load_metro_data()
    stations = load_stations_data()

    graph = Graph(nodes, edges, stations)
    print(depth_first_search(graph, graph.nodes[100]))
    print("----------------------")

    tree, total_time = kruskal(graph)
    print(len(tree), total_time)
    print("----------------------")

    time, path = dijkstra_between_nodes(graph, graph.nodes[0], graph.nodes[18])
    print(f"Abbesses -> Bastille ligne 8 : {time}")
    for node in path:
        node.print_node()
    print("----------------------")
    
    time, path = dijkstra_between_stations(graph, "Abbesses", "Bastille")
    print(f"Abbesses -> Bastille : {time}")
    for node in path:
        node.print_node()


if __name__ == '__main__':
    main()
