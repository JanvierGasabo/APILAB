#Student Database
students=[]
#Function to add a new student 
def Add_student():
    print(" Enter student details : ")
    name=input("full Name : ")
    age=int(input("Age: "))
    year_Of_Study=input("Year_Of_Study: ")
    course=input("course: ")
    marks=float(input("Enter Marks for the course: "))
    next_course=input("NEXT_COURSE: ")

    #Create a dictionary for student
    student={
    "Name": name,
    "Age":age,
    "Year_of_Study":year_Of_Study,
    "Course":course,
    "Marks":marks,
    "Next_course":next_course
    }   
#add students to database
    students.append(student)
    print("\n Student added successfully! \n")

# Colection of information from 5 students.

    for student_Number in range(5):
        Add_student()

# Display of all information about student

print("Information of all students :")
print("-------------------------------------------------------------------")
for student in students:
    print("\n student details :  ")
    for key,value in student.items():
        print(f" {key}:{value}")




