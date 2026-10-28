def get_grade_point(score):
    if score >= 70:
        return 5
    elif score >= 60:
        return 4
    elif score >= 50:
        return 3
    elif score >= 45:
        return 2
    else:
        return 0
    
while True:
    try:
        courses = int(input("How many courses did you take this semester? "))
        if courses <= 0:
            print("Please enter at least one course")
            continue
        else:
            print("You took", courses, "courses this semester.")
            break
    except ValueError:
        print("Please enter a valid number.")

scores = []
credits = []
for i in range(courses):
    while True:
        try:
            score = float(input(f"Enter score for course {i + 1}: "))
            if score < 0 or score > 100:
                print("Score must be between 0 and 100. Please try again.")
                continue
            scores.append(score)
            break
        except ValueError:
            print("That's not a valid number. Try again.")

    while True:
        try:
            credit = int(input(f"Enter credits for course {i + 1}: "))
            if credit <= 0 or credit > 5:
                print("Credits must be a positive integer between 1 and 5. Please try again.")
                continue
            credits.append(credit)
            break
        except ValueError:
            print("That's not a valid number. Try again.")

print("Your highest score is:", max(scores))
print("Your lowest score is:", min(scores))
print(f"Your average score is: {sum(scores) / len(scores):.2f}") 

total_points = 0
total_credits = 0

for i in range(courses):
    grade_point = get_grade_point(scores[i])
    total_points += grade_point * credits[i]
    total_credits += credits[i]

if total_credits > 0:
    gpa = total_points / total_credits
    print(f"Your GPA is: {gpa:.2f}")
else:
    print("No valid courses entered.")



