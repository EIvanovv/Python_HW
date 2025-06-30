user_height = float(input("Please enter your height in meters:"))
user_weight = int(input("Please enter your weight in kilograms:"))
bmi = user_weight / (user_height * user_height)

print(f"{round(bmi, 2)}")