# Data Structure ...
# User-Defined ...
# Linked List ...
# Singly Linked List (Traversal Working !!!) ...

class node():
    def __init__(self,data):
        self.data = data
        self.linkto = None

class linkedlist():
    def __init__(self):
        self.head = None

    def traversal(self):
        if self.head is None:
            print('Linked List is Empty!')
        else:
            node = self.head
            while node is not None:
                print(node.data)
                node = node.linkto

node1 = linkedlist()
node1.traversal()
