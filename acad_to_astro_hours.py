astronomical_hour = 60
academical_hour = 40
course_duration_in_academical_hours = 64
breaks = 20
sessions = course_duration_in_academical_hours / 4 #calculate the amount of sessions in the course
result = ((course_duration_in_academical_hours * 40) + (sessions * breaks)) / astronomical_hour # calculate the result

print(f"Total duration in astronomical hours: {result:.2f}")