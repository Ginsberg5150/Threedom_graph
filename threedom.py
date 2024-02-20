import matplotlib.pyplot as plt
import networkx as nx

# Defining the graph
G = nx.Graph()

# Adding nodes with the role attribute
G.add_node("Threedom", role="Podcast")
G.add_node("Lauren Lapkus", role="Host")
G.add_node("Paul F. Tompkins", role="Host")
G.add_node("Scott Aukerman", role="Host")
G.add_node("Earwolf", role="Parent Company")
G.add_node("Comedy Bang! Bang!", role="Related Show")
G.add_node("Between Two Ferns", role="Related Show")

# Adding edges to connect nodes
G.add_edge("Threedom", "Lauren Lapkus")
G.add_edge("Threedom", "Paul F. Tompkins")
G.add_edge("Threedom", "Scott Aukerman")
G.add_edge("Scott Aukerman", "Comedy Bang! Bang!")
G.add_edge("Scott Aukerman", "Between Two Ferns")
G.add_edge("Threedom", "Earwolf")
G.add_edge("Comedy Bang! Bang!", "Earwolf")
G.add_edge("Between Two Ferns", "Earwolf")

# Drawing the graph
plt.figure(figsize=(10, 8))
pos = nx.spring_layout(G, seed=42)  # For consistent layout
nx.draw(G, pos, with_labels=True, node_size=2000, node_color="skyblue", font_size=10, font_weight="bold")
nx.draw_networkx_edge_labels(G, pos, edge_labels={
    ("Threedom", "Lauren Lapkus"): "Hosts",
    ("Threedom", "Paul F. Tompkins"): "Hosts",
    ("Threedom", "Scott Aukerman"): "Hosts",
    ("Scott Aukerman", "Comedy Bang! Bang!"): "Hosts",
    ("Scott Aukerman", "Between Two Ferns"): "Created By",
    ("Threedom", "Earwolf"): "Produced By",
    ("Comedy Bang! Bang!", "Earwolf"): "Produced By",
    ("Between Two Ferns", "Earwolf"): "Distributed By"
}, font_color='red')

plt.title("Visualization of 'Threedom' Podcast and Connections")
plt.show()
