from collections import deque
node=[]
graph=[]
nodecount=0
def addnode(v):
    global nodecount
    if v in node:
        print("already present")
    else:
        nodecount+=1
        node.append(v)
        for row in graph:
            row.append(0)
        tem=[]
        for i in range(nodecount):
            tem.append(0)
        graph.append(tem)
def addedge(v1,v2):
    if v1 not in node:
        print("alreay present")
    elif v2  not in node:
        print("already present")
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
        x=node.remove(v)
        for row in graph:
            row.pop(x)
        graph.pop(x)
def removeedge(v1,v2):
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
        print("none")
        return
    print("vistednode",startnode)
    visited[node.index(startnode)]=True
    for i in range(nodecount):
        if graph[node.index(startnode)][i]==1 and not visited[i]:
            dfs(node[i],visited)
def bfs(startnode,visited):
    if startnode not in node:
        print("none")
        return
    que=deque([startnode])
    visited[node.index(startnode)]=True
    while que:
        currentnode=que.popleft()
        print("startnode",currentnode)
        for i in range(nodecount):
            if graph[node.index(currentnode)][i]==1 and not visited[i]:
                que.append(node[i])
                visited[i]=True
    
def printnode(graph):
    global nodecount
    for i in  range(nodecount):
        for j in range(nodecount):
            print(graph[i][j],end="")
        print()
addnode("a")
addnode("b")
addnode("c")

addedge("a","b")
addedge("b","c")
printnode(graph)
print("dfs traversal")
visited=[False]*nodecount
dfs("a",visited)
print("bfs")
visited=[False]*nodecount
bfs("a",visited)