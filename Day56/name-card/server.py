# 1. Download html5up's "Identity" template from this lesson's resources (PS: you can also browse the live demo sites on https://html5up.net/ and use a different template like "Astral" or "Ethereal"...)
#
# 2. Create a new PyCharm project called name-card and create a new Flask Application from scratch.
#
# 3. Create the necessary folders and move the relevant files from the download in step1.
#
# 4. Get the website to work when you access the root route ("/")
#
# 5. Personalise the website, change the background image, change the text, change the links, make it your own.

from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')
def home_page():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)

