from pprint import pprint
from collections import OrderedDict


class Node:
    pass

class InternalNode(Node):
    def __init__(self, type, children):
        self.type = type
        self.children = children
        for i in range(len(self.children)):
            if not isinstance(self.children[i], Node):
                self.children[i] = ExternalNode(str(self.children[i]), str(self.children[i]))
        ast = traverse(self)
        #print('--------------------------------------------------------------')
        #print(ast)
        #print('--------------------------------------------------------------')

    
class ExternalNode(Node):
    def __init__(self, type, value):
        self.type = type
        self.value = value
        #print('--------------------------------------------------------------')
        #print({self.type: self.value})
        #print('--------------------------------------------------------------')

def traverse(node):
    if isinstance(node, InternalNode):
        tree = [node.type, []]
        for child in node.children:
            tree[1].append(traverse(child))
    elif isinstance(node, ExternalNode):
        return {node.type: node.value}
    else:
        #print('???????????????????')
        #print(node)
        return None
    return tree