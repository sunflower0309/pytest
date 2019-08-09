import math

x=[1,3,5,7,2,3,6,11,23,345]
leng=len(x)
for i in range(leng):
    count=0
    for j in range(count,leng):
        if x[i]>x[j]:
            k=x[i]
            x[i]=x[j]
            x[j]=k
    count=count+1


y=[1,3,2,5,7,2,3,6,11,23,8,345]
k=[5,8,5,2,9]
def choosesort(x):#每次在未排序区间选择一个最小的，把最小的放在队头
    leng=len(x)
    for i in range(leng):
        min = x[i]
        num = i
        for j in range(i,leng):
            if x[j]<x[i]:
                min=x[j]
                num=j
        x[num]=x[i]
        x[i]=min
    return x
#print(choosesort(k))

def insertsort(k):#将序列分为排序的和未排序的，每次从未排序的部分中选取第一个，找到位置进行插入
    for i in range(len(k)):
        for j in range(i,0,-1):
            if k[j]<k[j-1]:
                k[j],k[j-1]=k[j-1],k[j]
    return k
#print(insertsort(y))

def quicksort(k):#将整个序列分成key的两侧，左侧始终比key小，右侧始终比key大，递归到左右大小为1

    if len(k)>=2:
        key = k[0]
        left = []
        right = []
        for i in range(1, len(k)):
            if k[i] > key:
                right.append(k[i])
            else:
                left.append(k[i])

        return quicksort(left) + [key] + quicksort(right)
    else:
        return k

#print(quicksort(y))

def shellsort(k):#选择增量，逐个进行插入排序
    leng=len(k)
    step=math.floor(leng/2)
    temp=k
    while step!=0:
        print(step)
        sli=[]
        for i in range(step):
            sli.append(temp[i::step])
        temp=[]
        for i in sli:
            i=insertsort(i)
            temp=temp+i
        step = math.floor(step / 2)
    return temp

#print(shellsort(y))
li1=[2,4,6,7]
li2=[1,2,3,5]
def merge(li1,li2):#归并排序之并：依序从前到后比较两个序列中元素大小，然后按顺序添加进返回序列
    len2=len(li2)
    li=[]
    l=0
    r=0
    while True:
        if l==len1:
            li=li+li2
            break
        elif r==len2:
            li=li+li1
            break
        else:
            if li1[0]<=li2[0]:
                li.append(li1[0])
                li1.pop(0)
                l=l+1
            else:
                li.append(li2[0])
                li2.pop(0)
                r = r + 1
    return li
#print(merge(li1,li2))

def mergesort(k):#归并排序之归：无限分解初始序列，直到长度为1以下，然后进行并操作，l和r始终返回一个序列
    if len(k)<=1:
        return k
    mid=math.floor(len(k)/2)
    l=mergesort(k[:mid])
    r=mergesort(k[mid:])
    return merge(l,r)
print(mergesort(y))