from flask import Flask
from flask import render_template

app = Flask(__name__,template_folder="templates")

@app.route("/user/<name>")
def user(name=""):
    age = 63
    my_list = [1,2,3,4,5,6,7,8,9,10]
    return render_template("html_web4.html",name=name,age=age,list=my_list)

if __name__ == "__main__":
    app.run(debug=True)
