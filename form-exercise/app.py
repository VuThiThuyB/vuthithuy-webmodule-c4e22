from flask import Flask,request,render_template
import mlab2
from random import choice
from infomation import Infomation

mlab2.connect()
app = Flask(__name__)

@app.route("/information", methods=["GET", "POST"])
def information():
    if request.method == "GET": 
        return render_template("register.html")
    elif request.method == "POST":
        form = request.form
        firstname = form["firstname"]
        lastname = form["lastname"]
        email = form["email"]
        yob = form["yob"]
        gender = form["gender"]
        city = form["city"]
        print(firstname)
        print(lastname)
        print(email)
        print(yob)
        print(gender)
        print(city)
        alphabet = "abcdefghijklmnopqrstuvwxyz".upper()
        c = ""
        for _ in range(6):
            c += choice(alphabet)
        
        p = Infomation(FirstName = firstname, LastName = lastname, Email = email,Yob=yob,Gender = gender,City=city,code=c )
        p.save()
        # print(form)
        return "Gotcha"


if __name__ == "__main__":
    app.run(debug=True)