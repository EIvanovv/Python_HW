def get_user_data():
    """retrieves user data from the command line

    Returns:
        [dictionary] of the form:
            {
                "name" : "user_name",
                "height": "user heigth in meters",
                "weight": "user weight in kilograms"
            }
    """
    user = {}


    def validate_name_input():
        while True:
            user_name = input(("Enter your name (at least 2 characters long): "))
            if len(user_name) >= 2:
                user["name"] = user_name
                break

    def validate_height_input():
        while True:
            user_height = float(input(("Enter your height in cm (must be between 50 and 250): ")))
            if user_height in range(50,251):
                user["height"] = user_height
                break
    
    def validate_weight_input():
        while True:
            user_weight = int(input(("Enter your weight in kg (must be between 5 and 300): ")))
            if user_weight in range(5,301):
                user["weight"] = user_weight
                break
                    
    validate_name_input()
    validate_height_input()
    validate_weight_input()
    

    return user

def calc_BMI(w,h):
    """calculates the BMI

    Arguments:
        w {[float]} -- [weight]
        h {[float]} -- [height]

    Returns:
        [float] -- [calculated BMI = w / (h*h)]
    """
    
    calculated_BMI = float(w / (h*h))

    return calculated_BMI
    

def calc_BMI_category(bmi):
    """Calculates the BMI category

    Arguments:
        bmi {[float]} -- [the bmi number index]

    Returns:
        [string] -- [bmi category]
    """
    category = [" Underweight (Severe thinness)", "Underweight (Moderate thinness)", "Underweight (Mild thinness)", "Normal range", "Overweight (Pre-obese)", "Obese (Class I)", "Obese (Class II)", "Obese (Class III)"]

    if bmi <=16.0:
        return {category[0]}
    elif bmi >=16.0 and bmi<17:
        return {category[1]}
    elif bmi >=17.0 and bmi<18.5:
        return {category[2]}
    elif bmi >=18.5 and bmi<24.9:
        return {category[3]}
    elif bmi >=25.0 and bmi<30:
        return {category[4]}
    elif bmi >=30.0 and bmi<35:
        return {category[5]}
    elif bmi >=35.0 and bmi<40:
        return {category[6]}
    else:
        return {category[7]}

def print_results(bmi_category):
    """[Prints the BMI category to the user ]

    Arguments:
        bmi_category {[string]} -- []
    """
    print(f"{bmi_category}")

# def cm_to_meters(cm):
#     """converts centimetres to meters

#     Arguments:
#         cm {[int]}

#     Returns:
#         [float]
#     """
#     return cm / 100

user_data = get_user_data()
bmi = calc_BMI(user_data["weight"],user_data["height"] )
bmi_category = calc_BMI_category(bmi)
print_results(bmi_category)