from validation import is_grade_valid, is_unit_valid
from calculation import calculate_gpa
from storage import save_courses, load_courses

courses = load_courses()


def menu():
    """Different options for the user to choose from."""
    print("""
    GPA CALCULATOR
    1. Add Course
    2. View Courses
    3. Edit Course
    4. Delete Course
    5. Calculate GPA
    6. Exit
    """)


def add_course():
    """Add the courses to calculate GPA"""
    course_code = input("Course code (e.g. EEG 401): ").upper()
    while course_code == "":
        print("Course code cannot be empty.")
        course_code = input("Course code: ").upper()

    course_units = input("Course units (1-6): ")
    while not is_unit_valid(course_units):
        print("Units must be a number from 1 to 6.")
        course_units = input("Course units (1-6): ")

    grade = input("Grade (A-F): ")
    while not is_grade_valid(grade):
        print('Grades must be from A to F')
        grade = input("Grade (A-F): ")

    courses.append({"code": course_code, "units": int(
        course_units), "grade": grade.upper()})
    save_courses(courses)
    print("Course added.")


def view_courses():
    """To access saved courses"""
    if len(courses) == 0:
        print('No courses added yet')
        return
    number = 1
    for course in courses:
        print(number, course['code'], course['units'], course['grade'])
        number += 1


def get_units():
    """Ask for valid course units"""
    units = input('Units (1-6): ')
    while not is_unit_valid(units):
        print('Enter a number from 1 to 6')
        units = input('Units (1-6): ')
    return int(units)


def get_grade():
    """Ask for valid grades"""
    grade = input('Grade(A-F):')
    while not is_grade_valid(grade):
        print('Enter a grade from A to F')
        grade = input('Grade(A-F):')
    return grade.upper()


def edit_course():
    """To edit a course and its details"""
    view_courses()
    if len(courses) == 0:
        return
    choice = input('Enter the number of the course to edit:')
    if choice.isdigit() and 1 <= int(choice) <= len(courses):
        course = courses[int(choice) - 1]
        course['units'] = get_units()
        course['grade'] = get_grade()
        save_courses(courses)
        print('Course details updated.')
    else:
        print('Invalid Number')


def delete_course():
    """To delete a course from the list"""
    view_courses()
    if len(courses) == 0:
        return
    choice = input('Enter the number of course to delete:')
    if choice.isdigit() and 1 <= int(choice) <= len(courses):
        removed = courses.pop(int(choice) - 1)
        save_courses(courses)
        print('Deleted', removed['code'])
    else:
        print('Invalid Number')


def calc_gpa():
    """To calculate and display the gpa"""
    if len(courses) == 0:
        print('No courses added yet')
        return
    gpa = calculate_gpa(courses)
    print('Your GPA is:', gpa)


while True:
    menu()
    choice = input("Choose an option (1-6): ")
    if choice == "1":
        add_course()
    elif choice == "2":
        view_courses()
    elif choice == '3':
        edit_course()
    elif choice == "4":
        delete_course()
    elif choice == "5":
        calc_gpa()
        input('\nPress enter to continue')
    elif choice == "6":
        print("Goodbye!")
        break
    else:
        print("Please enter a number from 1 to 6.")
