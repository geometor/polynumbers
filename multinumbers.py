import graphviz
from rich import print

a = [ [ [], [], [ [] ] ] ]

print(a)

b = [[] for _ in range(4)]
print(b)

nodes = a + b

print(nodes)

def graph_children(graph: graphviz.Digraph, parent_name: str, nodes: list):
    """connect parent node to list of child nodes

    :parent_name: str
    :nodes: list
    :returns: TODO

    """

    for i, node in enumerate(nodes):
        child_name = f'{parent_name}.{i}'
        graph.node(child_name, label=repr(node))
        graph.edge(parent_name, child_name)
        if node:
            graph_children(graph, child_name, node)


dot = graphviz.Digraph('multinumber', format='png')
dot.attr('graph', bgcolor='black')
dot.attr('node', fontcolor='white')
dot.attr('node', color='white')
#  dot.attr('node', shape='point')
dot.attr('node', shape='rest')
dot.attr('edge', color='#666666')
dot.attr('edge', arrowsize='1')

parent = '0'

dot.node(parent, label=repr(nodes),)
graph_children(dot, parent, nodes)

#  dot.view()
print(dot.source)

dot.render(view=True)
