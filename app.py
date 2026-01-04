from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/<path:path>')
def page(path):
    template_path = f'pages/{path}.html'
    return render_template(template_path, path=path)

if __name__ == '__main__':
    app.run(debug=True)
