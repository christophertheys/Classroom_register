# Class register program

# The user will be asked to enter the names of the students
print("The is a Class register program in order to capture attendance ".upper(), "\n")

user_type_for_class_name = input("Please enter in the class name for the register : ")
user_input_program = str()
counter_of_students = -1

# The counter is set at -1 in order to account for and cancel out the additional input of 'Stop' from the user

while user_input_program != str("Stop"):
    user_input_program = input("Enter the name of student  : \n")
    print("(if done, type in 'Stop')", "\n")
    counter_of_students = counter_of_students + 1

print("A total of {} students are attending the class and accounted for on the register ".format(counter_of_students))

# The final statement will print out total number of students accounted for in the loop, excluding the input of 'Stop'
