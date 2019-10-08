from DataStructure.SingleLinkedList import SingleLinkList
from DataStructure.BinarySearchTree import bst
import matplotlib.pyplot as plt
import numpy as np
import time
class imple_set_linkedlist(object):
    def __init__(self):
        self.linklist=SingleLinkList()
        self.timestart=time.time()
        self.timelist=[]

    def add(self,input):
        if self.linklist.search(input):
            return False
        else:
            self.linklist.append1(input)
            timeadd=time.time()
            self.timelist.append(timeadd-self.timestart)
            return True


    def contain(self,input):
        if self.linklist.search(input)==True:
            return self.linklist.search(input)
        else:
            return False

    def size(self):
        return self.linklist.length()

class imple_set_binarytree(object):
    def __init__(self):
        self.bst=bst()
        self.timestart = time.time()
        self.timelist = []

    def add(self,input):
        if self.search(input)==False:
            self.bst.insert(input,self.bst.root)
            timeadd = time.time()
            self.timelist.append(timeadd - self.timestart)
        else:
            return

    def search(self,input):
        return self.bst.search(input,self.bst.root)
    def size(self):
        return self.bst.count


class HashTableSet(object):
    def __init__(self):
        self.list=[]
        self.count = 0
        self.timestart = time.time()
        self.timelist = []
        for i in range(8011):
            self.list.append(SingleLinkList())

    def add(self, input):
        ha = hash(input)%13
        if self.list[ha].search(input):
            return
        else:
            self.list[ha].append1(input)
            timeadd = time.time()
            self.timelist.append(timeadd - self.timestart)

    def contain(self,input):
        ha = hash(input)%13
        return self.list[ha].search(input)

    def size(self):
        count=0
        for i in range(len(self.list)):
            count+=self.list[i].length()
        return count



lines=open('C:/Users/Administrator/Downloads/pride-and-prejudice.txt','r',encoding='utf-8-sig').readlines()
str=[]
for i in lines:
    n=''
    for cha in i:
        if cha.isalnum():
            n=n+cha
        else:
            n=n+' '

    str=str+n.split()

set_li=imple_set_linkedlist()
set_tree=imple_set_binarytree()
set_hash=HashTableSet()
for words in str:
    set_li.add(words)
for words in str:
    set_hash.add(words)
for words in str:
    set_tree.add(words)
x=np.linspace(0,set_li.size(),set_li.size())#X轴数据
y1=set_li.timelist
y2=[i-y1[-1] for i in set_hash.timelist]
y3=[i-y2[-1]-y1[-1] for i in set_tree.timelist]
plt.plot(x,y1,label='linkedlist',color='black')
plt.plot(x,y2,label='hashtable',color='blue')
plt.plot(x,y3,label='binarytree',color='red')
plt.legend()
plt.show()



#print(set_li.size())#7105
lines1=open('C:/Users/Administrator/Downloads/words-shuffled.txt','r',encoding='utf-8-sig').readlines()
count=0
print(len(lines1))
for i in lines1:
    n = ''
    for cha in i:
        if cha=='\n' or cha=='\r':
            n = n + ''
        else:
            n=n+cha
    if set_li.contain(n)==True:
        count+=1
    #print(count)
print(count)
