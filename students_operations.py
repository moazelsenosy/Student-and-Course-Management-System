import json

def add_student_data():
    student_records = []

    with open("student_data.json", "r") as student_file:
        student_records = json.load(student_file)

    student_name = input("Enter the student name: ")
    student_id = input("Enter the student ID: ")
    student_gpa = float(input("Enter the student GPA: "))
    enrolled_course_name = input("Enter the course name you want to enroll in: ")

    new_student = {
        "student_name": student_name,
        "student_id": student_id,
        "student_gpa": student_gpa,
        "enrolled_course_name": enrolled_course_name
    }

    student_records.append(new_student)

    with open("student_data.json", "w") as student_file:
        json.dump(student_records, student_file, indent=3)

def update_student_data():
    student_records = []
    with open("student_data.json", "r") as student_file:
        student_records = json.load(student_file)

    search_name = input("Enter the student name you want to update: ")
    search_id = input("Enter the student ID you want to update: ")

    for student in student_records:
        if (student["student_name"].lower() == search_name.lower()) and (student["student_id"] == search_id):
            updated_name = input("Enter the new student name: ")
            updated_id = input("Enter the new student ID: ")
            updated_gpa = float(input("Enter the new student GPA: "))
            updated_course = input("Enter the new enrolled course: ")

            student["student_name"] = updated_name
            student["student_id"] = updated_id
            student["student_gpa"] = updated_gpa
            student["enrolled_course_name"] = updated_course

    with open("student_data.json", "w") as student_file:
        json.dump(student_records, student_file, indent=3)

def delete_student_data():
    student_records = []
    with open("student_data.json", "r") as student_file:
        student_records = json.load(student_file)

    delete_name = input("Enter the student name you want to delete: ")
    delete_id = input("Enter the student ID you want to delete: ")

    for student in student_records:
        if delete_name.lower() == student["student_name"].lower() and student["student_id"] == delete_id:
            student_records.remove(student)

    with open("student_data.json", "w") as student_file:
        json.dump(student_records, student_file, indent=3)

def search_in_students_data():
    student_records = []
    with open("student_data.json", "r") as student_file:
        student_records = json.load(student_file)

    search_option = input("Do you want to search by:\n 1. Name\n 2. ID: ")

    if search_option == "1":
        search_name = input("Enter the student name you want to search for: ")

        print("\n=============================== Student Data ===============================\n")
        for student in student_records:
            if search_name.lower() == student["student_name"].lower():
                for key, value in student.items():
                    print(f"{key}: {value}\n")

    elif search_option == "2":
        search_id = input("Enter the student ID you want to search for: ")

        print("\n=============================== Student Data ===============================\n")
        for student in student_records:
            if search_id == student["student_id"]:
                for key, value in student.items():
                    print(f"{key}: {value}\n")
    else:
        print("\nInvalid option entered.")

def show_all_students():
    student_records = []
    with open("student_data.json", "r") as student_file:
        student_records = json.load(student_file)

    for student in student_records:
        for key, value in student.items():
            print(f"\n{key}: {value}")

def display_student_courses():
    with open("student_data.json", "r") as student_file:
        student_records = json.load(student_file)

    with open("courses_data.json", "r") as course_file:
        course_records = json.load(course_file)

    for student in student_records:
        student_name = student["student_name"]
        enrolled_course_name = student["enrolled_course_name"]

        print(f"Student Name: {student_name}")
        print("Enrolled Courses:")

        course = next((c for c in course_records if c["course_name"] == enrolled_course_name), None)
        if course:
            course_name = course["course_name"]
            course_code = course["course_code"]
            course_credit_hours = course["course_credit_hours"]
            print(f"- {course_name} - {course_code} - {course_credit_hours}")
        else:
            print("No courses found.")

        print("\n" + "-" * 40 + "\n")

def calculate_gpa_for_student(gpa_list, credit_hour_list):
    total_points = 0
    for i in range(len(gpa_list)):
        total_points += float(gpa_list[i]) * float(credit_hour_list[i])
    cumulative_gpa = total_points / sum(credit_hour_list)
    return cumulative_gpa

def calculate_gpa(gpa_list, credit_hour_list):
    student_cumulative_gpa = calculate_gpa_for_student(gpa_list, credit_hour_list)
    print(round(student_cumulative_gpa, 2))
