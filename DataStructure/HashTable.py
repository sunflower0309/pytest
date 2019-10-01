from DataStructure.SingleLinkedList import SingleLinkList
from DataStructure.SingleLinkedList import Node

class HashTableSet(object):
    def __init__(self):
        self.linkedlist=SingleLinkList()
        self.count=0

    def add(self,input):
        ha=hash(input)
        if self.linkedlist.search(ha)==False:
            self.linkedlist.append1(Node(SingleLinkList(Node(input)),ha))
        else:
            return

    def contain(self):
        ha=hash(input())
        return self.linkedlist.search(ha)

    def size(self):
        return self.linkedlist.length()