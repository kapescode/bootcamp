#Create an input command but store the answer as an integer 
number_students = int(input("How many students are registering for this exam? "))

#Open the register file to write the new student IDs each time, using w to overwrite the file each time
with open ("reg_form.txt", "w") as file:

#loop for the number of students
    for i in range (number_students):               
        student_id = input("Enter the ID number for the next student: ")
    
#writing command to add the student ID and new line, then dotted lines
        file.write(student_id + "\n")
        file.write("\n.................." + "\n \n")