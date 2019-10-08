N=[[1,3,8],[0,2,3,4],[1,4,5],[0,1,4,6],[1,2,3,5,6,7],[2,4,7],[3,4,7,8,9],[4,5,6,9],[0,6,9],[6,7,8]]#testdata

def dfsvisit(N,ver,visited,li):

    for i in N[ver]:
        if visited[i]!=1:
            visited[i]=1
            li.append(i)
            dfsvisit(N,i,visited,li)
    return

def dfs(N,ver):
    li=[]
    visited=[0]*len(N)
    visited[ver]=1
    li.append(ver)
    dfsvisit(N,ver,visited,li)
    return li
print("dfs:",dfs(N,0))

def bfsvisit(N,ver,visited,visitqueue,li):
    visitqueue.pop(0)
    for i in N[ver]:
        if visited[i]!=1:
            visited[i] = 1
            visitqueue.append(i)
            li.append(i)
    if len(visitqueue)!=0:
        next = visitqueue[0]
        bfsvisit(N, next, visited, visitqueue,li)
    else:
        return


def bfs(N,ver):
    li=[]
    visited = [0] * len(N)
    visitqueue=[]
    visited[ver] = 1
    visitqueue.append(ver)
    li.append(ver)
    bfsvisit(N,ver,visited,visitqueue,li)
    return li
print("bfs:",bfs(N,0))
