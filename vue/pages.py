# pages that return HTML

from flask import Flask, jsonify, render_template
from algos.data_loader import load_metro_data, load_stations_data

app = Flask(__name__)
nodes, edges = load_metro_data()
stations = load_stations_data()

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/api/graph')
def graph_data():
    positions = {station.station_name.strip(): station for station in stations}

    return jsonify({
        "nodes": [
            {
                "id": str(node.num),
                "name": node.name,
                "x": positions[node.name.strip()].x,
                "y": positions[node.name.strip()].y,
            }
            for node in nodes
            if node.name in positions
        ],
        "edges": [
            {
                "from": str(edge.first_node.num),
                "to": str(edge.second_node.num),
                "time": edge.time,
            }
            for edge in edges
        ],
    })