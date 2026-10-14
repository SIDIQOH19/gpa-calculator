-GPA CALCULATOR
A command line GPA calculator using a 5-point grading scale.

-To run : python main.py

-Features
Add, view, edit, and delete courses
calculate gpa with available courses
json file to save courses

-Grading scale:
A = 5
B = 4
C = 3
D = 2
E = 1
F = 0
GPA =  sum(units * grade point) / total units

-structure:
main.py: user interaction, includes menu
storage.py: save and load files with json
calculation.py: formula for calculating
validation.py: checks units and grades

-Thought process:
I divided into four different files to make the entire code neater, easier to understand and also for easy access.
I stored each course as a dictionary with three keys which includes code, units, grade then I kept all the courses in a list and saved it to `courses.json`, sto retain the data.
The program starts with an empty list if the file does not exist yet instead of crashing.
The biggest problems I faced were synthax errors
I learned to test each file on its own before importing them to the main file.
I used an AI assistant to guide me through the structure, I wrote and tested the code myself.
