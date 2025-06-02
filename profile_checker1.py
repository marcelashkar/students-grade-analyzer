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


if graduated=='yes':
         print("you are graduated")
else:
        print("no")

if Age < 25 and GPA<=3.5 and graduated=='yes':
        print("You are eligible for a scholarship!!")
elif Age < 30 and GPA >= 2.5:
        print("you are eligible for internship!!")
else :
       print("apply again later")
