from flask import request, Flask, render_template, make_response, url_for, redirect, session
from jinja2 import Template
import json
from engine import Engine as en
global questions

app = Flask(__name__)

#reads json data at bootup 
with open("static/Fragen/fragen.json") as json_data:
    questions = json.load(json_data)

#lists all question found in document
for keys, values in questions.items():
    print(keys)

@app.route('/',methods=["GET", "POST"])
def index():
    if en.cookie_check("started") and en.cookie_check("question"):
        questionlist = []
        # lists all questions from json and appends to questionlist
        for keys, values in questions.items():
            questionlist.append(keys)
        #gets current question count from cookie

        question_num = (int(en.cookie_content("question")) - 1)
        try:
            #print(questions[questionlist[question_num]])
            question = questions[questionlist[question_num]]
            print(question)
            answers = question["answers"]
            return(render_template("index.html", 
                started = True,
                questiontitle = str(questionlist[question_num]) + " von " + str(len(questionlist)), 
                question = question["question"],
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
    if request.form['Neustarten'] == 'Neustarten (Löscht alle Cookies)':
        return(en.cookie_delete())
        return(redirect("/"))
    elif request.form['Nein'] == 'Nein':
        print("nein")
    elif request.form['Ja'] == 'Ja':
        print("JA")
    else:
        return(redirect("/"))
    


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)