import helper as h

user_input = ""
while user_input != "exit":
    user_input = input(h.user_input_message)
    days_and_unit = user_input.split(":")
    print(days_and_unit)
    days_and_unit_dictionary = {"days": days_and_unit[0],"unit": days_and_unit[1]}
    h.validate_and_excute()