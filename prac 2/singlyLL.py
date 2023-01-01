#PERFORM CREATION,INSERTION & DELETION OPERATIONS IN SINGLY LINK LIST 
#creating a singly link list
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

