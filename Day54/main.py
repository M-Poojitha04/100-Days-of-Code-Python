from flask import Flask
# import random

app = Flask(__name__)
# $env:FLASK_APP = "main.py"
# print(random.__name__)
# print(__name__)
@app.route('/')
def hello_world():
    return "Hello, World!"

if __name__ == "__main__":
    app.run()
    
# def outer_function():
#     print("I'm outer")
    
#     def nested_function():
#         print("I'm inner")
        
#     return nested_function
    
# inner_function = outer_function()
# inner_function()