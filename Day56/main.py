from flask import Flask
import random

app = Flask(__name__)

randomly_generated_number = random.randint(0,9)

@app.route('/')
def home_page():
    return ("<h1>Guess a number between 0 and 9</h1>"
            "<img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif' width=200>")

@app.route('/<int:user_entered_number>')
def guess_page(user_entered_number):
    if user_entered_number < randomly_generated_number:
        return ("<h1 style='color: red'>Too low! Try again"
                "<img src='https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExeWx1czY1bmt3bDF6cHJtYTAzNDg5d3U4MXI1azRuZDZ3NDRwZWoyeiZlcD12MV9naWZzX3NlYXJjaCZjdD1n/fhLgA6nJec3Cw/giphy.gif'>")

    elif user_entered_number > randomly_generated_number:
        return ("<h1 style='color: green'>Too high! Try again"
                "<img src='https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExMDI3OXRkODNtNHQ5NHVxeHM5NDVzZXVjdWZrbGhlaWJxN2M0azNlMCZlcD12MV9naWZzX3NlYXJjaCZjdD1n/raBbE1fizfZGE/giphy.gif'>")

    else:
        return ("<h1 style='color: green'>Yes, you found it!!</h1>"
                "<img src='https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExMmE4eHVoMTRuNDJ0ZXd3cGRjOTNjb21uYTByNXowNmtxOHQzZHExNSZlcD12MV9naWZzX3NlYXJjaCZjdD1n/vxseYpI4M8tYMehu3w/giphy.gif'>")



if __name__ == "__main__":
    app.run(debug=True)