#Chapter VIII function 

def greet_user(username):
    #username is a 形参
#'def' here means define a fuction name 
    print("Hello, " + username.title() + "!")

greet_user('albus')
#albus 是实参

#function + 'while' circulation
#greet.py
def get_formatted_name(first_name,last_name):
    full_name = first_name + " " + last_name
    return full_name.title()

while True:
    print("\nPlease tell me your name:")
    print("(enter 'q' at any time to quit)")
    
    f_name = input("First name:")
    if f_name == 'q':
        break

    l_name = input("Last name:")
    if l_name == 'q':
        break

    formatted_name = get_formatted_name(f_name,l_name)
    print("Hello," + formatted_name +"!")
    #here last two lines of codes should be led by while 
    #so focus on the retraction

#8-6 city_name
def city_country(cityname,country):
    print('"'+cityname+ ',' +country+'"')
city_country('Beijing','China')


#8-7&8-8 albums
def make_album(album_name,artist,track_amount = ''):
    if track_amount:
        albums = {'name':album_name,'artist':artist,'tracks':track_amount}
    else:
        albums = {'name':album_name,'artist':artist}
    return albums

while True:
    print("\nPlease tell your favorite album and its artist:")
    print("(enter 'q' at any time to quit.")

    album_name = input("album name:")
    if album_name == 'q':
        break
    
    artist = input("artist:")
    if artist == 'q':
        break
 
dic = make_album(album_name,artist,track_amount = '')
print("Here is a dic of albums:\n" + dic)


#8-8 
def get_album_dic(album_name,artist,track_number = ''):
    album_dic = {'album':album_name,'artist':artist}
    if track_number:
        album_dic["track"] = track_number
    return album_dic

while True:
    print("\nPlease enter an album name and its artist:")
    print("(enter 'q' at any time to quit)")

    album = input("Album name:")
    if album == 'q':
        break

    artist = input("Artist:")
    if artist == 'q':
        break

    answer = input("Can you provide the track number?(yes/no)")
    if answer == "yes":
        tracks = input("Track_number:")
        if tracks == "q":
            break
    elif answer == 'no':
        albums_dic = get_album_dic(album,artist)
        print(albums_dic)
        continue

    albums_dic = get_album_dic(album,artist,int(tracks))
    print(albums_dic)

#8-8 revise 
def get_album_dic(album_name,artist,track_number = ''):
    album_dic = {'album':album_name,'artist':artist}
    if track_number:
        album_dic["track"] = track_number
    return album_dic

while True:
    print("\nPlease enter an album name and its artist:")
    print("(enter 'q' at any time to quit)")
    tracks = 0
    #here we define tracks in advance so that we can access to the value of tracks outside 'if'
    album = input("Album name:")
    if album == 'q':
        break

    artist = input("Artist:")
    if artist == 'q':
        break

    answer = input("Can you provide the track number?(yes/no)")
    if answer == "yes":
        tracks = input("Track number:")
        if answer == 'q':
            break
    album_dic = get_album_dic(album,artist,int(tracks))
    print(album_dic)



#8-14
def make_car(p, m, **car_info):
    car = {}
    car["producer"] = p
    car["model"] = m
    for key, value in car_info.items():
        car[key] = value
    return car

car = make_car('subaru','outback',color='blue', tow_package=True)
print(car)


