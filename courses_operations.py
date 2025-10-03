import json

def add_course_data(): 
    courses_data = []

    with open("courses_data.json", "r") as courses_file:
        courses_data = json.load(courses_file)

    course_name = input("Enter the course name: ")
    course_code = input("Enter the course code: ")
    credit_hours = float(input("Enter the course credit hours: "))
    credit_hour_price = float(input("Enter the course credit hour price: "))

    new_course = {
        "course_name": course_name, 
        "course_code": course_code,
        "credit_hours": credit_hours,
        "credit_hour_price": credit_hour_price 
    }

    courses_data.append(new_course)

    with open("courses_data.json", "w") as courses_file:
        json.dump(courses_data, courses_file, indent=3)

def update_course_data(): 
    courses_data = []
    with open("courses_data.json", "r") as courses_file:
        courses_data = json.load(courses_file)
    
    course_name = input("Enter the course name you want to update: ")
    course_code = input("Enter the course code you want to update: ")
    
    for course in courses_data: 
        if (course["course_name"].lower() == course_name.lower()) and (course["course_code"] == course_code): 
            
            new_name = input("Enter the new course name: ")
            new_code = input("Enter the new course code: ")
            new_credit_hours = float(input("Enter the new course credit hours: "))
            new_credit_hour_price = float(input("Enter the new course credit hour price: "))
            
            course["course_name"] = new_name
            course["course_code"] = new_code
            course["credit_hours"] = new_credit_hours
            course["credit_hour_price"] = new_credit_hour_price
            
            with open("courses_data.json", "w") as courses_file:
                json.dump(courses_data, courses_file, indent=3)
            break

def delete_course_data(): 
    courses_data = []
    with open("courses_data.json", "r") as courses_file:
        courses_data = json.load(courses_file)
    
    course_name = input("Enter the course name you want to delete: ")
    course_code = input("Enter the course code you want to delete: ")
    
    courses_data = [course for course in courses_data if not (course["course_name"].lower() == course_name.lower() and course["course_code"] == course_code)]
    
    with open("courses_data.json", "w") as courses_file:
        json.dump(courses_data, courses_file, indent=3)

def search_in_course_data():
    courses_data = []
    with open("courses_data.json", "r") as courses_file:
        courses_data = json.load(courses_file)
    
    search_option = input("Do you want to search by:\n 1. Course name\n 2. Course code\n: ")
    
    if search_option == "1": 
        course_name = input("Enter the course name you want to search for: ")
        
        print("\n========== Course Data ==========")
        for course in courses_data: 
            if course_name.lower() == course["course_name"].lower(): 
                for key, value in course.items(): 
                    print(f"{key}: {value}")
                print("\n")
                break
    elif search_option == "2": 
        course_code = input("Enter the course code you want to search for: ")
        
        print("\n========== Course Data ==========")
        for course in courses_data: 
            if course_code == course["course_code"]: 
                for key, value in course.items(): 
                    print(f"{key}: {value}")
                print("\n")
                break
    else: 
        print("\nInvalid option.")

def show_all_courses(): 
    courses_data = []
    with open("courses_data.json", "r") as courses_file:
        courses_data = json.load(courses_file)
    
    print("\n========== All Courses ==========")
    for index, course in enumerate(courses_data, start=1): 
        print(f"Course {index}:")
        for key, value in course.items(): 
            print(f"  {key}: {value}")
        print("\n")
