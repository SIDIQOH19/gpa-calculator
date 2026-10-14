import json


def save_courses(courses, filename='courses.json'):
    """To save the list of courses into a json file"""
    with open(filename, 'w') as file:
        json.dump(courses, file, indent=4)


def load_courses(filename='courses.json'):
    """To load the list of courses from the json file"""
    try:
        with open(filename, 'r') as file:
            return json.load(file)
    except (FileNotFoundError, ValueError):
        return []
