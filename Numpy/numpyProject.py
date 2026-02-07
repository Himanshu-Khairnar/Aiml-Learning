import numpy as np

attendance = np.array([
    [1, 1, 1, 0, 1, 1, 1, 1],  
    [1, 0, 0, 1, 0, 1, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1],
    [0, 0, 1, 0, 1, 0, 0, 1],
    [1, 1, 0, 1, 1, 1, 0, 1]
])

total_days = attendance.shape[1]

attendance_percentage = (attendance.sum(axis=1) / total_days) * 100

defaulters = attendance_percentage < 75

best_student = np.argmax(attendance_percentage)
worst_student = np.argmin(attendance_percentage)

print("Attendance Percentage:", attendance_percentage)
print("Defaulters (Below 75%):", defaulters)
print("Best Attendance Student Index:", best_student)
print("Worst Attendance Student Index:", worst_student)
