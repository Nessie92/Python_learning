import csv
import json
import requests


users = []

''' 
 Data structure: Film List program
 This program features a list of users, each user is a dictionary containing username, password and films. 
 Films is a list of dictionaries containing a film with its details.

 Example structure:
 
USERS = [ # list of users
            { # user 1 dictionary
                "username": "JohnD",
                "password": "123",
                "films":
                [ # list of films
                    { # film dictionary
                        'film': 'Film 1', # The name of the film (string)
                        'Released': '2021', # The release date of the film (string)
                        'Status': 'Unwatched', # The status of the film (string)
                        'rating': '-', # The rating of the film (string)
                        'genre': 'Action', # The genre of the film (string)
                        'imdb_rating': '7.5', # The IMDb rating of the film (string)
                        'description': 'Description of Film 1', # The description of the film (string)
                        'actors': 'Actor 1, Actor 2', # The actors in the film (string)
                        'director': 'Director 1' # The director of the film (string)
                    },
                    {
                        'film': 'Film 2',
                        'Released': '2020',
                        'Status': 'Watched',
                        'rating': '8',
                        'genre': 'Drama',
                        'imdb_rating': '8.2',
                        'description': 'Description of Film 2',
                        'actors': 'Actor 3, Actor 4',
                        'director': 'Director 2'
                    }
                ] # end of film list
            }, # end user 1
            { # user 2 dictionary
                "username": "JohnD",
                "password": "123",
                "films":
                [ # list of films
                    { # film dictionary
                        'film': 'Film 1',
                        'Released': '2021',
                        'Status': 'Unwatched',
                        'rating': '-',
                        'genre': 'Action',
                        'imdb_rating': '7.5',
                        'description': 'Description of Film 1',
                        'actors': 'Actor 1, Actor 2',
                        'director': 'Director 1'
                    },
                    {
                        'film': 'Film 2',
                        'Released': '2020',
                        'Status': 'Watched',
                        'rating': '8',
                        'genre': 'Drama',
                        'imdb_rating': '8.2',
                        'description': 'Description of Film 2',
                        'actors': 'Actor 3, Actor 4',
                        'director': 'Director 2'
                    }
                ] # end of film list
            } # end user 2
]
print(USERS [0]["films"][0]["actors"])
'''

#User Management 
def view_user_info(user):
    print(f'''user Information \n
          Username: {user['username']} \n
          Password: {user['password']}''')
    
def find_user(username):
    for user in users:
        if user["username"] == username:
            return user
    return None

def create_new_user(username, password):
    user = {
        "username": username,
        "film_list": [],
        "password": password,
    }
    users.append(user)
    print("New user created")
    return user


def save_users_as_json():
    filename = "users.json"
    with open(filename, mode='w') as file:
        json.dump(users, file)
    print('Users list saved as JSON.')

def load_users_from_json():
    filename = "users.json"
    try:
        with open(filename, mode='r') as file:
            loaded_users = json.load(file)
            users.extend(loaded_users)
        print("Users list loaded from JSON.")
    except FileNotFoundError:
        print("No saved users list found.")

def update_password(user):
    current_password = input("Enter your current password: ")
    if current_password == user['password']:
        new_password = input("Enter your new password: ")
        user['password'] = new_password
        print("Password updated successfully.")
    else:
        print("Incorrect password. Password update failed.")

#Film List Management

def add_film_to_list(user):
    film = input("Enter the name of a film: ")
    film_info = get_film_info(film)
    if film_info is not None:
        user["film_list"].append(film_info)
        print("Film added to list")
    else:
        print("Failed to retrieve film information")
    
def get_film_info(film):
    api_key = "4213cac3"
    url = f"http://www.omdbapi.com/?apikey={api_key}&t={film}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        film_info = {
            "film": data.get("Title", ""),
            "Released": data.get("Released", ""),
            "Status": "Unwatched",
            "rating": "-",
            "genre": data.get("Genre", ""),
            "imdb_rating": data.get("imdbRating", ""),
            "description": data.get("Plot", ""),
            "actors": data.get("Actors", ""),
            "director": data.get("Director", ""),
        }
        return film_info
    else:
        return None

def edit_film_list(user):
    view_film_list(user, "All")
    film_index = int(input("Enter the index of the film you wish to edit: "))               
    new_film = input("Enter the new film name: ")
    user["film_list"][film_index]["film"] = new_film
    print("Film edited")

def delete_film(user):
    view_film_list(user, "All")
    film_index = int(input("Enter the index of the film you wish to delete: "))  
    del user["film_list"][film_index]
    print("Film deleted") 

def mark_film_watched(user):
    view_film_list(user, "All")
    film_index = int(input("Enter the index of the film you wish to mark as watched: "))
    rate_film(user)
    print("Film marked as watched, and score added.")

