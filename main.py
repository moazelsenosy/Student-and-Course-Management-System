### Refactored: Main Page.py ###
import json
import students_operations as student_ops
import courses_operations as course_ops

# Authentication status selection
authentication_option = input("Choose an option:\n 1. Login\n 2. Signup\n: ")
selected_main_option = ""

if authentication_option == "1":
    username = input("Enter the username: ")
    password = input("Enter the password: ")

    if username == "admin" and password == "12345":
        selected_main_option = input("Select option:\n 1. Students operations\n 2. Courses operations\n: ")

        if selected_main_option == "1":
            student_operation_choice = input("\n 1. Add students\n 2. Update students\n 3. Delete students\n 4. Show all students\n 5. Search students\n 6. Display enrolled student courses\n 7. Calculate GPA\n: ")
            
            if student_operation_choice == "1":
                student_ops.add_student_data()
            elif student_operation_choice == "2":
                student_ops.update_student_data()
            elif student_operation_choice == "3":
                student_ops.delete_student_data()
            elif student_operation_choice == "4":
                student_ops.show_all_students()
            elif student_operation_choice == "5":
                student_ops.search_in_students_data()
            elif student_operation_choice == "6":
                student_ops.display_student_courses()
            elif student_operation_choice == "7":
                gpas = input("Enter the GPAs separated by a comma: ").split(",")
                credit_hours = input("Enter the credit hours separated by a comma: ").split(",")
                gpa_values = [float(gpa) for gpa in gpas]
                credit_hour_values = [float(ch) for ch in credit_hours]
                student_ops.calculate_gpa(gpa_values, credit_hour_values)
            else:
                print("Invalid option.")
        
        elif selected_main_option == "2":
            course_operation_choice = input("\n 1. Add courses\n 2. Update course\n 3. Delete course\n 4. Show all courses\n 5. Search courses\n: ")
            
            if course_operation_choice == "1":
                course_ops.add_course_data()
            elif course_operation_choice == "2":
                course_ops.update_course_data()
            elif course_operation_choice == "3":
                course_ops.delete_course_data()
            elif course_operation_choice == "4":
                course_ops.show_all_courses()
            elif course_operation_choice == "5":
                course_ops.search_in_course_data()
            else:
                print("Invalid operation number.")
    
    else:
        with open("system_users.json", "r") as user_file:
            user_data = json.load(user_file)

        user_found = False
        for user in user_data:
            if user["user_name"] == username and user["user_password"] == password:
                user_found = True
                selected_main_option = input("Select option:\n 1. Students operations\n 2. Courses operations\n: ")

                if selected_main_option == "1":
                    student_operation_choice = input("\n 1. Add students\n 2. Display student courses\n 3. Search students\n 4. Show all students\n 5. Calculate GPA\n: ")
                    
                    if student_operation_choice == "1":
                        student_ops.add_student_data()
                    elif student_operation_choice == "2":
                        student_ops.display_student_courses()
                    elif student_operation_choice == "3":
                        student_ops.search_in_students_data()
                    elif student_operation_choice == "4":
                        student_ops.show_all_students()
                    elif student_operation_choice == "5":
                        gpas = input("Enter the GPAs separated by a comma: ").split(",")
                        credit_hours = input("Enter the credit hours separated by a comma: ").split(",")
                        gpa_values = [float(gpa) for gpa in gpas]
                        credit_hour_values = [float(ch) for ch in credit_hours]
                        student_ops.calculate_gpa(gpa_values, credit_hour_values)
                    else:
                        print("Invalid option.")

                elif selected_main_option == "2":
                    course_operation_choice = input("\n 1. Add courses\n 2. Show all courses\n 3. Search courses\n: ")
                    
                    if course_operation_choice == "1":
                        course_ops.add_course_data()
                    elif course_operation_choice == "2":
                        course_ops.show_all_courses()
                    elif course_operation_choice == "3":
                        course_ops.search_in_course_data()
                    else:
                        print("Invalid option.")
                else:
                    print("Invalid username or password.")
        
        if not user_found:
            print("Invalid username or password.")

elif authentication_option == "2":
    new_username = input("Enter the username: ")
    new_password = input("Enter the password: ")
    
    with open("system_users.json", "r") as user_file:
        user_data = json.load(user_file)

    new_user = {"user_name": new_username, "user_password": new_password}
    user_data.append(new_user)

    with open("system_users.json", "w") as user_file:
        json.dump(user_data, user_file, indent=3)

    print("User has been added.")

else:
    print("Invalid option.")
