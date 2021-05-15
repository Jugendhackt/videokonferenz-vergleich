from flask import request, Flask, render_template, make_response, url_for, redirect, session
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
    en.cookie_delete()
    if en.cookie_check("started") and en.cookie_check("question"):
        questionlist = []
        # lists all questions
        for keys, values in questions.items():
            questionlist.append(keys)
        
        question_num = (int(en.cookie_content("question")) - 1)
        try:
            question = questions[questionlist[question_num]]
            #print(question)
            #print(question["answers"])
            answers = question["answers"]
            answer_options = []
            #print(answer)
            #print(question["answers"])
            #for y, x in question["answers"].items():
            #    print(y)
                #print("\n")
            #    print(x)
                #for q, w in :
                #    print(q)
                #answer_options.append(values)
                #print(answers["1"])
            #print(answer_options)
            return(render_template("index.html", 
                started = True,
                questiontitle = str(questionlist[question_num]) + " von " + str(len(questionlist)), 
                question = question["question"],
                answer = answer_options,
                ))
        except:
            return "Finished"
    else:
        return render_template("index.html")


#handel startup and set started question to 1
@app.route("/start",methods=["GET", "POST"] )
def api():
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

@app.route('/interface',methods=["GET", "POST"])
def interface():
    if request.form['Neustarten'] == 'Neustarten':
        return(en.cookie_delete())
    return(redirect("/"))


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)