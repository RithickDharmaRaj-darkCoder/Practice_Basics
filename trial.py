# Data Structure ...
# User-Defined ...
# Linked List ...
# Singly Linked List (Adding data @ begining) ...

class creatingnode():
    def __init__(self,data):
        self.data = data
        self.linkto = None

class linkedlist():
    def __init__(self):
        self.head = None

    def traversal(self):
        if self.head is None:
            print(f'[ Head --]--> {self.head}')
            print('Linked List is Empty!')
        else:
            n = self.head
            while n is not None:
                print(f'[ [{n.data}] | [{n.linkto}] ] ')
                n = n.linkto

    def add_at_starting(self,data):
        newnode = creatingnode(data)
        newnode.linkto = self.head
        self.head = newnode
        print(f'[ Head --]--> {self.head}')

ll = linkedlist()
ll.add_at_starting(50)
ll.traversal()
ll.add_at_starting(30)
ll.traversal()
