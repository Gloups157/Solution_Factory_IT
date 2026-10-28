class Station:
    def __init__(self, x: int, y: int, station_name: str):
        self.x: int = x
        self.y: int = y
        self.station_name: str = station_name

    def print_station(self):
       print(f"{self.x} {self.y} {self.station_name}")