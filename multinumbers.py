import graphviz
from rich import print

a = [ [ [], [], [ [] ] ] ]

print(a)

b = [[] for _ in range(4)]
print(b)

a.extend(b)

print(a)

dot = graphviz.Digraph('tree', format='png')
dot.edge('A', 'B')
dot.render('test.png')
dot.view()
