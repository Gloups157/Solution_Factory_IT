from typing import List
from models.node import Node
from models.edge import Edge

metro_data_path = "Version1/metro.txt"

nodes: List[Node] = []
edges: List[Edge] = []

def load_metro_datas():
    with open(metro_data_path, "r", encoding="utf-8") as f:
        start_data = False
        for line in f.readlines():
            if "V 0000" in line:
                start_data = True

            if 'V' in line[0] and start_data:
                # V 0000 Abbesses ;12 ;False 0

                # {"V 0000 Abbesses ", "12 ", "False 0"}
                split_line = line.split(";")

                # {"V", "0000", "Abbesses"}
                first_part = split_line[0].split(" ")
                num_node = int(first_part[1])

                # Concatenate name (can be strings with space between)
                name_node = ""
                full_name = first_part[2:]
                full_name_len = len(full_name)
                for index, name in enumerate(full_name):
                    name_node += str(name)
                    if index < full_name_len - 2:
                        name_node += " "

                num_line = split_line[1][:-1]

                last_part = split_line[2].split(" ")
                terminus = bool(last_part[0])

                # The connection can have space
                connection = 0
                for num in last_part[1:]:
                    if num.isdigit():
                        connection = int(num)
                nodes.append(Node(num_node, name_node, num_line, terminus, connection))

            if 'E' in line[0] and start_data:
                split_line = line.split(" ")
                first_node_num = int(split_line[1])
                second_node_num = int(split_line[2])
                time = int(split_line[3])
                edges.append(Edge(nodes[first_node_num], nodes[second_node_num], time))




def main():
    load_metro_datas()
    for node in nodes:
        node.print_node()
    for edge in edges:
        edge.print_edge()

if __name__ == '__main__':
    main()
