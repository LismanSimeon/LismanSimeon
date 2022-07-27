#Vim python program
import math
import random

first_name = input("first_name: " )
school = input("school: ")
student_id = int(input("student_id: "))
location = input("located: ")

madlib = (f"My name is {first_name} and i am a student at {school}\U0001F600, \ {student_id} is my student id_number and i stay outside school in {location}.")
print(madlib)
if first_name == "Luyando":
    print("Welcome to your final year mate.\U0001F917")
        
elif school != "unza":
    new_school = input("What school do you go to: ?")
    if new_school =="CBU":
        print("Must be great learning at such an institution.")

price  = 1000000
good_credit = True
buyer = int(price) * (10/100)

if good_credit == True:
    print(f"You can pay the down payment K{buyer}")
else:
    buyer = int(price) * (20/100)
print(buyer)
#adding emoji's to the code
print("Love means \U0001F618")
print("Sad means \U0001F62A ")
print("Sick means \U0001F637")
#print("Fuck you means \U0001F621")

name = input("name: ?")

if len(name) < 3:
    print("Name must be at least 3 characters long.")
elif len(name) > 50:
    print("Name can be a maximum of 50 characters.")
else:
    print("Name looks good.")

#weight coverter
weight= int(input("weight: "))
mans = input("Lbs or Kg: ")

if mans == "Lbs":
   pounds = int(weight) * 0.45
   print(f"You weigh {pounds} kilos")
elif mans == "kg":
   pounds = int(weight) / 0.45
   print(f"You weigh {pounds} pounds")

mylist = ["Muwemba"," Simawe", "Tom", "mu"]
print(random.choice(mylist))
















































