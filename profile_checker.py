print("Please enter the following information:")
Name=input("please enter your name:")
Age=int(input("please enter your age:"))
GPA=float(input("please enter your GPA:"))
Filed=input("enter your field:")
graduated=input("are you graduated?").lower()

#print in terminal

print("your information:")
print("your name is",Name)
print("your age is",Age)
print("your gpa is",GPA)
print("your field is:",Filed)


<<<<<<< HEAD
if graduated =='yes':
=======
if graduated=='yes':
>>>>>>> 8336d40d3526b3247fd21f8b8051c835f582380c
         print("you are graduated")
else:
        print("no")

if Age < 25 and GPA<=3.5 and graduated=='yes':
        print("You are eligible for a scholarship!!")
elif Age < 30 and GPA >= 2.5:
        print("you are eligible for internship!!")
else :
<<<<<<< HEAD
       print("apply again later")
=======
       print("apply again later")
>>>>>>> 8336d40d3526b3247fd21f8b8051c835f582380c
