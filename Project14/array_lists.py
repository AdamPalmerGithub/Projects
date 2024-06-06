'''A program to store and organize albums using classes and lists.'''

class Album:
    def __init__(self, album_name, number_of_songs, album_artist):   #Album class, with attributes for name, num of songs and artist 
        self.album_name = album_name
        self.number_of_songs = number_of_songs
        self.album_artist = album_artist

    def __str__(self):
        return f"({self.album_name}, {self.number_of_songs}, {self.album_artist})"     #string method to allow printing of items that use the class
    
    # define intiger?

albums1 = []    #empty list to be appended to 

albums1.append(Album("Rock", 12, "James"))
albums1.append(Album("Pop", 9, "Charlotte"))
albums1.append(Album("Rap", 15, "Daisy"))
albums1.append(Album("Techno", 8, "Stevo"))
albums1.append(Album("Classic", 13, "Dave"))  

print("The list of albums: ")           #lists the albums using a for loop
for album in albums1:
    print(album)

albums1_age_sort = sorted(albums1, key=lambda album: album.number_of_songs)   #sorts the albums by number of songs 

print("\nThe albums in order of songs: ")   #prints the new list
for album in albums1_age_sort:
    print(album)

albums1[1], albums1[2] = albums1[2], albums1[1]   #swaps the order of items at index 1 and 2

print("\nSwapping the items at 1 and 2")   #prints new list
for album in albums1:
    print(album)

albums2 = []   #empty list to be appended to

albums2.append(Album("Now 88", 18, "Sean"))
albums2.append(Album("R&B", 6, "Emma"))
albums2.append(Album("Jazz", 5, "Noah"))
albums2.append(Album("Country", 11, "Ava"))
albums2.append(Album("Hip hop", 13, "Mia"))  

print("\nThe albums in list 2: ")   #prints the new list
for album in albums2:
    print(album)

albums2.extend(albums1)   #combines the album1 into album2

print("\nAdding the items from albums1 to albums2")  #prints the combined lists
for album in albums2:
    print(album)

albums2.append(Album("Dark Side of the Moon", 9, "Pink Floyd"))      #adds two more albums to the list
albums2.append(Album("Oops!... I Did It Again", 16, "Britney Spears"))

print("\nAdding two new albums:")
for album in albums2:
    print(album)

albums2 = sorted(albums2, key=lambda album: album.album_name.lower())    #sorts the list by album name 

print("\nThe albums sorted alphabetically: ")         #prints the newly organised list
for album in albums2:
    print(album)

album_to_find = "Dark Side of the Moon"                      #sets the wanted album to a variable
for index, album in enumerate(albums2):            #use enumerate to find the index while looping through the list
    if album.album_name == album_to_find:                    #if the album is found returns its index, else returns not found
        print(f"{album_to_find} is at index: {index}")
        break
else:
    print("Album not found")