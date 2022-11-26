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
            print('HTML invalid type:', token)
            return
        value = token.value
        #print('Value:', value)
        if type(value) == str and re.fullmatch('\s+', value):
            value = value.replace('\n', '<br>')
            value = value.replace(' ', '&nbsp')
            self.__tokens.append(value)
        else:
            self.__tokens.append(f'<span class="{token.type}" data-bs-toggle="tooltip" data-bs-html="true" title="{token.type}">{token.value}</span>')

    def write_html(self, filename):
        with open(filename, 'w', encoding='utf8') as f:
            f.write('''<!doctype html>
        <html lang="en">
        <head>
            <meta charset="utf-8">
            <meta name="viewport" content="width=device-width, initial-scale=1">
            <title>Lexing output</title>
            <link href="bootstrap.min.css" rel="stylesheet">
            <script src="bootstrap.bundle.min.js"></script>
            <style>
                code {
                    color: #ffffff;
                    line-height: 1.2;
                }''' + '\n'.join(self.__classes.values()) + '''
            
span {
  border-radius: 8px;
}
            </style>
        </head>
        <body style="background-color:#000000;">
            <code style="display: block; margin: 2%">''' +  ''.join(self.__tokens) + '''
            </code>
            <script>
            var tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
            var tooltipList = tooltipTriggerList.map(function (tooltipTriggerEl) {
                return new bootstrap.Tooltip(tooltipTriggerEl);
            });
            </script>
        </body>
        </html>''')