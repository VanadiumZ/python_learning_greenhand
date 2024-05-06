pioneers=['elon','altman','albus','cauchy']
for pioneer in pioneers:
    print(pioneer)

for value in range(1,4):
    print(value)

numbers=list(range(3,9,2))
print(numbers)

squares=[]                               #etablish a blank list
for value in range(3,13):                #use "for" to circulate
    square=value**2                      #culculation
    squares.append(square)               #insert value at the END of the list
print(squares)

numbers=[1,2,3,4,5,6,7,8,8]              #value in lists could be repeated
min(numbers)
max(numbers)
sum(numbers)

squares=[value**2 for value in range(2,5)]
print(squares)


for number in range(1,21):
    print(number)

numbers=list(range(1,101))
print(numbers)

max(numbers)
min(numbers)
sum(numbers)

numbers=list(range(1,21,2))
for number in numbers:
    print(number)

numbers=[value**3 for value in range(1,11)]
print(numbers)

players=["a",'b','c','d','e','f']
for player in players[:2]:
    print(player.title())

print("The first three items in the list are:")
print(players[:3])

players.append("g")
print(players)

pizzas=['ab','cd','ef','gh']
friend_pizzas=pizzas[:]
pizzas.append("ij")
friend_pizzas.append("kl")
print("My favorite pizzas are:")
for pizza in pizzas:
    print(pizza)
print("My friend's favorite pizzas are:")
for pizza in friend_pizzas:
    print(pizza)
