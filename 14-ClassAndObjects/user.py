from _typeshed import Self


class User:

    def __init__(self, email, name, passowrd, current_job_title):
        self.email = email
        self.name = name
        self.password = passowrd
        self.current_job_title = current_job_title

    def change_password(self, new_password):
        self.password = new_password

    def current_job_title(self, new_job_title):
        self.current_job_title = new_job_title
