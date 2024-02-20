import matplotlib.pyplot as plt
import networkx as nx

# Updating the graph with additional nodes and edges for new connections
G = nx.Graph()

# Adding nodes with roles
nodes = {
    "Threedom": "Podcast",
    "Lauren Lapkus": "Host",
    "Paul F. Tompkins": "Host",
    "Scott Aukerman": "Host",
    "Earwolf": "Parent Company",
    "Comedy Bang! Bang!": "Related Show",
    "Between Two Ferns": "Related Show",
    "Weird Al Yankovic": "Guest/Bandleader",
    "Jason Mantzoukas": "Guest",
    "Nick Kroll": "Guest",
    "Reggie Watts": "Bandleader",
    "Zach Galifianakis": "Creator/Guest",
    "Barack Obama": "Guest",
    "Brad Pitt": "Guest",
    "Justin Bieber": "Guest",
    "Hillary Clinton": "Guest"
}
for node, role in nodes.items():
    G.add_node(node, role=role)

# Adding edges for connections
edges = [
    ("Threedom", "Lauren Lapkus"),
    ("Threedom", "Paul F. Tompkins"),
    ("Threedom", "Scott Aukerman"),
    ("Scott Aukerman", "Comedy Bang! Bang!"),
    ("Scott Aukerman", "Between Two Ferns"),
    ("Threedom", "Earwolf"),
    ("Comedy Bang! Bang!", "Earwolf"),
    ("Between Two Ferns", "Earwolf"),
    ("Comedy Bang! Bang!", "Paul F. Tompkins"),
    ("Comedy Bang! Bang!", "Lauren Lapkus"),
    ("Comedy Bang! Bang!", "Weird Al Yankovic"),
    ("Comedy Bang! Bang!", "Jason Mantzoukas"),
    ("Comedy Bang! Bang!", "Nick Kroll"),
    ("Comedy Bang! Bang!", "Reggie Watts"),
    ("Between Two Ferns", "Zach Galifianakis"),
    ("Between Two Ferns", "Barack Obama"),
    ("Between Two Ferns", "Brad Pitt"),
    ("Between Two Ferns", "Justin Bieber"),
    ("Between Two Ferns", "Hillary Clinton")
]
G.add_edges_from(edges)

# Drawing the updated graph
plt.figure(figsize=(12, 10))
pos = nx.spring_layout(G, seed=42)  # For consistent layout
nx.draw(G, pos, with_labels=True, node_size=1500, node_color="lightblue", font_size=9, font_weight="bold")
nx.draw_networkx_edge_labels(G, pos, edge_labels={
    ("Threedom", "Lauren Lapkus"): "Hosts",
    ("Threedom", "Paul F. Tompkins"): "Hosts",
    ("Threedom", "Scott Aukerman"): "Hosts",
    ("Scott Aukerman", "Comedy Bang! Bang!"): "Hosts",
    ("Scott Aukerman", "Between Two Ferns"): "Created By",
    ("Threedom", "Earwolf"): "Produced By",
    ("Comedy Bang! Bang!", "Earwolf"): "Produced By",
    ("Between Two Ferns", "Earwolf"): "Distributed By",
    ("Comedy Bang! Bang!", "Paul F. Tompkins"): "Frequent Guest",
    ("Comedy Bang! Bang!", "Lauren Lapkus"): "Guest",
    ("Comedy Bang! Bang!", "Weird Al Yankovic"): "Bandleader",
    ("Comedy Bang! Bang!", "Jason Mantzoukas"): "Guest",
    ("Comedy Bang! Bang!", "Nick Kroll"): "Guest",
    ("Comedy Bang! Bang!", "Reggie Watts"): "Original Bandleader",
    ("Between Two Ferns", "Zach Galifianakis"): "Star",
    ("Between Two Ferns", "Barack Obama"): "Featured Guest",
    ("Between Two Ferns", "Brad Pitt"): "Featured Guest",
    ("Between Two Ferns", "Justin Bieber"): "Featured Guest",
    ("Between Two Ferns", "Hillary Clinton"): "Featured Guest",
}, font_color='red')

plt.title("Expanded Visualization of 'Threedom' and Related Projects")
plt.show()
