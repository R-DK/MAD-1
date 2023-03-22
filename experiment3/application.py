from flask import Flask
from flask import render_template
from flask import request
from Templates import hello

app = Flask(__name__, template_folder='Templates')

@app.route('/', methods=["GET", "POST"])
def hello_world():
    if request.method=="GET":
        return render_template("get_details.html")
    elif request.method=="POST":
        username = request.form["user_name"]
        return render_template("display_details.html", name=username)
    else:
        print("Error check")

if __name__ == "__main__":
    app.debug = True
    app.run()
