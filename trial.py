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
        print('Head --> ',end=" ")
        if self.head is None:
            print('Linked List is Empty!')
        else:
            n = self.head
            while n is not None:
                print(f'[{n.data}] --> ',end=" ")
                n = n.linkto
            print('None')
            print('--------------------')

    def add_at_starting(self,data):
        newnode = creatingnode(data)
        newnode.linkto = self.head
        self.head = newnode
        self.traversal()
    def add_at_ending(self,data):
        newnode = creatingnode(data)
        if self.head is None:
            self.head = newnode
        else:
            n = self.head
            while n.linkto is not None:
                n = n.linkto
            n.linkto = newnode
        self.traversal()
    def add_after_node(self,data,x):
        newnode = creatingnode(data)
        n = self.head
        if self.head is None:
            print('No Node in the Linked List!')
        else:
            while (n.data != x) and (n.linkto is not None):
                n = n.linkto
            else:
                if n.data == x:
                    newnode.linkto = n.linkto
                    n.linkto = newnode
                else:
                    print(f'{x} is not in the Linked List!')
        self.traversal()




ll = linkedlist()
ll.add_at_starting(40)
ll.add_at_starting(20)
ll.add_at_starting(10)
ll.add_after_node(30,20)