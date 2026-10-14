# To check if grade is between A-F and unit is between 1 and 6
GRADES = ['A', 'B', 'C', 'D', 'E', 'F']
UNITS = ['1', '2', '3', '4', '5', '6']


def is_grade_valid(grade):
    """To check if the grade inputed is between A and F"""
    return grade.upper() in GRADES


def is_unit_valid(units):
    """To check if the unit inputed is between 1 and 6"""
    return units in UNITS
