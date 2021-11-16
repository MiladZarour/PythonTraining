import user  # we import the file name (be careful)

app_user_one = user.User("nn@nn.com", "Nana Janashia",
                         "pwd1", "DecOps Engineer")
app_user_one.get_user_info()


app_user_two = user.User("aa@aa.com", "James Bond", "SuperSecret", "Agent")
app_user_two.get_user_info()
