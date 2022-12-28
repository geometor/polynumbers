"""
Multinumber structure development and analysis
"""
import graphviz
from rich import print

a = [ [ [], [], [ [] ], [] ] ]

b = [[] for _ in range(4)]

nodes = a + b + [[[]]]


def graph_children(graph: graphviz.Digraph, parent_name: str, nodes: list):
    """connect parent node to list of child nodes

    :parent_name: str
    :nodes: list
    :returns: None

    """

    for i, node in enumerate(nodes):
        child_name = f'{parent_name}.{i}'
        graph.node(child_name, label=repr(node))
        graph.edge(parent_name, child_name)
        if node:
            graph_children(graph, child_name, node)


def get_digraph(name: str) -> graphviz.Digraph:
    """return a configured digraph

    :name: TODO
    :returns: TODO

    """
    dot = graphviz.Digraph(name, format='png')
    #  dot.engine = 'sfdp'
    dot.attr('graph', bgcolor='black')
    dot.attr('node', fontcolor='white')
    dot.attr('node', color='white')
    #  dot.attr('node', shape='point')
    dot.attr('node', shape='rect')
    dot.attr('edge', color='#666666')
    dot.attr('edge', arrowsize='1')
    return dot


def main():
    """TODO: Docstring for main.

    :returns: TODO

    """
    dot = get_digraph('multinumber')

    parent = '0'
    dot.node(parent, label=repr(nodes),)
    graph_children(dot, parent, nodes)

    print(dot.source)

    dot.render(view=True)



if __name__ == "__main__":
    main()
