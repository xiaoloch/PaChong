from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "你好 世界"

@app.route('/test')
def func01():
    return "Hello World"

if __name__ == '__main__':
    app.run(debug=True)

