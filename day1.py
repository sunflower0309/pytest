def hano(n,A,B,C):
    if n==1:
        print(n,A,'->',C)
    elif n>1:
        hano(n-1,A,C,B)
        print(n, A, '->', C)
        hano(n-1,B,A,C)

def trim(s):
    if len(s)==0:
        return s
    i=0
    isempty=0
    for i in range(len(s)):
        if(s[i]!=' '):
            s=s[i:]
            break
        if(i==len(s)-1):
            isempty=1
    if(isempty==1):
        return ''
    l=-1
    if len(s)==0:
        return s
    while 1:
        if(s[l]==' '):
            l=l-1
        else:
            break

    if l==-1:
        pass
    else :
        s=s[0:l+1]

    return s

def findMinAndMax(L):
    if L==[]:
        return(None,None)
    min=L[0]
    max=L[0]
    for i in L:
        if i>max:
            max=i
        if i<min:
            min=i
    return (min,max)

L1 = ['Hello', 'World', 18, 'Apple', None]
L2=[i.lower() for i in L1 if isinstance(i,str)==True]

def triangles():
    s=[1]
    yield s
    d=[1,1]
    yield d
    while 1:
        t=[1,1]
        for i in (range(len(d)-1)):
            t.insert(i+1,d[i]+d[i+1])
        yield t
        d=t
    return 'done'
k=triangles()
n=0
for t in triangles():
    print(t)

    n = n + 1
    if n == 10:
        break