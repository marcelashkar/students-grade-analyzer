def get_student (n,students=None):
    if students is None:
        students=[]              #vide


    if n==0:
        return students   
    

    name=input("enter student name:")
    grade= float(input("enter grade for ",name ,"out of 100"))


    students.append((name,grade))

    return

    get_students_data(n-1,students)

def display_student_summary(students):                    
    print("student grades :")
    for name,grade in students:
        print("the name is ",name,"and the grade is",grade)


def get_avg_grade(students):                     #average of grades
    total=0
    for grade in students:
        total +=grade
    average= total/len(students)
    return average


def get_heighest_grade(students):
    return max(students,lambda x:x[1])


def count_passed(students):                                     #number of students passed
    return sum(1 for name,garde in students if grade>=60)



def number():
    numb=int(input("enter number of students:")) #entter number of students

    students=get_student(numb)                   #getting number of stuf=dents

    display_student_summary(students)            #Display 

    print("avg",get_avg_grade(students))           

    top_name,top_grade=get_heighest_grade(students)

    print("top:",top_name,top_grade)

    print("passed",count_passed(students))
