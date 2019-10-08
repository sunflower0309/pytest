class treenode(object):
    def __init__(self,item,lchild=None,rchild=None):
        self.item=item
        self.lchild=lchild
        self.rchild=rchild


class tree(object):
    def __init__(self,node=None):
        self.root=node
        self.treeQueue=[]

    def add_node(self,item):
        #print("getin")
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


    def add_node_exchange(self,item):
        node = treenode(item)
        if len(self.treeQueue) == 0:
            self.treeQueue.append(node)
            self.root = node
        else:
            cur = self.treeQueue[0]
            if cur.lchild == None:
                node.item=cur.item#交换节点的值
                cur.item=item
                cur.lchild = node
                self.treeQueue.append(node)
            else:
                node.item = cur.item  # 交换节点的值
                cur.item = item
                cur.rchild = node
                self.treeQueue.append(node)
                self.treeQueue.pop(0)


    def front_travel(self,root1):
        #print("getin")
        if root1==None:
            return
        print(root1.item)
        self.front_travel(root1.lchild)
        self.front_travel(root1.rchild)

    def middle_travel(self,root):
        if root==None:
            return
        self.middle_travel(root.lchild)
        print(root.item)
        self.middle_travel(root.rchild)

    def later_travel(self,root):
        if root==None:
            return
        self.later_travel(root.lchild)
        self.later_travel(root.rchild)
        print(root.item)

    def stack_front(self,root):
        stack1=[]
        node=root
        while len(stack1)!=0 or node!=None:
            while node!=None:
                print(node.item)
                stack1.append(node)
                node=node.lchild

            node=stack1.pop().rchild

    def stack_middle(self,root):
        stack1 = []
        node = root
        while len(stack1) != 0 or node != None:
            while node != None:
                stack1.append(node)
                node = node.lchild
            print(stack1[-1].item)
            node = stack1.pop().rchild

    def stack_later(self,root):
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

elems=range(10)
treetest=tree()
for elem in elems:
    treetest.add_node(elem)

treetest.front_travel(treetest.root)
treetest.stack_middle(treetest.root)
treetest.stack_later(treetest.root)
