from flask import request, Flask, render_template, make_response, url_for, redirect
from jinja2 import Template
import json
from engine import Engine as en
global questions

app = Flask(__name__)

with open("static/Fragen/fragen.json") as json_data:
    #print(type(json.load(json_data)))
    questions = json.load(json_data)

for keys, values in questions.items():
    print(keys)
#print(questions["Frage 1"])

@app.route('/',methods=["GET", "POST"])
def index():
    if en.cookie_check("started") and en.cookie_check("question"):
        questionlist = []
        for keys, values in questions.items():
            questionlist.append(keys)
        question_num = (int(en.cookie_content("question")) - 1)
        if len(questionlist) >= question_num:
            #print(str(questionlist[question_num]))
            print("true")
            question = questions[questionlist[question_num]]
            #print(question)
            #print(question["answers"])
            answers = question["answers"]
            for i, y in question["answers"].items():
                print(y)
                #print(answers["1"])
            return(render_template("index.html", 
                questiontitle = str(questionlist[question_num]), 
                question = question["question"],
                answer = question["answers"]
                ))
    else:
        return render_template("index.html")

@app.route("/start",methods=["GET", "POST"] )
def api():
    questionlist = []
    if request.method == "POST":
        response = make_response(redirect("/"))
        if not en.cookie_check("started") or not en.cookie_check("question"):
            response.set_cookie("started", "1", None)
            response.set_cookie("question", "1", None)
            return response
    return(redirect("/"))


@app.route("/summary")
def summary():
    return render_template("Videokonferenz_Vergleich.html")

@app.route('/favicon.ico')
def favicon():

   pass

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)