from helper import validate_and_excute

user_input = ""
while user_input != "exit":
    user_input = input("Hej user, enter a number of days and conversion unity:\n")
    days_and_unit = user_input.split(":")
    print(days_and_unit)
    days_and_unit_dictionary = {"days": days_and_unit[0],"unit": days_and_unit[1]}
    print(days_and_unit_dictionary)
    print(type(days_and_unit_dictionary))
    validate_and_excute()











# message = "enter some value" #that is string
# days = 20
# price = 9.99
# valid_number = True
# exit_input = False
# list_of_days = [20,40,20,100] # it's ok to duplicate values
# list_of_month = ["January", "Febraury", "June"]

# set_of_dats = [20, 45, 100] # doesn't allow duplicate values
# my_dictionary = {"days" : 20, "unit":"hours", "message": "all good"}


# my_list = ["20", "30", "100"]
# print(my_list[1])
# print(my_list[2])

# my_dictionary = {"days" : 20, "unit":"hours", "message": "all good"}
# print(my_dictionary["days"])
# print(my_dictionary["unit"])
# print(my_dictionary["message"])