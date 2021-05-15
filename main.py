from flask import request, Flask, render_template, make_response, url_for, redirect
from jinja2 import Template
import json
from engine import Engine as en

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")


@app.route("/api",methods=["GET", "POST"] )
def api():
    print(request.method)
    if request.method == "POST":
        print(en.cookie_check("key"))
        if not en.cookie_check("key"):
            return en.setcookie("key","test",redirect("/") )
    return(redirect("/"))



@app.route("/summary")
def summary():
    return render_template("Videokonferenz_Vergleich.html")

@app.route('/favicon.ico')
def favicon():
    
   pass

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)