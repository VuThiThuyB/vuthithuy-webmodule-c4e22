from flask import Flask,render_template,request
import mlab
from poll import Poll

app = Flask(__name__)
mlab.connect()


#print add poll
@app.route("/polls")
def polls():
    #1.Read all poll
    poll_list = Poll.objects()
    return render_template("polls.html",polls = poll_list)

if __name__ == "__main__":
    app.run(debug=True)