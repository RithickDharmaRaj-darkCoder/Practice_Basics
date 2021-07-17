# Python Learning Field ...

class alrg:
    graph = {}

    def traversal(self):
        for i in self.graph:
            print(f'{i} = {self.graph.get(i)}')

    def add_node(self,v):
        if v in self.graph:
            print(f'{v} is already in graph!')
        else:
            self.graph[v] = []

    def add_edges(self,v1,v2,w):
        if v1 not in self.graph:
            print(f'{v1} is not in graph!')
        elif v2 not in self.graph:
            print(f'{v2} is not in graph!')
        else:
            lst1 = [v2,w]
            lst2 = [v1,w]
            if v2 not in self.graph[v1]:
                self.graph[v1].append(lst1)
            if v1 not in self.graph[v2]:
                self.graph[v2].append(lst2)

    def delete_node(self,v):
        if v not in self.graph:
            print(f'{v} is not in graph!')
        else:
            self.graph.pop(v)
            for keys in self.graph:
                for outer in range(len(self.graph[keys])):
                    if self.graph[keys][outer][0] == v:
                        self.graph[keys].pop(outer)


    def delete_edge(self,v1,v2):
        if v1 not in self.graph:
            print(f'{v1} is not in graph!')
        elif v2 not in self.graph:
            print(f'{v2} is not in graph!')
        else:
            #self.graph[v1].remove(v2)
            #self.graph[v2].remove(v1)
            for outer in range(len(self.graph[v1])):
                if self.graph[v1][outer][0] == v2:
                    del self.graph[v1][outer]
            for out in range(len(self.graph[v2])):
                try:
                    if self.graph[v2][out][0] == v1:
                        del self.graph[v2][out]
                except IndexError:
                    pass



gp = alrg()
# Adding Nodes ...
gp.add_node("A")
gp.add_node("B")
gp.add_node("C")
gp.add_node("D")
gp.add_node("E")

# Adding Edges ...
gp.add_edges("A","B",2)
gp.add_edges("A","C",3)
gp.add_edges("A","D",1)
gp.add_edges("B","D",1)
gp.add_edges("B","E",4)
gp.add_edges("C","D",1)
gp.add_edges("D","E",4)

# Deleting Nodes ...
gp.delete_node('E')

# Deleting Edge ...
gp.delete_edge('A','D')
gp.delete_edge('C','D')

gp.traversal()