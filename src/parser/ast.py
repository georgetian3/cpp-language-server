import json



class Node:
    pass

class AST:


    def __init__(self):
        self.root = None
        pass

    def __traverse(self, ast):
        if ast[0] == 'binop':
            output = {
                f'binop: {ast[1]}': {
                    'left operand': self.__traverse(ast[2]),
                    'right_operand': self.__traverse(ast[3])
                }
            }
        elif ast[0] == 'number':
            output = {'number': ast[1]}
        elif ast[0] == 'name':
            output = {'name': ast[1]}
        elif ast[0] == 'grouped':
            output = {'grouped': self.__traverse(ast[1])}
        else:
            print('Error')
        exit()

    def export(self):
        output = self.__traverse_ast(self.root)
        with open('out.json', 'w') as f:
            json.dump(output, f, ensure_ascii=False, indent=4)