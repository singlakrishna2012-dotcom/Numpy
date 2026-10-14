import numpy as np

dt = [('name', 'S15'), ('age', int), ('height', float)]
d = [('James', 7, 66.3), ('krishna', 13, 45), ('Charles', 23, 59)]

students = np.array(d, dtype=dt)

print("Orignal Array :")
print(students)
print("Sorted Array: ")
print(np.sort(students, order='height'))
