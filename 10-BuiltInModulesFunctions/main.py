from helper import validate_and_excute, user_input_message
import logging, os

my_os = os.name
print("my_os : ", my_os)
logger = logging.getLogger("MAIN")
logger.error("Error happened in the app")



# user_input = ""
# while user_input != "exit":
#     user_input = input(user_input_message)
#     days_and_unit = user_input.split(":")
#     print(days_and_unit)
#     days_and_unit_dictionary = {"days": days_and_unit[0],"unit": days_and_unit[1]}
#     validate_and_excute()