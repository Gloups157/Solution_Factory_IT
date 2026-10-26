class Node:
    def __init__(self, num: int, name: str, num_line: str, terminus: bool, connection: int):
        self.num: int = num # num_sommet
        self.name: str = name # nom_sommet
        self.num_line: str = num_line # numéro_ligne
        self.terminus: bool = terminus # si_terminus
        self.connection: int = connection #branchement

    def print_node(self):
       print(f"{self.num} {self.name} {self.num_line} {self.terminus} {self.connection}")