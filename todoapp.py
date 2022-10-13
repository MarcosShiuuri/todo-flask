from flask import Flask, render_template as rt, request, redirect

app = Flask(__name__)
@app.route("/", methods=["POST", "GET"])
def homepage():
    if request.method =="POST":
        print("Retornou um submit de POST")
        return redirect("/")
    else:
        return rt("index.html")
