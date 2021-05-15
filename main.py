from flask import request, Flask, render_template, make_response, url_for, redirect
from jinja2 import Template
import json
from engine import Engine as en
global questions

with open("static/Fragen/fragen.json") as json_data:
    #print(type(json.load(json_data)))
    questions = json.load(json_data)

for keys, values in questions.items():
    print(keys)
print(questions["Frage 1"])
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")
    

@app.route("/api",methods=["GET", "POST"] )
def api():
    questionlist = []
    if request.method == "POST":
        response = make_response(redirect("/"))
        if not en.cookie_check("started") or not en.cookie_check("question"):
            response.set_cookie("started", "1", None)
            response.set_cookie("question", "1", None)
            return response
    for keys, values in questions.items():
        questionlist.append(keys)
    try: 
        print(questions[1])
        print("yup")
    except:
        print("nope")
    return(redirect("/"))



@app.route("/summary")
def summary():
    return render_template("Videokonferenz_Vergleich.html")

@app.route('/favicon.ico')
def favicon():

   pass

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)