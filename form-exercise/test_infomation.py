from infomation import Infomation
import string
from random import choice
import mlab2


#1. connect to DB
mlab2.connect()


#2.Prepare data
f = "Thuy"
l = "Vu"
email = "abc"
yob = "20/09/1997"
gender = "nu"
city="hanoi"

alphabet = "abcdefghijklmnopqrstuvwxyz".upper()
c = ""
for _ in range(6):
    c += choice(alphabet)
print(c)  #print 6 ki tu trong vong for



#3.Creat document
p = Infomation(FirstName = f, LastName = l, Email = email,Yob=yob,Gender = gender,City=city,code=c )

#4.Save
p.save()
