import networkx as nx
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import os
import argparse
from datetime import datetime
from Vertices import Vertices

# argument parsing
parser = argparse.ArgumentParser(description="Process a graph file.")
parser.add_argument("filepath", type=str, help="Path to the input graph file")
args = parser.parse_args()
filename = args.filepath



#filename = ".venv/res/sample"
vertices = Vertices()

    
        

try:
    with open(filename, "r") as file:
        for line in file:
            line = line.strip()
            if len(line) > 0:
                if line[0] == 'p':
                    parts = line.strip().split()
                    vertices.create_vertices(parts[2])
                elif line[0] == 'e':
                    vertices.add_edge(line)
                else:
                    pass
except IOError as e:
    print(f"Error reading file: {e}")

queue = vertices.get_queue()

""" for i, q in enumerate(queue):
    if len(q) == 0:
        break
    print(f"Queue {i + 1}")
    for edge in q:
        print(edge) """


#now we draw the graph with networkx

#create the graph
G = nx.Graph()

# Add nodes to the graph from the vertices
for vertex in vertices.vertices:
    G.add_node(vertex)


# Add edges to the graph from the edges in vertices
for vs, neighbors in vertices.vertices.items():
    for vt in neighbors:
        if vs < vt:  # Avoid duplicate edges (undirected graph)
            G.add_edge(vs, vt)

#print(len(vertices.vertices))

# Define positions: all nodes on a line
pos = {vertex: (vertex, 0) for vertex in vertices.vertices}


# Create figure
plt.figure(figsize=(max(10, len(G.nodes) / 1.5) ,  max(8, len(G.nodes) / 8)))


# Draw stuff
nx.draw_networkx_nodes(G, pos, node_color='white', node_size=300)
nx.draw_networkx_labels(G, pos)

colors = [
    "red", "green", "blue", "orange", 
    "purple", "pink", "brown", "gray"
]



out_of_colors = False
i = 0
# Iterate through each queue
for q in queue:
    if len(q) == 0:
        continue  

    for edge in q:
        # Extract vertices from the Edge object
        vertex1 = edge.vertex1
        vertex2 = edge.vertex2

        # Check if we have run out of colors
        edge_color = colors[i] if i < len(colors) else "black"
        if i >= len(colors):
            out_of_colors = True  # Mark that we've run out of colors

        
        # Draw the edge between the two vertices
        nx.draw_networkx_edges(
            G, pos, edgelist=[(vertex1, vertex2)],
            edge_color=edge_color,
            connectionstyle="arc3,rad=0.3",
            arrows=True
        )
    i += 1

# Create a unique folder name using current date and time
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
output_folder = f"output_pages_{timestamp}"
os.makedirs(output_folder, exist_ok=True)

# First text line: number of pages
num_non_empty_queues = len([q for q in queue if len(q) > 0])
plt.text(0.5, 1.10, f"Pages required: {num_non_empty_queues}", 
ha="center", va="bottom", fontsize=14, color="black", transform=plt.gca().transAxes)

if out_of_colors:
    # Add a text annotation to the plot
    plt.text(0.5, 1.05, "Ran out of colors, some edges are shown in black.", 
             ha="center", va="bottom", fontsize=12, color="black", 
             transform=plt.gca().transAxes)
plt.axis('off')
plt.savefig(os.path.join(output_folder,"graph_ourview.png"), format="PNG", bbox_inches="tight")  # Save as PNG
plt.close()



#create and save a separate figure for each queue
for i, q in enumerate(queue):
    if len(q) == 0:
        continue

    # Create a new figure for each queue
    plt.figure(figsize=(max(10, len(G.nodes) / 1.5)  ,  max(8, len(G.nodes) / 8)))

    # Draw all nodes (white)
    nx.draw_networkx_nodes(G, pos, node_color='white', node_size=300)
    nx.draw_networkx_labels(G, pos)


    # Draw only the edges from this queue
    edgelist = [(edge.vertex1, edge.vertex2) for edge in q]
    nx.draw_networkx_edges(
        G, pos, edgelist=edgelist,
        edge_color="black",
        connectionstyle="arc3,rad=0.3",
        arrows=True
    )

    # Add title
    plt.text(0.5, 1.05, f"Page {i + 1}", 
             ha="center", va="bottom", fontsize=14, color="black",
             transform=plt.gca().transAxes)

    # Save the figure
    plt.axis('off')
    plt.savefig(os.path.join(output_folder,f"graph_page{i + 1}.png"), format="PNG", bbox_inches="tight")
    plt.close()









