class Station:
    def __init__(self, x, y, station_name):
        self.x = x
        self.y = y
        self.station_name = station_name

    def print_station(self):
       print(f"{self.x} {self.y} {self.station_name}")