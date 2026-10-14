GRADE_POINT = {'A': 5, 'B': 4, 'C': 3, 'D': 2, 'E': 1, 'F': 0}


def calculate_gpa(courses):
    """To calculate the gpa with the courses inputed"""
    total_units = 0
    total_points = 0
    for course in courses:
        total_units += course['units']
        total_points += course['units'] * GRADE_POINT[course['grade']]
    if total_units == 0:
        return 0.0
    return round(total_points/total_units, 2)
