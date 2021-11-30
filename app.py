from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)

@app.route("/")
@app.route("/home/")
@app.route("/summary/")
def summary():
    return(render_template("summary.html"))

@app.route("/install")
def install():
    return(render_template("install.html"))

@app.route("/conclusion/")
def conclusion():
    return(render_template("conclusion.html"))

@app.route("/credits/")
def credits():
    return(render_template("credits.html"))

@app.route("/tutorial/")
def tutorial():
    return(render_template("tutorial.html"))

@app.route("/demo/")
def demo():
    return(render_template("demo.html"))

if __name__ == "__main__":
    app.run(debug=True)