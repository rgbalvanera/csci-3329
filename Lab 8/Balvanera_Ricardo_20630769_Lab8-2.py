#input message
grade1, grade2 , grade3 = input("Enter your grades (e.g., A B C):").split()
#calculate the gpa using if statements
gpa = 0
if(grade1 == "A"):
    gpa += 4.0
elif(grade1 == "B"):
    gpa += 3.0
elif(grade1 == "C"):
    gpa += 2.0
elif(grade1 == "D"):
    gpa += 1.0
#repeat for grade 2
if(grade2 == "A"):
    gpa += 4.0
elif(grade2 == "B"):
    gpa += 3.0
elif(grade2 == "C"):
    gpa += 2.0
elif(grade2 == "D"):
    gpa += 1.0
#repeat for grade 3
if(grade3 == "A"):
    gpa += 4.0
elif(grade3 == "B"):
    gpa += 3.0
elif(grade3 == "C"):
    gpa += 2.0
elif(grade3 == "D"):
    gpa += 1.0
    
#average the 3 grades to get final gpa
gpa /= 3
#output message
print("Your GPA is ", gpa)