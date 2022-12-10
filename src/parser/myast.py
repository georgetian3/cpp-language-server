import json
from pprint import pprint


class Node:
    def __init__(self, type, value, children=[]):
        self.type = type
        self.value = value
        self.children = children

class AST:

    def __init__(self, root):
        self.root = root

    def __traverse(self, node):

        subtree = (node.type, node.value)
        if node.children:
            subtree = [subtree]
            for child in node.children:
                subtree.append(self.__traverse(child))

        return subtree


    """ def to_dict(self):
        return self.__traverse(self.root) """

    def get_list(self):
        return self.__traverse(self.root)

    def __str__(self):
        return str(self.__traverse(self.root))

    """ def export(self):
        with open('out.json', 'w') as f:
            json.dump(self.to_dict(), f, ensure_ascii=False, indent=4) """