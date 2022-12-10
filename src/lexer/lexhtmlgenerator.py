import re


class LexHTMLGenerator:


    def __init__(self):
        self.__tokens = []
        """ self.colors = {
            'string_literal': 'CE915B',
            'IDENTIFIER': '4FB8FE',
            'OPERATOR_OR_PUNCTUATOR': 'FFFFFF',
            'WS': 'FF0000',
            'PREPROCESSING_OPERATOR': '4FB8FE',
            'INTEGER_LITERAL': '4FB8FE',
            'KEYWORD': 'C586A1',
        } """

    def create_html_token(self, token):
        #if token.type not in self.colors:
            #print('HTML invalid type:', token)
            #pass
        value = token.value
        value = value.replace('\n', '<br>')
        value = value.replace(' ', '&nbsp')
            
        self.__tokens.append(f'<span id="{len(self.__tokens)}" class={token.type} onmouseover="show_info({len(self.__tokens)})" onmouseleave="hide_info({len(self.__tokens)})">{value}</span>')


    def write_html(self, filename):
        with open('output/base.html', encoding='utf8') as f:
            html = f.read()
        html = html.replace('</code>', ''.join(self.__tokens) + '</code>')

        with open('output/output.html', 'w', encoding='utf8') as f:
            f.write(html)
        # '\n'.join(self.__classes.values()) + '''

