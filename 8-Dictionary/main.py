def days_to_units(num_of_days, conversion_unit):
    if conversion_unit == "hours":
        return (f"{num_of_days} days are {num_of_days * 24} hours")
    elif conversion_unit == "minutes":
        return (f"{num_of_days} days are {num_of_days * 24 * 60} minutes")
    else:
        return "unsupported unit"

def validate_and_excute():
    try:

        user_input_number = int(days_and_unit_dictionary["days"])  
        if user_input_number > 0:
            calculated_value = days_to_units(user_input_number, days_and_unit_dictionary["unit"])
            print(calculated_value)
        elif user_input_number == 0:
            print("you entered a 0, please enter a valid positive number")
        else:
            print("you entered a negativ number, no conversion for you!")

    except ValueError:
        print("your input is not a number. Don't ruin my programe!")


user_input = ""
while user_input != "exit":
    user_input = input("Hej user, enter a number of days and conversion unity:\n")
    days_and_unit = user_input.split(":")
    print(days_and_unit)
    days_and_unit_dictionary = {"days": days_and_unit[0],"unit": days_and_unit[1]}
    print(days_and_unit_dictionary)
    print(type(days_and_unit_dictionary))
    validate_and_excute()



message = "enter some value" #that is string
days = 20
price = 9.99
valid_number = True
exit_input = False
list_of_days = [20,40,20,100] # it's ok to duplicate values
list_of_month = ["January", "Febraury", "June"]

set_of_dats = [20, 45, 100] # doesn't allow duplicate values
my_dictionary = {"days" : 20, "unit":"hours", "message": "all good"}


# my_list = ["20", "30", "100"]
# print(my_list[1])
# print(my_list[2])

# my_dictionary = {"days" : 20, "unit":"hours", "message": "all good"}
# print(my_dictionary["days"])
# print(my_dictionary["unit"])
# print(my_dictionary["message"])