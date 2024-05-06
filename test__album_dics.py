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

