class User:

    def __init__(self, email, name, passowrd, current_job_title):
        self.email = email
        self.name = name
        self.password = passowrd
        self.current_job_title = current_job_title

    def change_password(self, new_password):
        self.password = new_password

    def change_job_title(self, new_job_title):
        self.current_job_title = new_job_title

    def get_user_info(self):
        print(
            f"User {self.name} currently works as a {self.current_job_title}. You can contact them at {self.email}")


app_user_one = User("nn@nn.com", "Nana Janashia", "pwd1", "DecOps Engineer")
app_user_one.get_user_info()


app_user_two = User("aa@aa.com", "James Bond", "SuperSecret", "Agent")
app_user_two.get_user_info()
