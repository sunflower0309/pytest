#!usr/bin/python
import math
import time
import sys
import threading
import random
sys.setrecursionlimit(2000000)


class treenode(object):
    def __init__(self, item, lchild=None, rchild=None):
        self.item = item
        self.lchild = lchild
        self.rchild = rchild


class tree(object):
    def __init__(self, node=None):
        self.root = node
        self.treeQueue = []

    def add_node(self, item):
        # print("getin")
        node = treenode(item)
        if len(self.treeQueue) == 0:
            self.treeQueue.append(node)
            self.root = node
        else:
            cur = self.treeQueue[0]
            if cur.lchild == None:
                cur.lchild = node
                self.treeQueue.append(node)
            else:
                cur.rchild = node
                self.treeQueue.append(node)
                self.treeQueue.pop(0)

    def add_node_exchange(self, item):
        node = treenode(item)
        if len(self.treeQueue) == 0:
            self.treeQueue.append(node)
            self.root = node
        else:
            cur = self.treeQueue[0]
            if cur.lchild == None:
                node.item = cur.item  # 交换节点的值
                cur.item = item
                cur.lchild = node
                self.treeQueue.append(node)
            else:
                node.item = cur.item  # 交换节点的值
                cur.item = item
                cur.rchild = node
                self.treeQueue.append(node)
                self.treeQueue.pop(0)

    def front_travel(self, root1):
        # print("getin")
        if root1 == None:
            return
        print(root1.item)
        self.front_travel(root1.lchild)
        self.front_travel(root1.rchild)

    def middle_travel(self, root):
        if root == None:
            return
        self.middle_travel(root.lchild)
        print(root.item)
        self.middle_travel(root.rchild)

    def later_travel(self, root):
        if root == None:
            return
        self.later_travel(root.lchild)
        self.later_travel(root.rchild)
        print(root.item)

    def stack_front(self, root):
        stack1 = []
        node = root
        while len(stack1) != 0 or node != None:
            while node != None:
                print(node.item)
                stack1.append(node)
                node = node.lchild

            node = stack1.pop().rchild

    def stack_middle(self, root):
        stack1 = []
        node = root
        while len(stack1) != 0 or node != None:
            while node != None:
                stack1.append(node)
                node = node.lchild
            print(stack1[-1].item)
            node = stack1.pop().rchild

    def stack_later(self, root):
        stack1 = []
        stack2 = []
        node = root
        while len(stack1) != 0 or node != None:
            while node != None:
                stack2.append(node)
                stack1.append(node)
                node = node.rchild
            node = stack1.pop().lchild
        while stack2:
            print(stack2.pop().item)
def insertationsort(k):#将序列分为排序的和未排序的，每次从未排序的部分中选取第一个，找到位置进行插入

    for i in range(len(k)):
        for j in range(i,0,-1):
            if k[j]<k[j-1]:
                k[j],k[j-1]=k[j-1],k[j]


    return k

def selectionsort(x):#每次在未排序区间选择一个最小的，把最小的放在队头

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

def merge(li1,li2):#归并排序之并：依序从前到后比较两个序列中元素大小，然后按顺序添加进返回序列
    len2=len(li2)
    len1=len(li1)
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
    li=merge(l,r)

    return li




def quicksort(k):#将整个序列分成key的两侧，左侧始终比key小，右侧始终比key大，递归到左右大小为1
    if len(k)>=2:
        key = k[random.randint(0,len(k)-1)]
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



def quicksortfindmid(k,index):
    if k==[]:
        return
    else:
        key = k[0]
        left = []
        right = []
        for i in range(1, len(k)):
            if k[i] >= key:
                right.append(k[i])
            else:
                left.append(k[i])
        left.append(key)#因为是比较第几小，所以加到left里始终保证key是最大的，最不小的一个
        if len(left)==index:
            print(key)
            return key
        else:
            if index > len(left):#如果寻找的序列比左边大，就要去右边重新排名再找
                quicksortfindmid(right, index-len(left))
            elif index < len(left):#如果寻找的序列比左边小，就继续找
                quicksortfindmid(left, index)
# x=[1,4,10,5,6,9,8,3,12,54,67,98,345,2,7,13]
# y=[1,5,2,3,5,6,8,3,89,67,34,12,15,23]
# z=['sar','bs','swe','12','hg','strike']
# print(heapsort(z))

def heapify(arr, n, i):
    largest = i
    l = 2 * i + 1  # left = 2*i + 1
    r = 2 * i + 2  # right = 2*i + 2

    if l < n and arr[i] < arr[l]:
        largest = l

    if r < n and arr[largest] < arr[r]:
        largest = r

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # 交换

        heapify(arr, n, largest)


def heapSort(arr):#升序
    n = len(arr)

    # Build a maxheap.
    for i in range(n, -1, -1):
        heapify(arr, n, i)

        # 一个个交换元素
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # 交换
        heapify(arr, i, 0)
    return arr

wordlist=[]
lines=open('C:/Users/Administrator/Downloads/pride-and-prejudice.txt','r',encoding='utf-8-sig').readlines()
for i in lines:
    n=''
    for cha in i:
        if cha.isalnum():
            n=n+cha
        else:
            n=n+' '

    str=n.split()
    for words in str:
        wordlist.append(words)
        #print(len(wordlist))

wordlist2=wordlist.copy()
wordlist3=wordlist.copy()
# li_insertation=insertationsort(wordlist)#1200.596325461563
# li_selection=selectionsort(wordlist)#1002.4897632598877
# li_merge=mergesort(wordlist)#3.445197105407715 ok
# li_heap=heapSort(wordlist)#5.6120312213897705
# li_quick=quicksort(wordlist)
time1=time.time()
li_quick=quick_sort_standord(wordlist2,0,len(wordlist2)-1)
time2=time.time()
li_merge=mergesort(wordlist)#3.445197105407715
time3=time.time()
print(time2-time1,time3-time2)

print(li_merge==li_quick)
