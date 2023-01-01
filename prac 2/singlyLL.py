#PERFORM CREATION,INSERTION & DELETION OPERATIONS IN SINGLY LINK LIST 
#creating a singly link list
import structlinks
from structlinks import LinkedList
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class LL:
    def __init__(self):
        self.haed= None

#Insertion at front 
def push(self, new_data):
    new_node= Node(new_data)
    new_node.next=self.head
    self.head =new_node

#Insertion after a given node

def insert(self, prev_node, new_data):
    if prev_node is None:
        print("The given node must in LL ")
        return
    new_node = Node(new_data)
    new_node.next = prev_node.next
    prev_node.next = new_node

# Deletion with example 

def delete(self,key):
    T = self.head
    if (T is not None):
        if (T.data == key):
            self.head = T.next
            T = None 
            return
    
    while( T is not None):
        if T.data == key:
            break
        prev = T
        T = T.next
    
    if (T == None):
        return
    prev.next = T.next
    T = None

    def printL(self):
        T = self.head
        while(T):
            print("%d"%(T.data))
            T = T.next

Llist = Linkedlist()
Llist.push(7)
Llist.push(8)
Llist.push(9)
Llist.push(1)
print("Created LL: ")
Llist.printList()
Llist.deleteNode(1)
print("\n Link list after Deletion:")
Llist.print
