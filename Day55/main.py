from flask import Flask
# import random

app = Flask(__name__)
# $env:FLASK_APP = "main.py"
# print(random.__name__)
# print(__name__)
@app.route('/')
def hello_world():
    return ('<h1 style="text-align: center">Hello, World!</h1>'
            '<p>This is a paragraph</p>''<img src="https://images.pexels.com/photos/674010/pexels-photo-674010.jpeg?auto=compress&cs=tinysrgb&dpr=1&w=500" width=200>')

@app.route('/bye')
def bye():
    return "Bye!!"

#Dynamic variable for url
@app.route('/<name>')
def greeting(name):
    return f"Hey there, {name}"

# @app.route('/<path:name>')          #helps to include / in path ex: poojitha//
# def greet(name):
#     return f"Hey there, {name}"

@app.route('/username/<name>/<int:number>')
def greet(name, number):
    return f"Hey {name}, you are {number} years old!"

if __name__ == "__main__":
    app.run(debug=True)