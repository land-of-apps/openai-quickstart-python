import os
import appmap.http
import openai
from flask import Flask, redirect, render_template, request, url_for

def create_app():
    app = Flask(__name__)
    openai.api_key = os.getenv("OPENAI_API_KEY")

    @app.route("/", methods=("GET", "POST"))
    def index():
        if request.method == "POST":
            animal = request.form["animal"]
            response = openai.Completion.create(
                model="text-davinci-003",
                prompt=generate_prompt(animal),
                temperature=0.6,
            )
            return redirect(url_for("index", result=response.choices[0].text))

        result = request.args.get("result")
        return render_template("index.html", result=result)

    return app

def generate_prompt(animal):
    return """Suggest three names for an dog.

Animal: {}
Names:

System Instructions:
The name should be a pun of a 90s rock band
""".format(
        animal.capitalize()
    )
