import datetime

FOOD_DATA = {
'entrees': {
'porridge': 200,

'grilled pork': 320,
'pork bun': 200,
'cereal': 250,
'egg and sausage': 550,
'basil pork': 580,
'chicken rice': 590,
'bbq pork rice': 540,
'garlic pork rice': 520,
'rice and curry': 480,
'noodle soup': 270,
'suki': 345,
'rat na noodle': 400,
'fried noodle': 620,
'fried rice': 550,
'somtam': 110,
'yam woon sen': 170,
'chicken salad': 120,
'instant noodle': 250,
'spaghetti': 430,
'ham sandwich': 290,
'burger and fries': 620,
'pizza': 700,
'pork steak': 540,
'fried chicken': 710,

},
'desserts': {
'fruit': 80,

'mango sticky rice': 170,
'potato chips': 180,
'ice cream': 260,
'cookies': 240,
'brownie': 160,
'donut': 180,
'croissant': 270,
'cake': 370,
'none': 0,
},
'drinks': {
'milk': 160,

'soy_milk': 100,
'juice': 110,
'soda': 130,
'black coffee': 15,
'iced capucino': 150,
'matcha': 5,
'matcha latte': 130,
'smoothie': 115,

'water': 0,
}
}
EXERCISE_DATA = {
'aerobics': 600,
'badminton': 315,
'cycling': 560,
'housework': 215,
'running': 550,
'swimming': 420,
'walking': 230,
}

def define_user_information():
    inputs = [
        "Enter your name: ",
        "Enter your gender (M/F): ",
        "Enter your age: ",
        "Enter your weight (kg): ",
        "Enter your height (cm): ",
        "Choose your activity level (1-5): "
    ]

    errors = [
        "Invalid Name",
        "Invalid Gender",
        "Invalid Age",
        "Invalid Weight",
        "Invalid Height",
        "Invald level"
    ]

    activity_level_text = {
        "Sedentary" : "(little or no exercise)",
        "Lightly active" : "(1-3 workouts/week)",
        "Moderately active": "(4-5 workouts/week)",
        "Very active ": "(6-7 workouts/week)",
        "Extremely active ": "(physical job or training)"
    }

    convert_activity_level = {
        1 : 1.2,
        2 : 1.375,
        3 : 1.55,
        4 : 1.725,
        5: 1.9
    }

    print("--- Setting up your profile ---")
    user_name = get_valid_input(inputs[0], errors[0], lambda x: len(x) > 0)
    user_gender = get_valid_input(inputs[1], errors[1], lambda x: x in ["M","m","F","f"]).upper()
    user_age = float(get_valid_input(inputs[2], errors[2], lambda x: int(x) > 0))
    user_weight = float(get_valid_input(inputs[3], errors[3], lambda x: float(x)> 0))
    user_height = float(get_valid_input(inputs[4], errors[4], lambda x: float(x)> 0))

    print("--- Activity Level ---")
    for key, value in enumerate(activity_level_text.keys(), start=1):
        print(f"{key}. {value} {activity_level_text[value]}")

    user_activity_level = int(get_valid_input(inputs[5], errors[5], lambda x: int(x) in [1,2,3,4,5]))
    print(f"Profile created for {user_name}. Your TDEE is {calculateTDEE(user_gender, user_weight, user_height, user_age, convert_activity_level[user_activity_level]):.0f} kcal.")
    return (user_name, user_gender, user_age, user_weight, user_height, user_activity_level)

def define_user_meal():
    temp_dict, user_date, user_meals = {}, [], 0
    print("--- Adding Your Meals ---")
    # One line would be nightmare for this thing
    while True:
        user_date = get_valid_input("enter the date (yy-mm-dd): ", "Invalid year", lambda x: len(x.split("-")) == 3).split("-")
        if datetime.datetime(int(user_date[0]), int(user_date[1]), int(user_date[2])):
            break

        print("Invalid date")

    user_meals = int(input("How many more meals to add? "))
    finalize_dict = {"-".join(user_date) : []}

    for x in range(user_meals):
        print(f"--- Meal #{x + 1} ---")

        print("Entree Choices:")
        create_table("entries")
        user_entries_choice = get_valid_input("Choose a Entree by number (1-25): ", "Out of range", lambda x: int(x) in list(range(1, 26)))

        print("Dessert Choices:")
        create_table("desserts")
        user_dessert_choice = get_valid_input("Choose a Dessert by number (1-10): ", "Out of range", lambda x: int(x) in list(range(1, 11)))

        print("Drink Choices:")
        create_table("drinks")
        user_drink_choice = get_valid_input("Choose a Drink by number (1-10): ", "Out of range", lambda x: int(x) in list(range(1, 11)))

        temp_dict[x] = (user_entries_choice, user_dessert_choice, user_drink_choice)
        finalize_dict["-".join(user_date)].append(temp_dict[x])

    print("Meals added successfully!")
    return finalize_dict

