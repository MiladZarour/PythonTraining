from user import User  # we import from the file user , the class User

app_user_one = User("nn@nn.com", "Nana Janashia",
                    "pwd1", "DecOps Engineer")
app_user_one.get_user_info()


app_user_two = User("aa@aa.com", "James Bond", "SuperSecret", "Agent")
app_user_two.get_user_info()
