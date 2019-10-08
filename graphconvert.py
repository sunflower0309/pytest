#test data
N = [[0, 1, 1, 1, 1, 1, 0, 0],
     [1, 0, 1, 0, 1, 0, 0, 0],
     [1, 1, 0, 1, 0, 0, 0, 0],
     [1, 0, 1, 0, 1, 0, 0, 0],
     [1, 1, 0, 1, 0, 1, 0, 0],
     [1, 0, 0, 0, 1, 0, 1, 1],
     [0, 0, 0, 0, 0, 1, 0, 1],
     [0, 0, 0, 0, 0, 1, 1, 0]]

def matrixtolist(N):
    list=[]
    for i in range(len(N)):
        x=set([])
        for j in range(0,len(N)):
            if N[i][j]==1:
                x.add(j)
        list.append(x)
    return list
#time complexity is O(n^2)
#print(matrixtolist(N))

def adjtoinci(N):
    edge=[]
    mat=[]
    for i in range(len(N)):
        p1=str(i)
        for j in range(len(N[i])):
            p2=str(list(N[i])[j])
            if p1+p2 not in edge and p2+p1 not in edge:
                edge.append(p1+p2)
    for i in range(len(edge)):
        row=[0]*len(N)
        x1=int(edge[i][0])
        x2=int(edge[i][1])
        row[x1]=1
        row[x2]=1
        mat.append(row)
    return mat
#time complexity is O(n^2)
#print(adjtoinci(matrixtolist(N)))

def incitoadj(N):
    numofver=len(N[0])
    mat=[]
    for i in range(numofver):
        mat.append([0]*numofver)
    edge=[]
    for i in range(len(N)):
        ed=''
        for j in range(len(N[i])):
            if N[i][j]==1:
                ed+=str(j)
        edge.append(ed)
    for i in edge:
        x1=int(i[0])
        x2=int(i[1])
        mat[x1][x2]=1
        mat[x2][x1]=1
    return mat
#time complexity is O(n^2)
#print(incitoadj(adjtoinci(matrixtolist(N)))==N)
