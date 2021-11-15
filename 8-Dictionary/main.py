calculation_to_units = 24
name_of_unit = "hours"


def days_to_units(num_of_days):
    return (f"{num_of_days} days are {num_of_days * calculation_to_units} {name_of_unit}")


def validate_and_excute():
    try:

        user_input_number = int(days_and_unit_dictionary["days"])  
        if user_input_number > 0:
            calculated_value = days_to_units(user_input_number)
            print(calculated_value)
        elif user_input_number == 0:
            print("you entered a 0, please enter a valid positive number")
        else:
            print("you entered a negativ number, no conversion for you!")

    except ValueError:
        print("your input is not a number. Don't ruin my programe!")


# user_input = ""
# while user_input != "exit":
#     user_input = input("Hej user, enter a number of days and conversion unity:\n")
#     days_and_unit = user_input.split(":")
#     print(days_and_unit)
#     days_and_unit_dictionary = {"days": days_and_unit[0],"unit": days_and_unit[1]}
#     print(days_and_unit_dictionary)
#     validate_and_excute()


my_list = ["20", "30", "100"]
print(my_list[1])
print(my_list[2])

my_dictionary = {"days" : 20, "unit":"hours", "message": "all good"}
print(my_dictionary["days"])
print(my_dictionary["unit"])
print(my_dictionary["message"])