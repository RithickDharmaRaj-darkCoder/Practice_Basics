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
        self.traversal()

    def traversal(self):
        if self.head is None:
            print('Linked List is Empty!\n--------------------')
        else:
            print('Head --> ', end=" ")
            n = self.head
            while n is not None:
                print(f'[{n.data}] --> ',end=" ")
                n = n.linkto
            print('None')
            print('--------------------')

    def add_at_starting(self,data):
        newnode = creatingnode(data)
        if self.head is None:
            self.head = newnode
        else:
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
            print('No Node in the Linked List!\n--------------------')
        else:
            while (n.data != x) and (n.linkto is not None):
                n = n.linkto
            else:
                if n.data == x:
                    newnode.linkto = n.linkto
                    n.linkto = newnode
                else:
                    print(f'{x} is not in the Linked List!\n--------------------')
        self.traversal()
    def add_before_node(self,data,x):
        n = self.head
        if n is None:
            print('No Node in the Linked List!\n--------------------')
        elif n.data == x:
            self.add_at_starting(data)
        else:
            while n.linkto is not None:
                if n.linkto.data == x:
                    self.add_after_node(data,n.data)
                    break
                else:
                    n = n.linkto
            if n.linkto is None:
                print(f'{x} is not in the Linked List!\n--------------------')

    def add_when_llEmpty(self,data):
        if self.head is None:
            self.add_at_starting(data)
        else:
            print("Linked List is not empty!\n--------------------'")


ll = linkedlist()
ll.add_when_llEmpty(40)
ll.add_at_starting(10)
ll.add_at_ending(50)
ll.add_when_llEmpty(100)
ll.add_after_node(20,10)
ll.add_before_node(30,40)
ll.add_after_node(60,50)
ll.add_before_node(70,80)