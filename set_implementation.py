from DataStructure.SingleLinkedList import SingleLinkList
from DataStructure.BinaryTree import tree
from DataStructure.SingleLinkedList import Node
import re
import codecs
class imple_set_linkedlist(object):
    def __init__(self):
        self.linklist=SingleLinkList()

    def add(self,input):
        if self.linklist.search(input):
            return False
        else:
            self.linklist.append1(input)
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
        self.binarytree=tree()

    def add(self,input):
        if self.binarytree.search(input)==True:#找到了重复的是false
            self.binarytree.add_node(input)
        else:
            return False

    def contain(self,input):
        return self.binarytree.search(input)

    def size(self):
        return self.binarytree.length()


class HashTableSet(object):
    def __init__(self):
        self.linkedlist = SingleLinkList()
        self.count = 0

    def add(self, input):
        ha = hash(input)
        #print(input,ha)
        if self.linkedlist.searchindex(ha) == False:
            self.linkedlist.append1(input,ha)
        else:
            return

    def contain(self):
        ha = hash(input)
        return self.linkedlist.search(ha)

    def size(self):
        return self.linkedlist.length()


set_li=imple_set_linkedlist()
set_tree=imple_set_binarytree()
set_hash=HashTableSet()
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
        set_li.add(words)
        set_tree.add(words)
        #print(words)
        set_hash.add(words)
    #print(set_li.size())
print(set_li.size())#7105
lines1=open('C:/Users/Administrator/Downloads/words-shuffled.txt','r',encoding='utf-8-sig').readlines()
count=0
print(set_li.contain('Prejudice'))
for i in lines1:
    n = ''
    for cha in i:
        if cha=='\n' or cha=='\r':
            n = n + ''
        else:
            n=n+cha
    if set_li.contain(n)==True:
        count+=1
    print(count)
print(count)
#print(set_tree.size())