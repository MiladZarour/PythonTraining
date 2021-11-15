my_set = {"January", "February", "March"}
for element in my_set:
    print(element)

my_set.add("April")  # added an element to the set
print(my_set)
my_set.remove("January")
print(my_set)


my_list = ["January", "February", "March", "January"]
my_list.remove("January")
print(my_list)
