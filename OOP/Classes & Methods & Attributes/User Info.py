class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email

    def PrintUserInfo(self):
        print(f"User Name: {self.username}\nUser email: {self.email}")

user1 = User("Makochino", "alexandrniger@gmail.com")
user1.PrintUserInfo()