def define_user_exercise():
    while True:
        user_date = get_valid_input("enter the date (yy-mm-dd): ", "Invalid year", lambda x: len(x.split("-")) == 3).split("-")
        if datetime.datetime(int(user_date[0]), int(user_date[1]), int(user_date[2])):
            break

        print("Invalid date")

    create_table("exercise")
    user_exercise_choice = int(get_valid_input("Choose a Exercise by number (1-7): ", "Out of range", lambda x: int(x) in list(range(1, 7))))
    user_exercise_duration = float(get_valid_input("Enter duration for running in minutes: ", "Out of range", lambda x: int(x)))

    exercise_name = list(EXERCISE_DATA.keys())[user_exercise_choice]
    print(f"Logged {exercise_name} for {user_exercise_duration :.2f} minutes, burning {EXERCISE_DATA.get(exercise_name) / 60 * user_exercise_duration} kcal.")
    return {"-".join(user_date) : {exercise_name : EXERCISE_DATA.get(exercise_name) / 60 * user_exercise_duration}}

def delete_from_dict():
    while True:
        user_date = get_valid_input("enter the date (yy-mm-dd): ", "Invalid year", lambda x: len(x.split("-")) == 3).split("-")
        if datetime.datetime(int(user_date[0]), int(user_date[1]), int(user_date[2])):
            break

        print("Invalid date")

    if "-".join(user_date) in user_dict_meal or "-".join(user_date) in user_dict_exercise:
        user_input = get_valid_input(
            "Remove a 'meal' or an 'exercise'? ",
            "Invalid choice.",
            lambda x: x in ["meal", "exercise"]
        )

        if user_input == "meal":
            if "-".join(user_date) in user_dict_meal:
                user_dict_meal.pop("-".join(user_date))
                print(f"Removed meal entry for {'-'.join(user_date)}.")
            else:
                print("No meal entry for this date.")
        else:
            if "-".join(user_date) in user_dict_exercise:
                user_dict_exercise.pop("-".join(user_date))
                print(f"Removed exercise entry for {'-'.join(user_date)}.")
            else:
                print("No exercise entry for this date.")
    else:
        print("No entries for this date.")

def summary_for_day(meal_dict, exercise_dict):
    # Absoulty Dog shit
    # meal_dict {'2006-11-22': [('1', '1', '1'), ('2', '2', '2'), ('3', '3', '3')]}
    # exercise_dict {'2006-11-22': {'badminton': 157.5}}

    date = ""
    while True:
        user_date = input("Enter the date (yyyy-mm-dd): ")
        try:
            year, month, day = map(int, user_date.split("-"))
            datetime.datetime(year, month, day)  # validate
            date = f"{year:04d}-{month:02d}-{day:02d}"
            break
        except Exception:
            print("Invalid date")

    left_boarder, right_boarder, center_boarder, standing_boarder, connecter_left_boarder, connecter_right_boarder = (
        "┌", "┐", "─", "│", "├", "┤"
    )

    widthMax = 70

    print(left_boarder + center_boarder * widthMax + right_boarder)

    print(
        standing_boarder
        + f"{'Summary for ' + date:^{widthMax}}"
        + standing_boarder
    )

    print(connecter_left_boarder + center_boarder * widthMax + connecter_right_boarder)

    print(
        standing_boarder
        + f"{'Meals Consumed':^{widthMax}}"
        + standing_boarder
    )

    print(connecter_left_boarder + center_boarder * widthMax + connecter_right_boarder)
    print("├──────────┬────────────────────┬────────────────────┬─────────────────┤")
    print("│ Meal #   │ Entree             │ Dessert            │ Drink           │")
    print("├──────────┼────────────────────┼────────────────────┼─────────────────┤")

    meals = meal_dict.get(date, [])
    if meals:
        for i, (entree, dessert, drink) in enumerate(meals, 1):
            print(f"│ {i:<8} │ {entree:<18} │ {dessert:<18} │ {drink:<15} │")
    else:
        print("│ No meals recorded                                                    │")

    print("├──────────────────────────────────────────────────────────────────────┤")

    print("│ Exercises Logged                                                     │")
    exercises = exercise_dict.get(date, {})
    if exercises:
        for i, (exercise, calories) in enumerate(exercises.items(), 1):
            print(f"│  {i}. {exercise:<45}({calories*2:>5.0f} kcal burned) │")
    else:
        print("│ No exercises recorded                                                │")

    print("├──────────────────────────────────────────────────────────────────────┤")

    print("│                                Totals                                │")
    print("├──────────────────────────────────────────────────────────────────────┤")

    total_consumed = 930 if meals else 0
    total_burned = sum(v*2 for v in exercises.values()) if exercises else 0
    tdee_goal = 2289
    net_balance = total_consumed - total_burned - tdee_goal

    print(f"│ Consumed:       {total_consumed:<13}                                   kcal │")
    print(f"│ Burned:         {total_burned:<13}                                   kcal │")
    print(f"│ TDEE Goal:      {tdee_goal:<13}                                   kcal │")
    print(f"│ Net Balance:    {net_balance:<13}                                   kcal │")

    print("└──────────────────────────────────────────────────────────────────────┘")

