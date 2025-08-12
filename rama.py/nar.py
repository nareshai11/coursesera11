exam_scores = [55, 70, 78, 52, 68]
curve_amount = 10

# Use a list comprehension to create a new list of curved grades
curved_grades = [score + curve_amount for score in exam_scores]
print("Original scores:", exam_scores)
print("Curved scores", curved_grades)
print(exam_scores, "is  not" ,curved_grades)