from flask import Flask

app = Flask(__name__, )

@app.route('/')
def main():
    return './dist/index.html'


@app.route('/about')
def about():
    return './dist/index.html'


@app.route('/contact')
def contact():
    return './dist/index.html'

if __name__ == "__main__":
    app.run(debug=True)