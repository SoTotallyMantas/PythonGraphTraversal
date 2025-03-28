from random import randint
import networkx as nx
import matplotlib.pyplot as plt
import collections
from collections import deque
import matplotlib.patches as mpatches
# Sugeneruojamas grafas
def generate_graph():
    
    seed = randint(1,5000)
    Graph = nx.erdos_renyi_graph(20,0.2,seed)
    Graph.nodes
    return Graph
   
#  funkcija nupiesti galutini rezultata
def draw_final_result(Graph, bfs_path, dfs_path, ax, graph_title):
    pos = nx.shell_layout(Graph)

    common_nodes = set(bfs_path).intersection(set(dfs_path))
   
    nx.draw_networkx_nodes(Graph, pos, ax=ax, node_color='lightblue', node_size=400)
    nx.draw_networkx_edges(Graph, pos, ax=ax, edge_color='gray', width=1)
    nx.draw_networkx_labels(Graph, pos, ax=ax, font_size=10, font_weight="bold")

   
   
    # nubraizomas bfs kelias
    if bfs_path:
        bfs_edges = [(bfs_path[i], bfs_path[i + 1]) for i in range(len(bfs_path) - 1)]
        nx.draw_networkx_edges(Graph, pos, edgelist=bfs_edges, ax=ax, edge_color='blue', width=2)
        nx.draw_networkx_nodes(Graph, pos, nodelist=bfs_path, ax=ax, node_color='blue', node_size=600)

   # nubraizomas dfs kelias
    if dfs_path:
        dfs_edges = [(dfs_path[i], dfs_path[i + 1]) for i in range(len(dfs_path) - 1)]
        nx.draw_networkx_edges(Graph, pos, edgelist=dfs_edges, ax=ax, edge_color='green', width=2)
        nx.draw_networkx_nodes(Graph, pos, nodelist=dfs_path, ax=ax, node_color='green', node_size=600)
    # nubraizomi bendri kmazgai
    if common_nodes:
        nx.draw_networkx_nodes(Graph, pos, nodelist=common_nodes, ax=ax, node_color='orange', node_size=600)

    nx.draw_networkx_nodes(Graph, pos, nodelist=[0], ax=ax, node_color='lime', node_size=600)  # Start 
    target_node = bfs_path[-1] if bfs_path else dfs_path[-1]
    nx.draw_networkx_nodes(Graph, pos, nodelist=[19], ax=ax, node_color='red', node_size=600)  # End

    ax.set_title(graph_title, loc='left')


# BFs paieska
def bfs(graph, start,target):

    
    queue = deque([(start, [start])])
    
    
    visited = set([start])
    
    visited_count = 0

    while queue:
        
        node, path = queue.popleft()

        visited_count += 1
        
        if node == target:
            return path,visited_count
        
        
        for neighbor in graph.neighbors(node):
            if neighbor not in visited:
                
                visited.add(neighbor)  
                queue.append((neighbor, path + [neighbor]))  
    
    
    return None, visited_count
 # dfs paieka
def dfs(graph, start, target):
    
    stack = [(start, [start])]
    
    visited = set([start])
    
    visited_count = 0

    while stack:
       
        node, path = stack.pop()

        visited_count += 1
        
        if node == target:
            return path, visited_count
       
        for neighbor in graph.neighbors(node):
            if neighbor not in visited:
                visited.add(neighbor)  
                stack.append((neighbor, path + [neighbor]))  

    return None, visited_count
# Pagrindine funkcija
def main():
 
   fig, axs = plt.subplots(1, 3, figsize=(18, 8))

   bfs_paths = []
   dfs_paths = []
   dfs_counts = []
   bfs_counts = []
    # triju grafu generavimas ir rezultatai
   for i in range(3):

    graph = generate_graph()

    bfs_path , BFS_Results = bfs(graph,0,19)

    print("BFS Results")
    print(bfs_path,f"Count: {BFS_Results}") 

    dfs_path , DFS_Results = dfs(graph,0,19)

    print("DFS Results")
    print(dfs_path,f"Count: {DFS_Results}")
    # rezultatu saugojimas
    bfs_paths.append(bfs_path)
    dfs_paths.append(dfs_path)
    bfs_counts.append(BFS_Results)
    dfs_counts.append(DFS_Results)

    if bfs_path != None or dfs_path != None:
        draw_final_result(graph, bfs_path, dfs_path, ax=axs[i], graph_title=f"Graph {i+1}")
        
   legend_patches = [
        mpatches.Patch(color='blue', label='BFS Path'),
        mpatches.Patch(color='green', label='DFS Path'),
        mpatches.Patch(color='orange', label='Common Nodes'),
        mpatches.Patch(color='lime', label='Start Node'),
        mpatches.Patch(color='red', label='Target Node')
    ]

   fig.legend(handles=legend_patches, loc='upper center', bbox_to_anchor=(0.5, 1.0), ncol=5, fontsize='medium', title="Legend", framealpha=1)


   table_data = [
        ["Graph", "BFS Path", "DFS Path", "BFS Count", "DFS Count"],
        [f"Graph 1", f"{bfs_paths[0]}", f"{dfs_paths[0]}", f"{bfs_counts[0]}", f"{dfs_counts[0]}"],
        [f"Graph 2", f"{bfs_paths[1]}", f"{dfs_paths[1]}", f"{bfs_counts[1]}", f"{dfs_counts[1]}"],
        [f"Graph 3", f"{bfs_paths[2]}", f"{dfs_paths[2]}", f"{bfs_counts[2]}", f"{dfs_counts[2]}"]
    ]

   
   ax_table = fig.add_subplot(111, frame_on=False)
   ax_table.xaxis.set_visible(False)
   ax_table.yaxis.set_visible(False)
     
   table = ax_table.table(cellText=table_data, cellLoc='center', bbox=[0, -0.4, 1, 0.3]) 
    # lenteles vizualizacija
   table.auto_set_font_size(False)
   table.set_fontsize(10)
   table.scale(1.2, 1.2) 
   plt.subplots_adjust(top=0.85, bottom=0.25, hspace=0.3, wspace=0.4)
   plt.show()

       

if __name__ == "__main__":
    main()