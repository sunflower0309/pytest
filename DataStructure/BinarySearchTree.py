class treenode(object):
    def __init__(self,item,lchild=None,rchild=None):
        self.item=item
        self.lchild=lchild
        self.rchild=rchild


class bst(object):
    def __init__(self,treenode=None):
        self.root=treenode
        self.count=0

    def insert(self, input,root=None,):
        if root==None:
            if self.root==None:
                self.count += 1
                self.root = treenode(input)
            else:
                self.count += 1
                root = treenode(input)
        elif input < root.item:
            root.lchild = self.insert(input,root.lchild)
        elif input >root.item:
            root.rchild = self.insert(input,root.rchild)
        return root

    def search(self,input,root=None):

        if root==None:
            return False
        if root.item==input:
            return True
        elif input < root.item:
            return self.search(input,root.lchild)
        elif input > root.item:
            return self.search(input,root.rchild)

    def size(self):
        return self.count

    def front_travel(self,root1):
        #print("getin")
        if root1==None:
            return

        self.front_travel(root1.lchild)
        self.front_travel(root1.rchild)