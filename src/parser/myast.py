import json
from pprint import pprint


class Node:
    def __init__(self, type, leaf, children=[]):
        self.type = type
        self.leaf = leaf
        self.children = children

class AST:

    def __init__(self, root):
        self.root = root

    def __traverse(self, node):
        if not node.children:
            subtree = {f'{node.type}: {node.leaf}': None}
        else:
            subtree = {
                f'{node.type}: {node.leaf}':
                    {key: item for child in node.children
                        for key, item in self.__traverse(child).items()
                    }
            }

        pprint(subtree)
        return subtree

    def to_dict(self):
        return self.__traverse(self.root)

    def __str__(self):
        return str(self.__traverse(self.root))

    def export(self):
        with open('out.json', 'w') as f:
            json.dump(self.to_dict(), f, ensure_ascii=False, indent=4)