from flask import Flask, render_template, url_for, jsonify
from flask_bootstrap import Bootstrap

app = Flask(__name__)

@app.route('/')
def index():
    return jsonify({"message":"Index Page"})


if __name__ == '__main__':
    app.run(debug=True)