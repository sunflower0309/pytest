from DataStructure.SingleLinkedList import SingleLinkList
from DataStructure.SingleLinkedList import Node

class treenode(object):
    def __init__(self,item,lchild=None,rchild=None):
        self.item=item
        self.lchild=lchild
        self.rchild=rchild


class tree(object):
    def __init__(self,node=None):
        self.root=node
        self.treeQueue=SingleLinkList()
        self.treenodelist=SingleLinkList()

    def add_node(self,item):
        #print("getin")
        node=treenode(item)
        if self.treeQueue.length()==0:
            self.treeQueue.append1(node)
            self.treenodelist.append1(node)
            self.root=node
        else:
            cur=self.treeQueue.getindex(0)
            if cur.elem.lchild==None:
                cur.elem.lchild=node
                self.treeQueue.append1(node)
                self.treenodelist.append1(node)
            else:
                cur.elem.rchild=node
                self.treeQueue.append1(node)
                self.treenodelist.append1(node)
                self.treeQueue.pop()

    def search(self,input):
        for i in range(self.treenodelist.length()):
            if input==self.treenodelist.getindex(i).elem.item:
                return False
        return True

    def length(self):
        return self.treeQueue.length()