def edit_score(user):
    view_film_list(user, "All")
    film_index = int(input("Enter the index of the film you wish to change the score"))
    new_score = input("give the film a score from 0 (the lowest) to 10 (the highest)")
    user["film_list"][film_index]["rating"] = new_score
    print("Film score edited")

def rate_film(user):
    film_index = int(input("Enter the index of the film you wish to rate: "))
    film_rating = {
        "story": 0,
        "characters": 0,
        "special effects": 0,
        "acting": 0,
        "overall": 0,
        "comments": ""
    }

    keys_to_rate = ["story", "characters", "special effects", "acting"]

    for key in keys_to_rate:
        rating = int(input(f"From 0 - 10, how would you rate {key}?: "))
        film_rating[key] = rating

    overall_rating = sum(film_rating[key] for key in keys_to_rate) / len(keys_to_rate)
    film_rating["overall"] = overall_rating

    comment = input("Enter your review comments: ")
    film_rating["comments"] = comment

    user["film_list"][film_index]["rating"] = film_rating

def view_film_list(user, film_list_type):
    print("\n" + film_list_type + " Films")

    for i, film in enumerate(user["film_list"]):
        if film_list_type == "All" or film["Status"] == film_list_type:
            print(f"{i}. Film: {film['film']}")
            print(f"   Released: {film['Released']}")
            print(f"   Status: {film['Status']}")
            print(f"   Rating: {film['rating']}")
            print(f"   Genre: {film['genre']}")
            print(f"   IMDB Rating: {film['imdb_rating']}")
            print(f"   Description: {film['description']}")
            print(f"   Actors: {film['actors']}")
            print(f"   Director: {film['director']}")

def delete_all_films(user):
    user["film_list"] = []
    print("All films deleted from the list.")

#File Operations

def save_film_list_as_csv(user):
    filename = f"{user['username']}_film_list.csv"
    with open(filename, mode='w', newline='') as file:
        my_writer = csv.writer(file, delimiter='\t')
        for film in user["film_list"]:
            my_writer.writerow([film['film'], film['Status'], film['rating']])
    print("Film list saved as CSV")

def save_film_list_as_json(user):
    save_users_as_json()
    filename = f"{user['username']}_film_list.json"
    with open(filename, mode='w') as file:
        json.dump(user["film_list"], file)
    print('Film List saved as JSON.')
    

def save_film_list(user):
    save_option = input("Save film as CSV (C) or JSON (J)?").upper()
    if save_option == "C":
        save_film_list_as_csv(user)
    elif save_option == "J":
        save_film_list_as_json(user)
    else:
        print("Invalid option, please enter either (C) or (J)")

def load_film_list():
    load_users_from_json()
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    user = find_user(username)

    if user:
        if user["password"] == password:
            try:
                load_option = input("Load film list from CSV (C) or JSON (J)? ").upper()
                if load_option == 'C':
                    load_list_from_csv(user)
                elif load_option == 'J':
                    load_list_from_json(user)
                else:
                    print("Invalid option. No film list loaded.")
            except FileNotFoundError:
                print("No saved film list found.")
        else:
            print("Incorrect password. Access denied.")
            return None
    else:
        password_confirm = input("Create a password for your account: ")
        user = create_new_user(username, password_confirm)
    return user

def load_list_from_csv(user):
    filename = f"{user['username']}_film_list.csv"
    with open(filename, mode='r') as file:
        reader = csv.reader(file, delimiter='\t')
        user["film_list"] = [
            {
                'film': row[0],
                'Status': row[1],
                'rating': row[2],
            }
            for row in reader
        ]
    print("Film list loaded from CSV.")

def load_list_from_json(user):
    filename = f"{user['username']}_film_list.json"
    with open(filename, mode='r') as file:
        user["film_list"] = json.load(file)
    print("Film list loaded from JSON.")

#Main Interface

user = load_film_list()
while True:
    print('''\nFilm List Menu 
1. Add film to list 
2. Edit film in list 
3. Delete film from list 
4. Mark film as watched 
5. Edit film rating 
6. View all list 
7. View unwatched film list 
8. View watched film list 
9. Save list
10. Delete all film list
11. View user information
12. Change password
13. Quit''')

    choice = input("Enter your choice: ")

    match choice:
        case "1":
            add_film_to_list(user)
            
        case "2":
            edit_film_list(user)
            
        case "3":
            delete_film(user)
            
        case "4":
            mark_film_watched(user)
            
        case "5":
            edit_score(user)
            
        case "6":
            view_film_list(user, "All")
            
        case "7":
            view_film_list(user, "Unwatched")
            
        case "8":
            view_film_list(user, "Watched")

        case "9":
            save_film_list(user)

        case "10":
            delete_all_films(user)  

        case "11":
            view_user_info(user) 

        case "12":
            update_password(user)
             
        case "13":
            want_save = input("Do you want to save your changes? (y/n)")
            if want_save.lower() == "y":
                save_film_list(user)
            print("Goodbye!")
            break

        case _:
            print("Invalid choice, please try again!")
