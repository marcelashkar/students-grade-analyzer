def display_students_summary(students: list):
    if len(students)==0:
        return
    print("summary")
    for student in students:
        print(student[0],":",student[1])
 
 
def get_avg_grade(students:list):
    if len(students)==0:
        return 0
    sum=0
    for student in students:
        
        sum+=student[1]

    return sum/len(students)

def get_heighest_grade(students:list):    #first way

    highest_grade_students=[]

    highest_grade =students[0][1]

    for student in students:
        if student[1] == highest_grade:
            highest_grade_students.append(student)
        elif student[1] > highest_grade:
             highest_grade = student[1]
             highest_grade_students = []
             highest_grade_students.append(student)


    return highest_grade_students  

students=[("joe",23),("jhon",59),("ali",65),("amir",10)]

print("summary:")
display_students_summary(students)

print("average grade:")
print(get_avg_grade(students))
print("highest grade students:")
print(get_heighest_grade(students))