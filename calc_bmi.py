def get_user_data():
    """retrieves user data from the command line

    Returns:
        [dictionary] of the form:
            {
                "name" : "user_name",
                "height": "user heigth in cm",
                "weight": "user weight in kilograms"
            }
    """
    user = {}
    # user_name = str(input(("Enter your name: ")))
    # user_height = float(input(("Enter your height in meters: ")))
    # user_weight = float(input(("Enter your weight in kilograms: ")))

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

    # user["name"] = user_name
    # user["height"] = user_height
    # user["weight"] = user_weight
    
    return user

# def calc_BMI(w,h):
#     """calculates the BMI

#     Arguments:
#         w {[float]} -- [weight]
#         h {[float]} -- [height]

#     Returns:
#         [float] -- [calculated BMI = w / (h*h)]
#     """

#     calculated_BMI = float(w / (h*h))
#     return calculated_BMI
    

# def calc_BMI_category(bmi):
#     """Calculates the BMI category

#     Arguments:
#         bmi {[float]} -- [the bmi number index]

#     Returns:
#         [string] -- [bmi category]
#     """


# def print_results(bmi_category):
#     """[Prints the BMI category to the user ]

#     Arguments:
#         bmi_category {[string]} -- []
#     """
#     pass

# def cm_to_meters(cm):
#     """converts centimetres to meters

#     Arguments:
#         cm {[int]}

#     Returns:
#         [float]
#     """
#     pass

# user_data = get_user_data()
# bmi = calc_BMI(user_data["weight"],user_data["height"] )
# bmi_category = calc_BMI_category(bmi)
# print_results(bmi_category)