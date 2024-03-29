import sys

class Node(object):
    """定义节点"""

    def __init__(self, elem,index=None):
        self.elem = elem
        self.index=index
        self.next = None

    def get_elem(self):
        return self.elem

class SingleLinkList(object):
    """单链表操作"""

    def __init__(self, node=None):
        """初始化"""
        self.__head = node

    def is_empty(self):
        """链表是否为空"""
        return self.__head == None

    def length(self):
        """链表长度"""
        # 定义游标，用来移动遍历节点
        cur = self.__head
        # 定义计数
        count = 0
        while cur != None:
            count += 1
            cur = cur.next
        return count

    def travel(self):
        """遍历整个链表"""
        cur = self.__head
        while cur != None:
            print(cur.elem, end=" ")
            cur = cur.next
        print("")

    def add(self, item):
        """链表头部添加元素，头插法"""
        node = Node(item)
        node.next = self.__head
        self.__head = node

    def append1(self, item,index=None):
        """链表尾部添加元素,尾插法"""
        node = Node(item,index)
        # if self.__head == None:
        if self.is_empty():
            self.__head = node
            return
        else:
            cur = self.__head
            while cur.next != None:
                cur = cur.next
            cur.next = node

    def insert(self, pos, item):
        """指定位置添加元素
        pos 从0开始
        """
        if pos < 0:
            # 输入值小于0，默认为头插法
            return self.add(item)
        elif pos > self.length() - 1:
            # 输入值大于列表长度，默认为尾插法
            self.append1(item)
        else:
            node = Node(item)
            cur = self.__head
            count = 0
            while count < (pos - 1):
                count += 1
                cur = cur.next
            # 当循环退出时，cur指向pos-1的位置
            node.next = cur.next
            cur.next = node

    def remove(self, item):
        """删除节点,只删除第一个找到的数据"""
        cur = self.__head
        pre = None
        while cur != None:
            if cur.elem == item:
                # 先判断此节点是否是头节点
                # if pre == None:
                if cur == self.__head:
                    self.__head = cur.next
                # 删除节点
                else:
                    pre.next = cur.next
                break
            else:
                pre = cur
                cur = cur.next
        return

    def search(self, item):#找到了是true

        cur = self.__head
        while cur != None:
            if cur.elem == item:
                return True
            else:
                cur = cur.next

        return False

    def searchindex(self, item):
        count=0
        cur = self.__head
        while cur != None:
            if cur.index == item:
                return True
            else:
                cur = cur.next
                count+=1
        return False


    def last(self):
        cur = self.__head

        if cur != None:
            while cur.next != None:
                cur = cur.next
            print("inlast")
            print(cur.get_elem())

            return cur
        else:
            print("Empty")

    def insertnew(self, item, pos):
        node = Node(item)

        cur = self.__head
        if cur == None:
            self.__head = node
        elif pos < 0:
            node.next = cur
            self.__head = node
        elif pos > self.length() - 1:
            cur = self.last()
            cur.next = node
        else:
            count = 0
            while count < pos:
                cur = cur.next
            node.next = cur.next
            cur.next = node

    def reverse(self):
        list=[]
        prev=self.__head
        cur=prev.next
        next=cur.next
        prev.next=None
        while next.next!=None:
            cur.next=prev
            prev=cur
            cur=next
            next=next.next
        next.next=cur
        cur.next=prev
        self.__head=next
        return self

    def find_middle(self):
        cur=self.__head
        count=1
        while cur.next:
            cur=cur.next
            count+=1
        cur=self.__head
        if count%2==1:
            index=(count+1)/2
            for i in range(1,int(index)):
                cur=cur.next
            print("middle node")
            print(cur.elem)
        else:
            index=count/2
            for i in range(1,int(index)):
                cur=cur.next
            print("middle node")
            print(cur.elem,cur.next.elem)

    def pop(self):
        cur=self.__head
        self.__head=self.__head.next
        cur.next=None

    def getindex(self,index):
        cur=self.__head
        for i in range(0,index):
            cur=cur.next
        return cur

# linkedlist=SingleLinkList(Node(1))
# for i in range(2,11):
#     linkedlist.append1(i)



