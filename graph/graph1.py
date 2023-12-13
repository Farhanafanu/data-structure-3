from collections import deque

def add_node(v):
    global node_count
    if v in node:
        print(v, "Already available")
    else:
        node_count += 1
        node.append(v)
        for row in graph:
            row.append(0)
        tem = []
        for i in range(node_count):
            tem.append(0)
        graph.append(tem)


def add_edge(v1, v2):
    if v1 not in node:
        print("Node", v1, "not available")
    elif v2 not in node:
        print("Node", v2, "not available")
    else:
        x = node.index(v1)
        y = node.index(v2)
        graph[x][y] = 1
        graph[y][x] = 1


def print_node(graph):
    global node_count
    for i in range(node_count):
        for j in range(node_count):
            print(graph[i][j], end=" ")
        print()


# def delete_node(v):
#     global node_count
#     if v not in node:
#         print("Node", v, "not found")
#     else:
#         x = node.index(v)
#         node_count -= 1
#         node.remove(v)
#         graph.pop(x)
#         for row in graph: 
#             row.pop(x)


# def delete_edge(v1, v2):
#     if v1 not in node:
#         print("Node", v1, "not found")
#     elif v2 not in node:
#         print("Node", v2, "not found")
#     else:
#         x = node.index(v1)
#         y = node.index(v2)
#         graph[x][y] = 0
#         graph[y][x] = 0


# def DFS(start_node, visited):
#     if start_node  not in node:
#         print("np")
#         return
#     visited[node.index(start_node)] = True
   
#     print(start_node, end=" ")
   
#     for i in range(node_count):
#         if graph[node.index(start_node)][i] ==1 and not visited[i]:
#             DFS(node[i], visited)
           
# def BFS(start_node, visited):
#     if start_node not in node:
#         print("No")
#         return
#     queue = deque()
#     queue.append(start_node)
   
#     while queue:
#         current = queue.popleft()
#         print(current, end=" ")
#         visited[node.index(current)]  = True
       
#         for i in range(node_count):
#             if graph[node.index(current)][i] == 1 and not visited[i]:
#                 queue.append(node[i])
#                 visited[i] = 1
               
# def shortest_path(start, end):
#     visited = [False]* node_count
#     queue = deque()
#     queue.append((start, 0, [start]))
   
#     while queue:
#         current_node, dist, path = queue.popleft()
       
#         if current_node == end:
#             return dist, path
#         visited[node.index(current_node)] = 1
       
#         for i in range(node_count):
#             if graph[node.index(current_node)][i] == 1 and not visited[i]:
#                 queue.append((node[i], dist+1, path+ [node[i]]))
               
#     print("No ptah")
#     return None

# def any_connection(start, end, visited = None):
#     if visited is None:
#         visited =  [False]*node_count
#     visited[node.index(start)] = True
   
#     if start ==end:
#         return True
#     for i in range(node_count):
#         if graph[node.index(start)][i] == 1 and not visited[i]:
#             if any_connection(node[i], end, visited):
#                 return True
#     return False
           
   
       


visited = []
node = []
graph = []
node_count = 0

add_node("A")
add_node("A")
add_node("B")
add_node("C")
add_node("D")
add_node("F")
add_edge("A", "B")
add_edge("B", "C")
add_edge("C", "D")
add_edge("D", "F")
print_node(graph)

# delete_node("C")
# delete_edge("A", "B")
# print("DFS Traversal:")
# visited = [False]* node_count
# DFS("A", visited)

# print("\nBFS Traversal:")
# visited = [False] * node_count
# BFS("A", visited)

# print("\nShortest Path:")
# shortest_path_nodes = shortest_path("A", "F")
# print(shortest_path_nodes)


# if any_connection( "A", "D"):
#     print("Yes")
# else:
#     print("NO")

