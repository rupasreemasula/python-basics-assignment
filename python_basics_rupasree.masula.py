#TASKS

'''Task 1: Variables and Data Types Create variables to store a person's name (string), age (integer), height in meters (float), and whether they are a student (boolean). Print all four values in a single print() statement.'''

person_name = "Rupasree"
age = 26
height = 1.585
is_student = True

print("Name:", person_name, "Age:", age, "Height:", height, "Student:", is_student)

'''Task 2: String Formatting Using the variables from Task 1, print a sentence in the following format: Name: <name> | Age: <age> | Height: <height> | Student: <is_student>'''

print(f"Name: {person_name} | Age: {age} | Height: {height} | Student: {is_student}")

'''Task 3: Arithmetic Operations Using the age variable, calculate and print:

Age in months
Age in days (assume 365 days/year)
The remainder when age is divided by 7
Age raised to the power of 2'''

age_in_months = age * 12
age_in_days = age * 365
age_remainder_7 = age % 7
age_squared = age**2

print(f"Age in months: {age_in_months} | Age in days: {age_in_days} | The remainder when age is divided by 7: {age_remainder_7} | Age raised to the power of 2: {age_squared}")