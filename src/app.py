from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello():
    return render_template("particles.html")


@app.route('/about')
def demo():
    return render_template("about.html")


if __name__ == "__main__":
    app.run()
