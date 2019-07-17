from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/about")
def about():
    return render_template('about.html')

if __name__ == "__main__":
        app.run(host=os.getenv('IP', '127.0.0.1'), port=int(os.getenv('PORT', 8080)), debug=True)