msg = "Hello"
print(msg)

print(type("this should be a string type"))
print(type(123.4))
print(type(23))

calculation_to_units = 24
name_of_unit = "hours"


def days_to_units(num_of_days):
    return (f"{num_of_days} days are {num_of_days * calculation_to_units} {name_of_unit}")


def validate_and_excute():
    try:

        user_input_number = int(user_input)  # Casting into a int
        if user_input_number > 0:
            calculated_value = days_to_units(user_input_number)
            print(calculated_value)
        elif user_input_number == 0:
            print("you entered a 0, please enter a valid positive number")
        else:
            print("you entered a negativ number, no conversion for you!")

    except:
        print("your input is not a number. Don't ruin my programe!")


user_input = ""
while user_input != "exit":
    user_input = input(
        "Hej user, enter a number of days and I will convert it to hours: ")
    validate_and_excute()
