import csv
import json
import requests
film_list = []

def add_film_to_list():
    film = input("Enter the name of a film: ")
    film_info = get_film_info(film)
    if film_info:
        film_list.append(film_info)
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

def edit_film_list():
    view_film_list("All")
    film_index = int(input("Enter the index of the film you wish to edit: "))               
    new_film = input("Enter the new film name: ")
    film_list[film_index]["film"] = new_film
    print("film edited")

def delete_film():
    view_film_list("All")
    film_index = int(input("Enter the index of the film you wish to delete: "))  
    del film_list[film_index]
    print("film deleted") 

def mark_film_watched():
    view_film_list("All")
    film_index = int(input("Enter the index of the film you wish to mark as watched: "))
    film_score = input("Give the film a score from 0 (the lowest) to 10 (the highest). If unsure, mark as '-' for now: ")
    film_list[film_index]["Status"] = "Watched"
    film_list[film_index]["rating"] = film_score
    print("Film marked as watched, and score added.")

def edit_score():
    view_film_list("All")
    film_index = int(input("Enter the index of the film you wish to change the score"))
    new_score = input("give the film a score from 0 (the lowest) to 10 (the highest)")
    film_list[film_index]["rating"] = new_score
    print("film score edited")

def view_film_list(film_list_type):
    print("\n" + film_list_type + " Films")

    for i, film in enumerate(film_list):
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

def save_film_list_as_csv():
    with open('film_list.csv', mode='w', newline='') as file:
        my_writer = csv.writer(file, delimiter='\t')
        for film in film_list:
            my_writer.writerow([film['film'], film['Status'], film['rating']])
    print("Film list saved as CSV")

def save_film_list_as_json():
    with open('film_list.json', mode='w') as file:
        json.dump(film_list, file)
    print('Film List saved as JSON.')

def save_film_list():
    save_option = input("Save film as CSV (C) or JSON (J)?").upper()
    if save_option == "C":
        save_film_list_as_csv()
    elif save_option == "J":
        save_film_list_as_json()
    else:
        print("invalid option, please enter either (C) or (J)")

def load_film_list():
    try:
        load_option = input("Load film list from CSV (C) or JSON (J)? ").upper()
        if load_option == 'C':
            with open('film_list.csv', mode='r') as file:
                reader = csv.reader(file, delimiter='\t')
                for row in reader:
                    film_list.append({
                        'film': row[0],
                        'Status': row[1],
                        'rating': row[2],
                    })
            print("Film list loaded from CSV.")
        elif load_option == 'J':
            with open('film_list.json', mode='r') as file:
                film_list.extend(json.load(file))
            print("Film list loaded from JSON.")
        else:
            print("Invalid option. No film list loaded.")
    except FileNotFoundError:
        print("No saved film list found.")

def delete_all_films():
    global film_list
    film_list = []
    print("All films deleted from the list.")

load_film_list()
while True:

    print('''\nFilm List Menu 
1. add film to list 
2. edit film in list 
3. delete film from list 
4. mark film as watched 
5. edit film rating 
6. view all list 
7. view unwatched film list 
8. view watched film list 
9. save list
10. delete all film list
11. quit''')

    choice = input("enter your choice: ")

    match choice:
        case "1":
            add_film_to_list()
            
        case "2":
            edit_film_list()
            
        case "3":
            delete_film()
            
        case "4":
            mark_film_watched()
            
        case "5":
            edit_score()
            
        case "6":
            view_film_list("All")
            
        case "7":
            view_film_list("Unwatched")
            
        case "8":
            view_film_list("Watched")

        case "9":
            save_film_list()

        case "10":
            delete_all_films()   
             
        case "11":
            want_save = input("Do you to save your changes? (y/n)")
            if want_save.lower() == "y":
                save_film_list()
                print("Goodbye!")
                break
            else:
                print("Goodbye!")
                break
            
        case _:
            print("invalid choice, please try again!")