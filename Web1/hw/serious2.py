from flask import *


List_user={
    "huy":{
        "name":"Nguyễn Quang Huy",
        "age":29
    },
    "tuananh":{
        "name":"Huỳnh Tuấn Anh",
        "age":22
    }
}

app = Flask(__name__)

@app.route("/user/<username>")
def Infomation(username):
    if username in List_user:
        return render_template("serious2.html",user=List_user[username])
    else:
        return ("User not found")


if __name__ == "__main__":
    app.run(debug=True)