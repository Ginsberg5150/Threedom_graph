import matplotlib.pyplot as plt
import networkx as nx

# Initialize the graph
G = nx.Graph()

# Define nodes with their roles
nodes_with_roles = {
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
    "SiriusXM": "Parent Company",
    "Stitcher": "Acquisition",
    "Jim Meyer": "Executive",
    "How Did This Get Made?": "Podcast",
    "Unspooled": "Podcast",
    "Crooked Media": "Partnership",
    "Jon Hamm": "Guest",
    "Amy Poehler": "Guest",
    "Elizabeth Banks": "Guest",
    "Spontaneanation": "Podcast",
    "With Special Guest Lauren Lapkus": "Podcast"
}    
    # Add nodes to the graph
for node, role in nodes_with_roles.items():
    G.add_node(node, role=role)

# Define edges between nodes
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
    ("SiriusXM", "Earwolf"),
    ("SiriusXM", "Stitcher"),
    ("Stitcher", "How Did This Get Made?"),
    ("Stitcher", "Unspooled"),
    ("Stitcher", "Crooked Media"),
    ("Jim Meyer", "SiriusXM")
]

# Add edges to the graph
G.add_edges_from(edges)

# Custom color scheme for nodes
node_colors = {"Podcast": "green", "Host": "lightblue", "Bandleader": "lightblue", "Creator/Guest": "lightblue", "Parent Company": "gold", "Acquisition": "gold", "Executive": "gold", "Partnership": "gold"}

# Apply colors based on roles
color_map = [node_colors.get(node[1]['role'], 'grey') for node in G.nodes(data=True)]

# Drawing the graph
plt.figure(figsize=(18, 16))
pos = nx.spring_layout(G, seed=42)  # For consistent layout
nx.draw(G, pos, with_labels=True, node_size=2000, node_color=color_map, font_size=12, font_weight="bold")

# Define and draw edge labels
edge_labels = {
    ("Threedom", "Lauren Lapkus"): "Hosts",
    ("Threedom", "Paul F. Tompkins"): "Hosts",
    ("Threedom", "Scott Aukerman"): "Hosts",
    ("Scott Aukerman", "Comedy Bang! Bang!"): "Hosts",
    ("Scott Aukerman", "Between Two Ferns"): "Created By",
    ("SiriusXM", "Earwolf"): "Owns",
    ("SiriusXM", "Stitcher"): "Acquired",
    ("Stitcher", "How Did This Get Made?"): "Hosts",
    ("Stitcher", "Unspooled"): "Hosts",
    ("Stitcher", "Crooked Media"): "Partnership",
    ("Jim Meyer", "SiriusXM"): "CEO",
    ("Threedom", "Earwolf"): "Produced By",
    ("Comedy Bang! Bang!", "Earwolf"): "Produced By",
    ("Between Two Ferns", "Earwolf"): "Distributed By",
    ("Comedy Bang! Bang!", "Jon Hamm"): "Guest",
    ("Comedy Bang! Bang!", "Amy Poehler"): "Guest",
    ("Comedy Bang! Bang!", "Elizabeth Banks"): "Guest",
    ("Paul F. Tompkins", "Spontaneanation"): "Hosts",
    ("Lauren Lapkus", "With Special Guest Lauren Lapkus"): "Hosts",
    ("Spontaneanation", "Earwolf"): "Produced By",
    ("With Special Guest Lauren Lapkus", "Earwolf"): "Produced By",
    ("Zach Galifianakis", "Between Two Ferns"): "Starred In",
    ("Between Two Ferns", "Earwolf"): "Promoted By",
    ("Comedy Bang! Bang!", "Paul F. Tompkins"): "Frequent Guest",
    ("Comedy Bang! Bang!", "Lauren Lapkus"): "Guest",
    ("Comedy Bang! Bang!", "Weird Al Yankovic"): "Bandleader",
    ("Comedy Bang! Bang!", "Jason Mantzoukas"): "Guest",
    ("Comedy Bang! Bang!", "Nick Kroll"): "Guest",
    ("Comedy Bang! Bang!", "Reggie Watts"): "Original Bandleader",
    ("Zach Galifianakis", "Between Two Ferns"):"Starred In",
    ("Between Two Ferns", "Zach Galifianakis"): "Creator/Guest",
    ("Between Two Ferns", "Barack Obama"): "Featured Guest",
    ("Between Two Ferns", "Brad Pitt"): "Featured Guest",
    ("Between Two Ferns", "Justin Bieber"): "Featured Guest",
    ("Between Two Ferns", "Hillary Clinton"): "Featured Guest",
    ("Between Two Ferns", "Earwolf"): "Promoted By"
}

nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='black')

plt.title("Expanded CBB Universe with SiriusXM and Affiliations")
plt.show()
