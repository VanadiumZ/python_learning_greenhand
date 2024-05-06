
#dictionary 
#here dictionary showes a map(映射)
alien_0={'color': 'green','point': 5}
print(alien_0['color'])
print(alien_0['point'])


alien_0={'color': 'green','point': 5}
alien_0['x_position']=0         #0 is a number not a str!!!
alien_0['y_position']=25
#directly add key and its value to the dictionary
print(alien_0)
#the order of key-value pairs donesn't matter

#accoding to operations above, we could firstl create a balnk dictionary

alien_0={'color': 'green','point': 5}
alien_0['color']='yellow'       #replace the value in the dictionary
print(alien_0)


alien_0={'x_position': 0,'y_position': 25,'speed': 'medium'}
print('Original_x_position:' + str(alien_0['x_position']))
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3
alien_0['x_position'] = alien_0['x_position'] + x_increment
print('New x_position: '+str(alien_0['x_position']))



alien_0={'x_position': 0,'y_position': 25,'speed': 'fast'}
print('Original_x_position:' + str(alien_0['x_position']))
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3
alien_0['x_position'] = alien_0['x_position'] + x_increment
print('New x_position: '+str(alien_0['x_position']))



alien_0={'x_position': 0,'y_position': 25,'speed': 'fast'}
del alien_0['speed']
print(alien_0)



favorite_language={
    'jen':"python",
    'sarah':'c',
    'edward':'ruby',
    'phil':'python',
    }
print("Sarah's favorite language is "+
      favorite_language['sarah'].title() +
     ".")



favorite_numbers={'albus':7,
       'cauchy':3,
       'musk':5,
       'altman':4,
       }
for person in favorite_numbers:
    print(person,":",favorite_numbers[person])


favorite_numbers={'albus':7,
       'cauchy':3,
       'musk':5,
       'altman':4,
       }
for person , favorite in favorite_numbers.items():
    print('\nperson:'+ person)
    print('number:' + str(favorite))
#still the problem: you can't put the number with the str!!!

for person in favorite_numbers:     #.keys()
    print(person.title())


favorite_numbers={'albus':7,
       'cauchy':3,
       'musk':5,
       'altman':3,
       }
for number in set(favorite_numbers.values()):
    print(str(number))
#set:delete the repeated ones

'''exercise'''


favorite_language={
    'jen':"python",
    'sarah':'c',
    'edward':'ruby',
    'phil':'python',
    }
participants=['jen','sarah','edward','phil','mike','jimmy']
for participant in  participants:
    if participant in favorite_language.keys():
        print(participant.title() + ", thank you for your participation!")
    else:
        print(participant.title() + ", please join in the survey.")


'''--------------------------------------------------------------------------------------------'''
#to control dics in bulk we could put the dics in a list
aliens=[]
for alien_number in range(30):
    new_alien={'color':'green','points':5,'speed':'slow'}
    aliens.append(new_alien)

for alien in aliens[:5]:
     print(alien)
print('...')

print("Total number of aliens is: "+ str(len(aliens)))

'''--------------------------------------------------------------------------------------------'''

users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
        },
    
    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
        },
    }
for username, user_info in users.items():
    print("\nUsername: "+ username)
    full_name = user_info['first'] + " " + user_info['last']
    location=user_info['location']

    print("\tFull name: " + full_name.title())
    print("\tLocation: " + location.title())
# nest dics in dics


'''exercises'''




favorite_places = {'albus': ['beijing','wuhan','silicon valley'],
                   'jim': ['wuhan','shanghai','nanjing'],
                   'rose': ['chongqing','chengdu','hangzhou'],
                   }
for name, places in favorite_places.items():
    print("\n" + name.title() + "'s favorite_places are:")
    for place in places:
        print("\t" + place.title())


'''---------------------------------------------------------------------------------'''







