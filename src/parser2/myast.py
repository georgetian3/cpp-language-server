from pprint import pprint


class InternalNode:
    def __init__(self, type, children):
        print('-------------------InternalNode:', type, children)
        self.type = type
        self.children = children
        print('begin print')
        for i in range(len(self.children)):
            print(self.children[i])
            if not isinstance(self.children[i], ExternalNode):
                print('not node')
class ExternalNode:
    def __init__(self, type, value):
        print('--------------------ExternalNode:', type, value)
        self.type = type
        self.value = value

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