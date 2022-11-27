import re


class LexHTMLGenerator:


    def __init__(self):
        self.__tokens = []
        self.colors = {
            'string_literal': 'CE915B',
            'IDENTIFIER': '4FB8FE',
            'OPERATOR_OR_PUNCTUATOR': 'FFFFFF',
            'WS': 'FF0000',
            'PREPROCESSING_OPERATOR': '4FB8FE',
            'INTEGER_LITERAL': '4FB8FE',
            'KEYWORD': 'C586A1',
        }

        self.__classes = {type: '.' + type + ''' {
    color: #''' + self.colors[type] + '''
}''' for type in self.colors
        }

    def create_html_token(self, token):
        if token.type not in self.colors:
            #print('HTML invalid type:', token)
            pass
        value = token.value
        if type(value) == str and re.fullmatch('\s+', value):
            value = value.replace('\n', '<br>')
            value = value.replace(' ', '&nbsp')
            self.__tokens.append(value)
        else:
            self.__tokens.append(f'<span id="{len(self.__tokens)}" class={token.type} onmouseover="show_info({len(self.__tokens)})" onmouseleave="hide_info({len(self.__tokens)})">{token.value}</span>')


    def write_html(self, filename):
        with open('base.html', encoding='utf8') as f:
            html = f.read()
        html = html.replace('</code>', ''.join(self.__tokens) + '</code>')

        with open('output/output.html', 'w', encoding='utf8') as f:
            f.write(html)
        # '\n'.join(self.__classes.values()) + '''

