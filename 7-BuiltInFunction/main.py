msg = "Hello"
print(msg)

# writing comments

print(type("this should be a string type"))
print(type(123.4))
print(type(23))

calculation_to_units = 24
name_of_unit = "hours"


def days_to_units(num_of_days):
    return (f"{num_of_days} days are {num_of_days * calculation_to_units} {name_of_unit}")


def validate_and_excute():
    try:

        user_input_number = int(num_of_days_element)  # Casting into a int
        if user_input_number > 0:
            calculated_value = days_to_units(user_input_number)
            print(calculated_value)
        elif user_input_number == 0:
            print("you entered a 0, please enter a valid positive number")
        else:
            print("you entered a negativ number, no conversion for you!")

    except ValueError:
        print("your input is not a number. Don't ruin my programe!")


user_input = ""
while user_input != "exit":
    user_input = input(
        "Hej user, enter a number of days as a comma separated list and I will convert it to hours:\n")
    list_of_days = user_input.split(", ")
    print(list_of_days)
    print(set(list_of_days))

    print(type(list_of_days))
    print(type(set(list_of_days)))

    # converting user_input to list, and with split(",") we can write 10, 30, 50
    for num_of_days_element in set(user_input.split(", ")):
        validate_and_excute()


print()  # print to the terminal
input()  # ask the user to enter
set()  # return new set
int()  # Casting to
