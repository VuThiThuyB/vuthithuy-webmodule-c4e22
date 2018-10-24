from flask import Flask,render_template,redirect

app = Flask(__name__)

@app.route("/")
def homepage():
    return ("WELCOME")

@app.route("/about-me")
def information():
    return render_template("infomation.html")

@app.route("/school")
def school():
    return redirect("http://techkids.vn ", code=302)

if __name__ == "__main__":
    app.run(debug=True)
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port) 