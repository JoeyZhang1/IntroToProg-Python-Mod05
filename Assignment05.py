# ------------------------------------------------------------------------------------------ #
# Title: Assignment05
# Desc: This assignment demonstrates using dictionaries, files, and exception handling
# Change Log: (Who, When, What)
#   JZhang,5/13/2025,Created Script
#   JZhang,5/21/2025,Modified Script
# ------------------------------------------------------------------------------------------ #
import json

# Define the Data Constants
MENU: str = '''
---- Course Registration Program ----
  Select from the following menu:  
    1. Register a Student for a Course.
    2. Show current data.  
    3. Save data to a file.
    4. Exit the program.
----------------------------------------- 
'''
# Define the Data Constants
FILE_NAME: str = "Enrollments.json"

# Define the Data Variables and constants
student_first_name: str = ''  # Holds the first name of a student entered by the user.
student_last_name: str = ''  # Holds the last name of a student entered by the user.
course_name: str = ''  # Holds the name of a course entered by the user.
student_data:dict = {}  # one row of student data
students: list = []  # a table of student data
file = None  # Holds a reference to an opened file.
menu_choice: str  # Hold the choice made by the user.

# When the program starts, read the file data into a list of lists (table)
# Extract the data from the file

try:
    file = open(FILE_NAME, "r")

    students = json.load(file)

    file.close()
except FileNotFoundError as e:
    print("Text file must exist before running this script!\n")
    print("Built-In Python error info: ")
    print(e, e.__doc__, type(e), sep='\n')
except Exception as e:
    print("Please check that the file is in json format.")
    print("-- Technical Error Message -- ")
    print(e, e.__doc__, type(e), sep='\n')
finally:
    if not file.closed:
        file.close()

# Present and Process the data
while True:

    # Present the menu of choices
    print(MENU)
    menu_choice = input("What would you like to do: ")

    # Input user data
    if menu_choice == "1":  # This will not work if it is an integer!

        try:
            student_first_name = input("Enter the student's first name: ")
            if not student_first_name:
                raise ValueError("Please enter a first name: ")
            if not student_first_name.isalpha():
                raise ValueError("The last name should not contain numbers.")
            student_last_name = input("Enter the student's last name: ")
            if not student_last_name:
                raise ValueError("Please enter a last name.")
            if not student_last_name.isalpha():
                raise ValueError("The last name should not contain numbers.")
            course_name = input("Please enter the name of the course: ")
            if not course_name:
                raise ValueError("Please enter course name.")
            student_data = {"FirstName": student_first_name,
                            "LastName": student_last_name,
                            "CourseName": course_name}
            students.append(student_data)
            print(f"You have registered {student_first_name} {student_last_name} for {course_name}.")
        except ValueError as e:
            print(e)  # Prints the custom message
            print("-- Technical Error Message -- ")
            print(e.__doc__)
            print(e.__str__())
        except Exception as e:
            print("There was a non-specific error!\n")
            print("-- Technical Error Message -- ")
            print(e, e.__doc__, type(e), sep='\n')
        continue

    # Present the current data
    elif menu_choice == "2":

        # Process the data to create and display a custom message
        if not students:
            print("No students registered.")
        else:
            print("-" * 50)
            for student in students:
                print(f"Student {student['FirstName']} {student['LastName']} is enrolled in {student['CourseName']}")
            print("-" * 50)
        continue

    # Save the data to a file
    elif menu_choice == "3":

        try:
            file = open(FILE_NAME, "w")
            json.dump(students, file, indent=4)
            file.close()
            print("The following data was saved to file!")
            for student in students:
                print(f"Student {student['FirstName']} {student['LastName']} is enrolled in {student['CourseName']}")
        except Exception as e:
            if not file.closed:
                file.close()
            print("Error: There was a problem with writing to the file.")
            print("Please check that the file is not open by another program.")
            print("-- Technical Error Message -- ")
            print(e.__doc__)
            print(e.__str__())
        continue

    # Stop the loop
    elif menu_choice == "4":
        break  # out of the loop
    else:
        print("Please only choose option 1, 2, 3, or 4")

print("Program Ended")
