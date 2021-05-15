from flask import request, Flask, render_template
from jinja2 import Template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")


@app.route("/api",methods=["GET", "POST"] )
def api():
    print(request.method)
    if request.method == "POST":
        if request.form.get("Start") == "Start":
            return render_template("Start")
        #return(request.form.get("Start"))
    return("api")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)