import datetime

user_input = input("enter your goal with a deadline separated by colon\n")
input_list = user_input.split(":")
print(input_list)
goal = input_list[0]
deadline = input_list[1]

deadline_date = datetime.datetime.strptime(deadline, "%d.%m.%Y") #30.12.2021
# calculate how many days from now till deadline

today_date = datetime.datetime.today()
print("deadline_date",deadline_date)
print("today_date",today_date)
print("deadline_date - today_date = ",deadline_date - today_date)

