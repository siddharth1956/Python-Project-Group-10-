#Problem Statement 1


# Pre-populated user data
user_data = {
    "john.doe@example.com": {"password": "john123", "first_name": "John", "last_name": "Doe", "age": 28},
    "jane.smith@example.com": {"password": "jane456", "first_name": "Jane", "last_name": "Smith", "age": 32},
    "alice.jones@example.com": {"password": "alice789", "first_name": "Alice", "last_name": "Jones", "age": 24},
    "bob.brown@example.com": {"password": "bob101", "first_name": "Bob", "last_name": "Brown", "age": 30},
    "charlie.white@example.com": {"password": "charlie202", "first_name": "Charlie", "last_name": "White", "age": 35},
    "diana.green@example.com": {"password": "diana303", "first_name": "Diana", "last_name": "Green", "age": 27},
    "evan.black@example.com": {"password": "evan404", "first_name": "Evan", "last_name": "Black", "age": 29},
    "fiona.red@example.com": {"password": "fiona505", "first_name": "Fiona", "last_name": "Red", "age": 22},
    "george.blue@example.com": {"password": "george606", "first_name": "George", "last_name": "Blue", "age": 26},
    "hannah.yellow@example.com": {"password": "hannah707", "first_name": "Hannah", "last_name": "Yellow", "age": 31}
}

def signup():
    email = input("Enter your email ID: ").lower()
    if email in user_data:
        print("Email ID already exists. Please use a different one.")
        return
    password = input("Enter your password: ")
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")
    age = input("Enter your age: ")
    
    user_data[email] = {
        "password": password,
        "first_name": first_name,
        "last_name": last_name,
        "age": int(age)
    }
    print("Registration successful!")

def signin():
    email = input("Enter your email ID: ").lower()
    password = input("Enter your password: ")
    
    if email in user_data and user_data[email]["password"] == password:
        print(f"Welcome, {user_data[email]['first_name']}!")
    else:
        print("Invalid email ID or password.")

