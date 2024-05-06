import random

def move_one_by_one(length,group):
    while length > 0:
        length -= 1
        group = group[1:] + group[:1]
    return group

def move_firstN_to_mid(n_length,group):
    group_remain = 0
    group_remove = 0
    if n_length <= 0:
        print("Error,choose N again!")
    elif n_length < len(group):
        group_remain = group[n_length:]
        group_remove = group[:n_length]
        mid_rand_position = random.randint(1,len(group_remain)-1)
    elif n_length > len(group):
        while n_length > len(group):
            n_length -= len(group)
        group_remain = group[n_length:]
        group_remove = group[:n_length]
        mid_rand_position = random.randint(1,len(group_remain)-1)
        
    new_group = group_remain[:mid_rand_position] + group_remove + group_remain[mid_rand_position:]
    return new_group

lucky_numbers = []

for range_number in range(1,5):
    lucky_number = input("enter 4 lucky numbers between 0~15:")
    lucky_numbers.append(lucky_number)
print(lucky_numbers)

#mix randomly
random.shuffle(lucky_numbers)
#break and pile up
lucky_numbers += lucky_numbers

name_length = int(input("How long is your full name?"))
lucky_numbers = move_one_by_one(name_length,lucky_numbers)

lucky_numbers = move_firstN_to_mid(3,lucky_numbers)

luck_store = lucky_numbers.pop(0)

sec_move_mid = 0
response = input("Where are you from?(south/north/unknown)")
if response == 'south':
    sec_move_mid = 1
elif response == 'north':
    sec_move_mid = 2
elif response == 'unknown':
    sec_move_mid = 3
lucky_numbers = move_firstN_to_mid(sec_move_mid,lucky_numbers)


kick_out = 0
answer = input("What is your gender?(male/female)")
if answer == 'male':
    kick_out = 1
if answer == 'female':
    kick_out = 2
lucky_numbers = lucky_numbers[kick_out:]


print('念咒语：“见证奇迹的时刻”')
lucky_numbers = move_one_by_one(7,lucky_numbers)

while len(lucky_numbers) > 1:
    lucky_numbers = lucky_numbers[1:] + lucky_numbers[:1]
    lucky_numbers.pop(0)

lucky_numbers.append(str(luck_store))
print(lucky_numbers)
print("Congratulations! You'll have good luck!")
