from flask import request, Flask, render_template, make_response, url_for, redirect, session
from jinja2 import Template
import json
from engine import Engine as en
global question

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
            if request.method == "POST":
                try:
                    if request.form['Nein']:
                        print("nein")
                        print(question["answers"]["2"]["whitelist"])
                        test = en.cookie_content("question")
                        res = make_response(redirect("/"))
                        test_res = int(test) + int(1)
                        tests = str(test_res)
                        res.set_cookie("question", tests, None)
                        res.set_cookie("whitelist", str(question["answers"]["2"]["whitelist"]), None)
                        return(res)

                except:
                    if request.form['Ja']:
                        print("ja")                        
                        test = en.cookie_content("question")
                        res = make_response(redirect("/"))
                        test_res = int(test) + int(1)
                        tests = str(test_res)
                        res = make_response(redirect("/"))
                        res.set_cookie("question", tests, None)
                        res.set_cookie("whitelist", str(question["answers"]["2"]["whitelist"]), None)
                        return(res)


            return(render_template("index.html", 
                started = True,
                questiontitle = str(questionlist[question_num]) + " von " + str(len(questionlist)), 
                question = question["question"],
                ))
        except :
            
            return request.cookies.get('whitelist')
    else:
        return render_template("index.html")


#handel startup and set started question to 1
@app.route("/start",methods=["GET", "POST"] )
def start():
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

@app.route('/restart',methods=["POST"])
def restart():
    if request.form['Neustarten'] == 'Neustarten (Löscht alle Cookies)':
        return(en.cookie_delete())
        return(redirect("/"))
    return(redirect("/"))
    
@app.route('/interface',methods=["POST"])
def interface():
    return(redirect("/"))


@app.route('/yes', methods=["POST"])
def yes():
   if request.form['Ja']:
        return(redirect("/"))


@app.route('/no', methods=["POST"])
def no():
    if request.form['Nein']:
        return(redirect("/"))


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)