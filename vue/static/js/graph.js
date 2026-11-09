async function showGraph() {
  const container = document.getElementById("graph");

  try {
    const response = await fetch("/api/graph");
    if (!response.ok) {
      throw new Error(`Graph request failed (${response.status})`);
    }

    const graph = await response.json();
    const elements = [
      ...graph.nodes.map(node => ({
        data: { id: node.id, label: node.name },
        position: { x: node.x, y: node.y }
      })),
      ...graph.edges.map(edge => ({
        data: { source: edge.from, target: edge.to, time: edge.time }
      }))
    ];

    cytoscape({
      container,
      elements,
      layout: { name: "preset" },
      style: [
        { selector: "node", style: {
          "label": "data(label)", "background-color": "#2563eb",
          "font-size": 8, "width": 8, "height": 8
        }},
        { selector: "edge", style: {
          "width": 2, "line-color": "#94a3b8"
        }}
      ]
    });
  } catch (error) {
    console.error("Could not display the metro graph:", error);
    container.textContent = "Could not load the graph. Check the browser console and Flask server.";
  }
}

showGraph();