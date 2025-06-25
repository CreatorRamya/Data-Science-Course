import numpy as np

data_type = [('name', 'S15'), ('class', int), ('height', float)]
students_details = [('Sarah', 5, 49), ('Joshua', 6, 51.5), ('Alexandra', 5, 43), ('Karl', 6, 46)]

students = np.array(students_details, dtype=data_type)
print("Orginal Info:")
print(students)
print("Sorted by height")
print(np.sort(students, order='height'))