def main():
    while True:
        print("\nMenu:\n1. Signup\n2. Sign-in\n3. Exit")
        option = input("Choose an option (1, 2, or 3): ")
        
        if option == '1':
            signup()
        elif option == '2':
            signin()
        elif option == '3':
            print("Exiting the application. Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

# Run the main function to start the program
if __name__ == "__main__":
    main()
-----------------------------------------------------------------------------------------------------------------------------------------------------------------

#Problem statement 2 

import os

def load_song_data():
    filename = input("Enter the file name to load songs: ")
    if not os.path.exists(filename):
        print(f"Error: {filename} not found.")
        return {}

    songs_db = {}
    with open(filename, 'r') as file:
        for line in file:
            try:
                # Parsing the CSV-like format
                title, artist, album, genre, duration = line.strip().split(", ")
                song_info = {
                    "Title": title.strip('"'),
                    "Album": album.strip('"'),
                    "Genre": genre.strip('"'),
                    "Duration": duration.strip('"')
                }
                
                if artist.strip('"') in songs_db:
                    songs_db[artist.strip('"')].append(song_info)
                else:
                    songs_db[artist.strip('"')] = [song_info]
                    
            except ValueError:
                print(f"Error parsing line: {line}")
                continue

    print(f"Songs loaded from {filename}.")
    return songs_db


def view_songs_database(songs_db):
    if not songs_db:
        print("Songs database is empty.")
        return

    print("Songs Database:")
    for artist, songs in songs_db.items():
        for song in songs:
            print(f"Title: {song['Title']}, Artist: {artist}, Genre: {song['Genre']}")


def delete_song(songs_db):
    artist = input("Enter the artist's name of the song to delete: ").strip()
    title = input("Enter the title of the song to delete: ").strip()

    if artist in songs_db:
        for song in songs_db[artist]:
            if song['Title'] == title:
                songs_db[artist].remove(song)
                if not songs_db[artist]:
                    del songs_db[artist]  # Remove artist if no songs are left
                print(f"Deleted '{title}' by '{artist}' from the database.")
                return
        print(f"Song '{title}' by '{artist}' not found.")
    else:
        print(f"Artist '{artist}' not found.")


def modify_song_information(songs_db):
    artist = input("Enter the artist's name of the song to modify: ").strip()
    title = input("Enter the title of the song to modify: ").strip()

    if artist in songs_db:
        for song in songs_db[artist]:
            if song['Title'] == title:
                print(f"Current details:\nTitle: {song['Title']}, Album: {song['Album']}, Genre: {song['Genre']}, Duration: {song['Duration']}")
                
                new_album = input("Enter new album (or press Enter to keep current): ").strip()
                new_genre = input("Enter new genre (or press Enter to keep current): ").strip()
                new_duration = input("Enter new duration (or press Enter to keep current): ").strip()

                if new_album:
                    song['Album'] = new_album
                if new_genre:
                    song['Genre'] = new_genre
                if new_duration:
                    song['Duration'] = new_duration

                print(f"Modified '{title}' by '{artist}'.")
                return
        print(f"Song '{title}' by '{artist}' not found.")
    else:
        print(f"Artist '{artist}' not found.")


def main():
    songs_db = {}
    while True:
        print("\nDeveloper Menu:")
        print("1. Load Song Data")
        print("2. View Songs Database")
        print("3. Delete a Song")
        print("4. Modify a Song")
        print("5. Exit")
        
        option = input("Select an option: ").strip()
        
        if option == '1':
            songs_db = load_song_data()
        elif option == '2':
            view_songs_database(songs_db)
        elif option == '3':
            delete_song(songs_db)
        elif option == '4':
            modify_song_information(songs_db)
        elif option == '5':
            print("Exiting the system.")
            break
        else:
            print("Invalid option, please try again.")


if __name__ == "__main__":
    main()

-----------------------------------------------------------------------------------------------------------------------------------------------------------------

# Problem statement 3

# Function to load song data from the file into a nested dictionary
def load_songs_data(file_path):
    songs_db = {}
    with open(file_path, 'r') as f:
        for line in f:
            # Split each line by commas to extract details
            data = line.strip().split(',')
            title = data[0].strip().lower()  # Convert to lowercase for case-insensitive search
            artist = data[1].strip()
            album = data[2].strip()
            genre = data[3].strip()
            duration = data[4].strip()

            # Store the song details in the dictionary
            songs_db[title] = {
                'artist': artist,
                'album': album,
                'genre': genre,
                'duration': duration
            }
    return songs_db

# Function to search a song by title
def search_song_by_title(songs_db, title):
    title = title.lower()  # Case-insensitive search
    if title in songs_db:
        song = songs_db[title]
        print(f"Found: '{title.title()}' by {song['artist']} (Genre: {song['genre']}, Album: {song['album']}, Duration: {song['duration']})")
    else:
        print(f"The song titled '{title.title()}' does not exist in the database.")

# Function to search all songs by an artist
def search_songs_by_artist(songs_db, artist_name):
    found_songs = [title for title, details in songs_db.items() if details['artist'].lower() == artist_name.lower()]
    if found_songs:
        print(f"Songs by {artist_name}:")
        for title in found_songs:
            song = songs_db[title]
            print(f"Found: '{title.title()}' (Album: {song['album']}, Genre: {song['genre']}, Duration: {song['duration']})")
    else:
        print(f"No songs found for artist '{artist_name}'.")

# Function to display the menu and handle user input
def display_menu(songs_db):
    while True:
        print("\n--- User Menu ---")
        print("1. Search for a Song by Title")
        print("2. Search for All Songs by an Artist")
        print("3. Exit")
        
        option = input("Select an option: ").strip()
        
        if option == '1':
            title = input("Enter the song title to search: ").strip()
            print(f"Searching for songs with title: '{title}'")
            search_song_by_title(songs_db, title)
        
        elif option == '2':
            artist_name = input("Enter the artist's name to search: ").strip()
            print(f"Searching for songs by artist: '{artist_name}'")
            search_songs_by_artist(songs_db, artist_name)
        
        elif option == '3':
            print("Exiting the Songs Management System. Goodbye!")
            break
        
        else:
            print("Invalid option. Please try again.")

# Main function to load the data and start the program
def main():
    file_path = 'songs_database.txt'
    songs_db = load_songs_data(file_path)
    display_menu(songs_db)

# Run the program
if __name__ == "__main__":
    main()
