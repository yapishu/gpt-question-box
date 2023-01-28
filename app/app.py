import os, openai
from gevent.pywsgi import WSGIServer
from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)

openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route("/", methods=("GET", "POST"))
def index():
    if request.method == "POST":
        prompt = request.form["prompt"]
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=generate_prompt(prompt),
            temperature=0.6,
            max_tokens=256,
        )
        return redirect(url_for("index", result=response.choices[0].text))

    result = request.args.get("result")
    return render_template("index.html", result=result)

def generate_prompt(prompt):
    return """Answer the following answer in a precise but sophisticated way. Explain your reasoning and any corroborating evidence. If the question has to do with personal values, mimic the values of an avowed Pakistani nationalist.
Prompt: {}
Response:""".format(prompt.capitalize())

if __name__ == "__main__":
    http_server = WSGIServer(('0.0.0.0', 8090), app)
    http_server.serve_forever()
