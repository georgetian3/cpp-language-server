from pprint import pprint


class Node:
    def __init__(self, type):
        self.type = str(type)

class InternalNode(Node):
    def __init__(self, type, children):
        super().__init__(type)
        self.children = children
        for i in range(len(self.children)):
            if not isinstance(self.children[i], Node):
                self.children[i] = ExternalNode(str(self.children[i]), str(self.children[i]))

class ExternalNode(Node):
    def __init__(self, type, value):
        super().__init__(type)
        self.value = value

def traverse(node):
    if isinstance(node, InternalNode):
        tree = {node.type: {}}
        for child in node.children:
            res = traverse(child)
            tree[node.type][list(res.keys())[0]] = list(res.values())[0]
    else:
        return {node.type: node.value}
    return tree