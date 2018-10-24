from flask import Flask,render_template

#steup Flask server
app = Flask(__name__)

@app.route("/")
def homepage():
    return "Welcome to C4E22 Web module , enjoy aa"
#nếu người dùng truy cập vào trnag chủ thì hãy gọi hàm này

@app.route("/thuy")
def hello_thuy():
    return "Hello Thuy"

@app.route("/praise/linh")
def praise_linh():
    return "Linh is awesome"

@app.route("/praise/<name>")
def praise(name):
    return name + " is awesome"

# @app.route("/add/<a>/<b>")
# def add(a,b):
#     s = int(a) + int(b)
#     return str(s)

@app.route("/add/<int:a>/<int:b>")
def add(a,b):
    s = a + b
    return str(s)

@app.route("/question")
def show_question():
    return render_template("question.html")


if __name__ == "__main__":
    app.run(debug=True)
#
