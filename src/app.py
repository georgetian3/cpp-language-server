from flask import Flask, send_file, request
from flask_cors import CORS


app = Flask(__name__)
CORS(app)


@app.get('/')
def index_get():
    return send_file('editor.html')

@app.post('/process')
def process():
    src = request.data.decode('utf8')
    print('Source:', src)

    res = '<span style="color:red">' + src + '</span>'
    suggestions = ['test', 'test1']
    print('Formatting:', res)
    print('Autocomplete:', suggestions)
    return {'formatting': res, 'suggestions': suggestions}

if __name__ == '__main__':
    app.run(debug=False, port='5000')