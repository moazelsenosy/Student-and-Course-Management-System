# Student and Course Management System (Console-based)

## Description
A simple console-based Python project for managing students and courses.  
The system allows administrators and users to:
- Add, update, delete, and search for students and courses.
- Display all students and courses.
- Enroll students in courses.
- Calculate GPA for students.
- Authentication system (Admin / User login & signup).

This project is designed for practice in Python programming, JSON file handling, and basic system operations.

## Features
### Student Operations
- Add new students.
- Update student data.
- Delete student records.
- Show all students.
- Search for students by name or ID.
- Display student enrolled courses.
- GPA calculation.

### Course Operations
- Add new courses.
- Update course data.
- Delete course records.
- Show all courses.
- Search for courses by name or code.

### Authentication
- Admin login (default: username = `admin`, password = `12345`).
- Normal user login (from `system_users.json`).
- User signup with username and password.

## Project Structure
Student-and-Course-Management-System/  
│── main.py                  # Main entry point  
│── students_operations.py   # All student-related functions  
│── courses_operations.py    # All course-related functions  
│── student_data.json        # Stores students information  
│── courses_data.json        # Stores courses information  
│── system_users.json        # Stores users (for login/signup)  
│── README.md                # Project documentation  

## How to Run
1. Clone the repository:
   ```bash
   git clone https://github.com/moazelsenosy/Student-and-Course-Management-System.git
