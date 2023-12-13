from collections import deque
node=[]
graph=[]
nodecount=0
def addnode(v):
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
        print("Startnode",startnode)
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
def printgraph(graph):
    for i in range(nodecount):
        for j in range(nodecount):
            print(graph[i][j],end=" ")
        print()
addnode("a")
addnode("b")
addnode("c")
addedges("a","b")
addedges("b","c")
addedges("c","a")
visited=[False]*nodecount
dfs("a",visited)
visited=[False]*nodecount
bfs("c",visited)
s=shortpath("a","b")
print(s)
printgraph(graph)