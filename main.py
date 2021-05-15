from flask import request, Flask, render_template, make_response
from jinja2 import Template
import json


app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")


@app.route("/api",methods=["GET", "POST"] )
def api():
    print(request.method)
    if request.method == "POST":
        if not request.cookies.get("key"):
            if request.form.get("Start") == "Start":
                res = make_response("Setting a cookie")
                res.set_cookie("key", value="test", max_age=None)
                return res

        #return(request.form.get("Start"))
    return("api")

@app.route("/summary")
def summary():
    return render_template("Videokonferenz_Vergleich.html")



if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)