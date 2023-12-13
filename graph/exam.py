from collections import deque
node=[]
graph=[]
nodecount=0
def addvalue(v):
    global nodecount
    if v in node:
        print("already")
    else:
        nodecount+=1
        node.append(v)
        tem=[]
        for i in range(nodecount):
            tem.append(0)
        graph.append(tem)
        for row in graph:
            row.append(0)
def addedges(v1,v2):
    if v1 not in node:
        print("empty")
    elif v2 not in node:
        print("empty")
    else:
        x=node.index(v1)
        y=node.index(v2)
        graph[x][y]=1
        graph[y][x]=1
def removenode(v):
    global nodecount
    if v not in node:
        print("empty")
    else:
        nodecount-=1
        x=node.index(v)
        node.remove(v)
        graph.pop(x)
        for row in graph:
            row.pop(x)
def removeedges(v1,v2):
    if v1 not in node:
        print("empty")
    elif v2 not in node:
        print("empty")
    else:
        x=node.index(v1)
        y=node.index(v2)
        graph[x][y]=0
        graph[y][x]=0
def dfs(startnode,visited):
    if startnode not in node:
        print("empty")
    else:
        print("startnode",startnode)
        visited[node.index(startnode)]=True
        for i in range(nodecount):
            if graph[node.index(startnode)][i]==1 and not visited[i]:
                dfs(node[i],visited)
def bfs(startnode,visited):
    if startnode not in node:
        print("empty")
    else:
        que=deque([startnode])
        visited[node.index(startnode)]=True
        while que:
            currentnode=que.popleft()
            print("startnode",currentnode)
            for i in range(nodecount):
                if graph[node.index(currentnode)][i]==1 and not visited[i]:
                    que.append(node[i])
                    visited[i]=True
def shortest_path(start, end):
    visited = [False]* nodecount
    queue = deque()
    queue.append((start, 0, [start]))
   
    while queue:
        current_node, dist, path = queue.popleft()
       
        if current_node == end:
            return dist, path
        visited[node.index(current_node)] = 1
       
        for i in range(nodecount):
            if graph[node.index(current_node)][i] == 1 and not visited[i]:
                queue.append((node[i], dist+1, path+ [node[i]]))
               
    print("No ptah")
    return None

def printgraph(graph):
    for i in range(nodecount):
        for j in range(nodecount):
            print(graph[i][j],end=" ")
        print()
addvalue("a")
addvalue("b")
addvalue("c")
addedges("a","b")
addedges("b","c")
addedges("a","c")
visited=[False]*nodecount
dfs("a",visited)
visited=[False]*nodecount
bfs("c",visited)
printgraph(graph)
print("\nShortest Path:")
shortest_path_nodes = shortest_path("a", "c")
print(shortest_path_nodes)
