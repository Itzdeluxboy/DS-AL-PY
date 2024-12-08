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
    def __init__(self):
        self.users=[]

    def insert(self,user):
        i = 0
        while i < len(self.users):
            if self.users[i].username > user.username:
                break
            i +=1
            self.users.insert(i,user)

    def find(self, username):
        for user in self.users:
            if user.username == username:
                return user
    def update(self,user):
        target = self.find(user.username)
        target.name, target.email = user.name, user.emal
    def list_all(self):
        return self.users
