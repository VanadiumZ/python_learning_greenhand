import json

username = input("What is your name?")
filename = 'username.json'

with open(filename,'w') as f_obj:
    json.dump(username,f_obj)
    
#remember
file_name = 'username.json'

with open(filename) as f_obj:
    username = json.load(f_obj)
    
print("welcome back," + username + "!")


#mix together
filename = 'username.json'
try:
    with open(filename) as f_obj:
        username = json.load(f_obj)
except FileNotFoundError:
    username = input("What is your name?")
    with open(filename,'w') as f_obj:
        json.dump(username,f_obj)
        print("We'll remember you when you come back, " + username + "!")
else:
    print("Welcome back, " + username + "!")
    


#reconstruct
import json

def get_stored_username():
    filename = "username.json"
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return username
    
def get_new_username():
    username = input("What is your name?")
    filename = 'username.json'
    with open(filename) as f_obj:
        json.dump(username,f_obj)
    return username

def greet_user():
    username = get_stored_username()
    if username:
        print(username)
        answer = input("Is this your username?(yes/no)")
        if answer == 'yes':
            print("Welcome back, " + username)
        elif answer == 'no':
            username = get_new_username()
            print("We'll remember you when you come back, " + username
                  + "!")
    else:
        username = get_new_username()
        print("We'll remember you when you come back, " + username
                  + "!")
greet_user()

    
        