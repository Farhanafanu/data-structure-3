from collections import deque
node = []
graph = []
nodecount = 0

def addvalue(v):
    global nodecount
    if v in node:
        print("already present")
    else:
        nodecount += 1
        node.append(v)
        for row in graph:
            row.append(0)
        tem = []
        for i in range(nodecount):
            tem.append(0)
        graph.append(tem)

def addedges(v1, v2):
    if v1 not in node:
        print("not present")
    elif v2 not in node:
        print("not present")
    else:
        x = node.index(v1)
        y = node.index(v2)
        graph[x][y] = 1
        graph[y][x] = 1

def removenode(v):
    global nodecount
    if v not in node:
        print("not present")
    else:
        x = node.index(v)
        node.remove(v)
        nodecount -= 1
        graph.pop(x)
        for row in graph:
            row.pop(x)

def remoevedge(v1, v2):
    if v1 not in node:
        print("not present")
    elif v2 not in node:
        print("not present")
    else:
        x = node.index(v1)
        y = node.index(v2)
        graph[x][y] = 0
        graph[y][x] = 0

def dfs(startnode, visited):
    if startnode not in node:
        print("empty")
        return
    print("Visiting node:", startnode)
    visited[node.index(startnode)] = True
    for i in range(nodecount):
        if graph[node.index(startnode)][i] == 1 and not visited[i]:
            dfs(node[i], visited)
def shortpath(start,end):
    visited=[False]*nodecount
    que=deque()
    que.append((start,0,[start]))

    while que:
        currentnode,dist,path=que.popleft()
        if currentnode==end:
            return dist,path
        visited[node.index(currentnode)]=1
        for i in range(nodecount):
            if graph[node.index(currentnode)][i]==1 and not visited[i]:
                que.append((node[i],dist+1,path+[node[i]]))
        
def bfs(startnode, visited):
    if startnode not in node:
        print("empty")
        return
    
    queue = deque([startnode])
    visited[node.index(startnode)] = True

    while queue:
        currentnode = queue.popleft()
        print("Visiting node:", currentnode)

        for i in range(nodecount):
            if graph[node.index(currentnode)][i] == 1 and not visited[i]:
                queue.append(node[i])
                visited[i] = True

def printgraph(graph):
    for i in range(nodecount):
        for j in range(nodecount):
            print(graph[i][j], end="")
        print()

addvalue("a")
addvalue("b")
addvalue("c")
addedges("a", "b")
addedges("b", "c")
addedges("a", "c")
# removenode("c")
remoevedge("a", "b")
printgraph(graph)
print("DFS Traversal:")
visited = [False] * nodecount
dfs("a", visited)
# Example usage:
visited = [False] * nodecount
print("BFS Traversal:")
bfs("a", visited)
s=shortpath("a","b")
print("shortpath",s)
