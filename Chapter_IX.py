class Dog():

    def __init__(self, name, age):
#attention: "__init__" has two "_" at both ends
        self.name = name
        self.age = age

    def sit(self):
        print(self.name.title() + " is now sitting.")

    def roll_over(self):
        print(self.name.title() + " rolled over!")

my_dog = Dog('will',2)
my_dog.sit()

#9-3
class User():
    def __init__(self,f,l,a,la):
        self.first_name = f
        self.last_name = l
        self.age = a
        self.login_attempts = la

    def describe_user(self):
        full_name = self.first_name.title() +"." +  self.last_name.title()
        user_info = []
        user_info.append(full_name)
        user_info.append(self.age)
        print(user_info)

    def greet_user(self):
        full_name = self.first_name.title() +"."  + self.last_name.title()
        print("Hello, " + full_name + "!")

    def increment_login_attempts(self):
        self.login_attempts += 1
        print(self.login_attempts)

    def reset_login_attempts(self):
        self.login_attempts = 0
        print(self.login_attempts)

#user_a = User('albus','z',19,3)
#user_b = User('cauchy','c',19,4)
#user_a.increment_login_attempts()
#user_a.increment_login_attempts()
#user_a.increment_login_attempts()
#user_b.reset_login_attempts()


class Admin(User):
    
    def __init__(self,f,l,a,la,pr):
        User.__init__(self,f,l,a,la)
        self.privileges = pr
        pr = ['can add post','can delete post','can ban user']

    def show_priviledges(self):
        print(self.priviledges)

user_c = Admin('alan','turin',10,0)
user_c.show_priviledges()
        