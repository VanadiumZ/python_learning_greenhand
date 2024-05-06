
#7-2
amount = input("How many people are going to have dinner?\n")
amount = int(amount)
#'int' is used to capture the numeric input
if amount > 8:
    print("Sorry, there is no available table.")
else:
    print("Please come in, there are free tables.")

#7-3
number = input("please enter a number here:\n")
number = int(number)

print("Is the number divisible by 10?")
if number %10 == 0:
    print("yes")
else:
    print("no")

#while
prompt = "\nTell me something, and I will repeat it back to you."
prompt += "\nEnter 'quit' to end the program."

message = ""
while message != 'quit':
    message = input(prompt)
    if message != 'quit':
    #to ensure that 'quit' won't be printed
        print(message)

'''add a SIGN into the program'''




prompt = "\nTell me something, and I will repeat it back to you."
prompt += "\nEnter 'quit' to end the program."

active = True
while active:
    message = input(prompt)

    if message == 'quit':
        active = False
    else:
        print(message)



#7-5 movie tickets
prompt = "\nHow old are you?"
prompt += "\nEnter 'quit' to end the program."

active = True
while active:
    answer_age = input(prompt)

    if answer_age == 'quit':
        active = False
    else:
        answer_age = int(answer_age)
        if answer_age < 3:
            print("Your ticket is free.")
        elif answer_age <= 12:
            print("You should pay 10$.")
        elif answer_age >12:
            print("You should pay 15$.")





#7-6 movie tickets variant 1
prompt = "\nHow old are you?"
prompt += "\nEnter 'quit' to end the program."

answer_age = ""
while answer_age != "quit":
    answer_age = input(prompt)
    if answer_age != 'quit':
        answer_age = int(answer_age)
        if answer_age < 3:
            print("Your ticket is free.")
        elif answer_age <= 12:
            print("You should pay 10$.")
        elif answer_age >12:
            print("You should pay 15$.")





#7-6 movie tickets variant 2
prompt = "\nHow old are you?"
prompt += "\nEnter 'quit' to end the program."

while True :
    answer_age = input(prompt)

    if answer_age == 'quit':
        break
    else:
        answer_age = int(answer_age)
        if answer_age < 3:
            print("Your ticket is free.")
        elif answer_age <= 12:
            print("You should pay 10$.")
        elif answer_age >12:
            print("You should pay 15$.")


#7.3 use "while" to process lists and dics
#7.3.1 move values between lists 
#confirmed_users

unconfirmed_users = ["albus","cauchy","elon"]
confirmed_users = []

while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    print("Verifying user:" + current_user.title())

    confirmed_users.append(current_user)

print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())


#7.3.2 delete all certain values in a list
pets = ['dog','cat','frog','horse','dog','dog','horse','eagle']
print(pets)
while 'dog' in pets:
    pets.remove('dog')
print(pets)


pets = ['dog','cat','frog','horse','dog','dog','horse','eagle']
while pets:
    #here if the circulatio comes to "cat" '.remove('dog')'
    #cannot find the value in the list=>cause error
    pets.remove('dog')
print(pets)


#fill the dics with the input from users
#establish a blank dic
responses = {}

poll_active = True

while poll_active:
    name = input("\nWhat is your name?")
    response = input("Which mountain would you like to climb someday?")
    
    responses[name] = response
    repeat = input("Would you like to let another person respond?(yes/no)")
    if repeat == 'no':
        poll_active = False

print("--- Poll Results ---")
for name, response in responses.items():
    print(name + " would like to clime " + response + ".")

#7-8 sandwich
sandwich_orders = ["Egg and Cheese Sandwich",
                   "Ham and Cheese Sandwich",
                   "Tuna Salad Sandwich",
                   "Grilled Cheese Sandwich",
                   "BLT Sandwich"]
finished_sandwiches = []

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print("I made your " + current_sandwich + ".")
    finished_sandwiches.append(current_sandwich)

print("\nThe following sandwiched have been finished:")
for finished_sandwich in finished_sandwiches:
    print(finished_sandwich)

#7-9 sandwich_pastrami
sandwich_orders = ["Egg and Cheese Sandwich",
                   'pastrami',
                   "Ham and Cheese Sandwich",
                   'pastrami',
                   "Tuna Salad Sandwich",
                   "Grilled Cheese Sandwich",
                   'pastrami',
                   "BLT Sandwich"]
print("Pastrami is sold out!")

while 'pastrami'in sandwich_orders:
    sandwich_orders.remove('pastrami')
print(sandwich_orders)

finished_sandwiches = []

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print("I made your " + current_sandwich + ".")
    finished_sandwiches.append(current_sandwich)

print("\nThe following sandwiched have been finished:")
for finished_sandwich in finished_sandwiches:
    print(finished_sandwich)
