#if...:
#   xxxxxx
#else:
#   xxxxxx

car="audi"
print(car=="audi")

age_1=2
age_2=3
print(age_1>=2 and age_2<4)

alien_color='red'
if alien_color=='red':
    print("You got 5 points.")
    
alien_color='red'
if alien_color=='green':
    print("You got 5 points.")

age=19
if age<2:
    print('He is a infant.')
elif age>=2 and age<4:
    print('He is learning how to walk.')
elif age>=4 and age<13:
    print('He is a child.')
elif age>=13 and age<20:
    print("He is a teenager.")
elif age>=20 and age<65:
    print("He is an adult.")
else:
    print("He is an old man. ")

users=["q"]
for user in users:
    if user==None:
        print("We need to find some users!")
    if user=="admin":
        print("Hello admin,would you like to see a status report?")
    else:
        print("Hello "+user+",thank you for logging in again")



current_users=["Ab",'BD','C','D','E']
new_users=["AB",'Bd','G','H','I']
current_users_lower=[]
for current_user in current_users:
    current_users_lower.append(current_user.lower())

for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print("You need to choose another username.")
    else:
        print("This name hasn't been used.")




current_users=["Ab",'BD','C','D','E']
new_users=["AB",'Bd','G','H','I']
for current_user in current_users:
    for new_user in new_users:
        if new_user.lower()==current_user.lower():
            print("Enter another name.")
        else:
            print("This name hasn't been used.")
            #the result is false,for 5*5 circultion

'''
revise, below
'''

current_users=["Ab",'BD','C','D','E']
new_users=["AB",'Bd','G','H','I']
for new_user in new_users:
    #examine the objective(the two "for")here means initially pick out new_user
    for current_user in current_users:
        if new_user.lower()==current_user.lower():
            print("Enter another name.")
            break
        #mind the retract of "break"
    else:                           
        #mind the retract of "else"
        print("This name hasn't been used.")

'''------------------------------------------------------------'''

numbers=[str(i) for i in range(1,11)]
for i in numbers:
    if i=='1':
        print(i+"st")
    elif i=='2':
        print(i+"nd")
    elif i=='3':
        print(i+"rd")
    else:
        print(i+"th")
#mind the type of the statistics

