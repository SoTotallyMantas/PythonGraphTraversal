from random import randint
import networkx as nx
import matplotlib.pyplot as plt
import collections
from collections import deque
def generate_graph():
    
    seed = randint(1,5000)
    Graph = nx.erdos_renyi_graph(20,0.2,seed)
    # print("Nodes", Graph.nodes(data=True))
    # print("Edges", Graph.edges(data=True))
    Graph.nodes
    return Graph
   

def draw_final_result(Graph):

    plt.subplots(figsize=(12, 9))
    pos = nx.spring_layout(Graph,seed=225)
    nx.draw_networkx_nodes(Graph, pos, node_color='lightblue', node_size=600)
    nx.draw_networkx_edges(Graph, pos, edge_color='gray', width=1)
    nx.draw_networkx_labels(Graph, pos, font_size=10, font_weight="bold")
    nx.draw_networkx_nodes(Graph, pos, nodelist=[0], node_color='lime', node_size=800)
    nx.draw_networkx_nodes(Graph, pos, nodelist=[19], node_color='red', node_size=800)
    plt.show()

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

def main():
   graph= generate_graph()
  # draw_final_result(graph)
   BFS_Results = bfs(graph,0,19)
   
   DFS_Results = dfs(graph,0,17)
   graph= generate_graph()
   
   BFS_Results += bfs(graph,0,13)
   
   DFS_Results += dfs(graph,0,17)
   graph= generate_graph()
   
   BFS_Results += bfs(graph,0,17)
   
   DFS_Results += dfs(graph,0,17)
   print("BFS Results")
   for BFSResult in BFS_Results:
       
       print(BFSResult)
       
   print("DFS Results")
   for DFSResult in DFS_Results:
       
       print(DFSResult)
       

if __name__ == "__main__":
    main()