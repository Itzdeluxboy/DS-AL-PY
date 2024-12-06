class User:
    def __init__(self, username, name, email):
        self.username = username
        self.name = name
        self.email = email
        print('User Created!')

    def introduce_yourself(self, cont_name):
        print("Hi {}, I'm {}! Contact me at {}".format(cont_name, self.name, self.email))


    def __repr__(self):
        return "User(username='{}', name='{}', email='{}')".format(self.username, self.name, self.email)

    def __str__(self):
        return self.__repr__()

user = User('john', 'John Doe', 'john@doe.com')

user2= User('jane' , "Jane Doe", "jane@doe.com")

print(user,user2)



class UserDatabase:
    def insert(self,user):
        pass
    def find(self, username):
        pass
    def update(self,user):
        pass
    def list_all(self):
        pass
    