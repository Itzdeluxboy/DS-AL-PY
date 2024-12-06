class User:
    def __init__(self, username, name, email):
        self.username = username
        self.name = name
        self.email = email
        print('User Created!')

    def introduce_yourself(self, cont_name):
        print("Hi {}, I'm {}! Contact me at {}".format(cont_name, self.name, self.email))

user = User('john', 'John Doe', 'john@doe.com')
print(user.name, user.username, user.email)

user2= User('jane' , "Jane Doe", "jane@doe.com")
User.introduce_yourself(user2,'David')
