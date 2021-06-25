# Data Structure ...
# User-Defined ...
# Linked List ...
# Singly Linked List (Adding data @ Ending) ...

class creatingnode():
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
            n = self.head
            while n is not None:
                print(f'[ [{n.data}] | [{n.linkto}] ] ')
                n = n.linkto
            print('--------------------')

    def add_at_starting(self,data):
        newnode = creatingnode(data)
        newnode.linkto = self.head
        self.head = newnode

    def add_at_ending(self,data):
        newnode = creatingnode(data)
        if self.head is None:
            self.head = newnode
        else:
            n = self.head
            while n.linkto is not None:
                n = n.linkto
            n.linkto = newnode

ll = linkedlist()
ll.add_at_starting(10)
ll.add_at_ending(15)
ll.traversal()