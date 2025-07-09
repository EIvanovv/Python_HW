student_scores = {
    "Ivan": 5.00,
    "Alex": 3.50,
    "Maria": 5.50,
    "Georgy": 5.00
}

highest_score = max(student_scores.values())
highest_score_key = max(student_scores, key=student_scores.get)

lowest_score = min(student_scores.values())
lowest_score_key = min(student_scores, key=student_scores.get)

print(f"{highest_score_key} - {highest_score}")
print(f"{lowest_score_key} - {lowest_score}")