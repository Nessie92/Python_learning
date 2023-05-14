import csv
film_list = []

def add_film_to_list():
    film = input("Enter the name of a film: ")
    film_list.append({"film": film, "Status": "Unwatched", "rating": "-"}) 
    print("film added to list")

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
    film_score = input("give the film a score from 0 (the lowest) to 10 (the highest), if unsure mark as '-' for now: ")
    film_list[film_index]["Status"] = "Watched"
    film_list[film_index]["rating"] = film_score
    print("film marked as watched and score given")

def edit_score():
    view_film_list("All")
    film_index = int(input("Enter the index of the film you wish to change the score"))
    new_score = input("give the film a score from 0 (the lowest) to 10 (the highest)")
    film_list[film_index]["rating"] = new_score
    print("film score edited")


def view_film_list(film_list_type):

    print("\n" + film_list_type + " Films")
    
    for i, film in enumerate(film_list):
        if  film_list_type is "All" or film["Status"] == film_list_type:
            print(f"{i}. {film['film']} - {film['Status']} - {film['rating']}")

def save_film_list():
    with open('film_list.csv', mode='w', newline='') as file:
        my_writer = csv.writer(file, delimiter='\t')
        for film in film_list:
            my_writer.writerow([film['film'], film['Status'], film['rating']])
    print("Film list saved.")


def load_film_list():
    try:
        with open('film_list.csv', mode='r') as file:
            reader = csv.reader(file, delimiter='\t')
            for row in reader:
                film_list.append({'film': row[0], 'Status': row[1], 'rating': row[2]})
        print("Film list loaded.")
    except FileNotFoundError:
        print("No saved film list found.")

#save as a file, using tab as delimiter
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
10. quit''')

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