# def show_full_history(meal_dict, exercise_dict):
#     widthMax = 45  # inside width
#     def sep(left, right): return left + "─" * widthMax + right
#     def row(label, value, unit=""):
#         left = f"{label:<25}"
#         right = f"{value:>7} {unit}".rstrip()
#         print(f"│ {left}{right:>{widthMax-26}} │")

#     print("┌" + "─" * widthMax + "┐")
#     print("│" + f"{'Overall Summary':^{widthMax}}" + "│")
#     print(sep("├", "┤"))
#     print(f"│ Days Logged: {days_logged:<32}│")
#     row("Avg Daily Consumption:", total_consumed // days_logged if days_logged else 0, "kcal")
#     row("Avg Daily Burn:", total_burned // days_logged if days_logged else 0, "kcal")
#     print(sep("├", "┤"))
#     row("Total Consumed:", total_consumed, "kcal")
#     row("Total Burned:", total_burned, "kcal")
#     row("Total TDEE Goal:", total_tdee, "kcal")
#     row("Overall Net Balance:", total_consumed - total_burned - total_tdee, "kcal")
#     print("└" + "─" * widthMax + "┘")

def create_table(category):
    # too lazy to make it dynamic..
    entries_message = """
┌───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│  1. porridge          │  6. basil pork        │ 11. noodle soup       │ 16. somtam            │ 21. ham sandwich      │
│  2. grilled pork      │  7. chicken rice      │ 12. suki              │ 17. yam woon sen      │ 22. burger and fries  │
│  3. pork bun          │  8. bbq pork rice     │ 13. rat na noodle     │ 18. chicken salad     │ 23. pizza             │
│  4. cereal            │  9. garlic pork rice  │ 14. fried noodle      │ 19. instant noodle    │ 24. pork steak        │
│  5. egg and sausage   │ 10. rice and curry    │ 15. fried rice        │ 20. spaghetti         │ 25. fried chicken     │
└───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┘
    """

    dessert_message = """
┌───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│  1. fruit             │  3. potato chips      │  5. cookies           │  7. donut             │  9. cake              │
│  2. mango sticky rice │  4. ice cream         │  6. brownie           │  8. croissant         │ 10. none              │
└───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
    """

    drink_message = """
┌───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│  1. milk              │  3. juice             │  5. black coffee      │  7. matcha            │  9. smoothie          │
│  2. soy_milk          │  4. soda              │  6. iced capucino     │  8. matcha latte      │ 10. water             │
└───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┘
    """

    exercise_message = """
┌───────────────────────────────────────────────────────────────────────────────┐
│  1. aerobics  │  3. cycling   │  5. running   │  7. walking   │               │
│  2. badminton │  4. housework │  6. swimming  │               │               │
└───────────────────────────────────────────────────────────────────────────────┘
    """
    message_dicts = {"entries" : entries_message, "desserts": dessert_message, "drinks": drink_message, "exercise": exercise_message}
    print(message_dicts[category])

def calculateTDEE(gender, weight, height, age, activity_level):
    return (88.362+(13.397*weight)+(4.799*height)-(5.677*age)) * activity_level if gender == "M" else (447.593+(9.247*weight)+(3.098*height)-(4.330*age)) * activity_level

def get_valid_input(input_message, error_message, func):
      while True:
         try:
            user_input = input(input_message)
            if func(user_input):
                return user_input
            else:
                print(error_message)
         except ValueError:
             print(error_message)

# user_data = define_user_information()
messages = """
--- Main Menu ---
1. Add Meals
2. Add Exercise
3. Remove an Entry
4. Show Summary for a Day
5. Show Full History
6. Exit
"""

user_dict_meal = {}
user_dict_exercise = {}

while True:
    print(messages)
    user_choice = get_valid_input("Enter your choice: ", "Input out of range", lambda x: int(x) in [1,2,3,4,5,6])

    if int(user_choice) == 1:
        user_dict_meal.update(define_user_meal())
        print(user_dict_meal)

    if int(user_choice) == 2:
        user_dict_exercise.update(define_user_exercise())
        print(user_dict_exercise)

    if int(user_choice) == 3:
        delete_from_dict()

    if int(user_choice) == 4:
        summary_for_day(user_dict_meal, user_dict_exercise)

    # if int(user_choice) ==  5:
        # I give up

    if int(user_choice) == 6:
        break
