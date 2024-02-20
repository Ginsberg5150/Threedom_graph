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
    "Hillary Clinton": "Guest",
    "Jon Hamm": "Guest",
    "Amy Poehler": "Guest",
    "Elizabeth Banks": "Guest",
    "Spontaneanation": "Podcast",
    "With Special Guest Lauren Lapkus": "Podcast"
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
    ("Between Two Ferns", "Hillary Clinton"),
    ("Comedy Bang! Bang!", "Jon Hamm"),
    ("Comedy Bang! Bang!", "Amy Poehler"),
    ("Comedy Bang! Bang!", "Elizabeth Banks"),
    ("Paul F. Tompkins", "Spontaneanation"),
    ("Lauren Lapkus", "With Special Guest Lauren Lapkus"),
    ("Spontaneanation", "Earwolf"),
    ("With Special Guest Lauren Lapkus", "Earwolf")
]
G.add_edges_from(edges)

# Drawing the updated graph
plt.figure(figsize=(14, 12))
pos = nx.spring_layout(G, seed=42)  # For consistent layout
nx.draw(G, pos, with_labels=True, node_size=1500, node_color="lightgreen", font_size=9, font_weight="bold")
nx.draw_networkx_edge_labels(G, pos, edge_labels={
    # Existing labels and new labels
}, font_color='red')  # You can add the edge labels as needed

plt.title("Expanded Visualization with 'Comedy Bang! Bang!' TV Show and Connections")
plt.show()
