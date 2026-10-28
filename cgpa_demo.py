grade_points = [5, 4, 3]
credits = [3, 2, 4]

total_points = 0
total_credits = 0

for i in range(len(grade_points)):
    total_points += grade_points[i] * credits[i]
    total_credits += credits[i]

cgpa = total_points / total_credits
print(f"CGPA: {cgpa:.2f}")