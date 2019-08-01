class treenode(object):
    def __init__(self,item,lchild=None,rchild=None):
        self.item=item
        self.lchild=lchild
        self.rchild=rchild


class tree(object):
    def __init__(self,node=None):
        self.root=node
        self.treeQueue=[]

    def addnode(self,item):
        node=treenode(item)
        if len(self.treeQueue)==0:
            self.treeQueue.append(node)
            self.root=node
        else:
            cur=self.treeQueue[0]
            if cur.lchild==None:
                cur.lchild=node
                self.treeQueue.append(node)
            else:
                cur.rchild=node
                self.treeQueue.append(node)
                self.treeQueue.pop(0)

    def front_travel(self,node):
        if()
