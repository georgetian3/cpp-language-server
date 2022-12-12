from pprint import pprint


class InternalNode:
    def __init__(self, type, children):
        self.type = type
        self.children = children
        for i in range(len(self.children)):
            pass
        ast = traverse(self)
        print('--------------------------------------------------------------')
        print(ast)
        print('--------------------------------------------------------------')

    
class ExternalNode:
    def __init__(self, type, value):
        self.type = type
        self.value = value
        print('--------------------------------------------------------------')
        print({self.type: self.value})
        print('--------------------------------------------------------------')

def traverse(node):
    if isinstance(node, InternalNode):
        tree = {node.type: {}}
        for child in node.children:
            res = traverse(child)
            tree[node.type][list(res.keys())[0]] = list(res.values())[0]
    elif isinstance(node, ExternalNode):
        print(node.type, node.value)
        return {node.type: node.value}
    else:
        print('???????????????????')
        return {None: None}
    return tree