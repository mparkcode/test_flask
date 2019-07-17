from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def say_hi():
    return "Hello World"

if __name__ == "__main__":
        app.run(host=os.getenv('IP', '127.0.0.1'), port=int(os.getenv('PORT', 8080)), debug=True)