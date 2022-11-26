


class LexHTMLGenerator:


    

    

    def __init__(self):
        self.__tokens = []
        self.colors = {
            'string_literal': 'orange',
            'IDENTIFIER': 'blue',
            'OPERATOR_OR_PUNCTUATOR': 'black',
            'WS': 'white',
        }

    def create_html_token(self, token):
        if token.type not in self.colors:
            print('HTML invalid type:', token)
            return
        value = token.value
        value.replace('\n', '<br>')
        value.replace('\t', '&#09;')
        self.__tokens.append(f'<span data-bs-toggle="tooltip" data-bs-html="true" title="{token.type}"><pre>{token.value}</pre></span>')

    def write_html(self, filename):

        with open(filename, 'w', encoding='utf8') as f:
            f.write(f'''<!doctype html>
        <html lang="en">
        <head>
            <meta charset="utf-8">
            <meta name="viewport" content="width=device-width, initial-scale=1">
            <title>Lexing output</title>
            <link href="bootstrap.min.css" rel="stylesheet">
            <script src="bootstrap.bundle.min.js"></script>
            <style>
            .code {{
                color: black
            }}
            </style>
        </head>
        <body>
            <code>
            {''.join(self.__tokens)}
            </code>
            <script>
            var tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
            var tooltipList = tooltipTriggerList.map(function (tooltipTriggerEl) {{
                return new bootstrap.Tooltip(tooltipTriggerEl);
            }});
            </script>
        </body>
        </html>''')