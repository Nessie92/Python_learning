import json
import datetime
import os

#User Management Functions
players_directory = {}

def create_new_profile():
    while True:
        username = input("Enter a unique username for your profile: ")
        if username in players_directory:
            print(username + " is already in use. Please choose a different username")
        else:
            players_directory[username] ={
                "match history":[]
            }
            print("A profile for " + username + " created successfully.")
            return players_directory
    
score_names = ["Hole in one! ", "Eagle ", "Birdie ", "Par ", "Bogey ", "Double Bogey ", "Go Home! "]

def is_valid_number(value):
    return isinstance(value, int) or isinstance(value, float)

def color_text(text, color_name):
    color_codes = {
        "red": "31",
        "green": "32",
        "cyan": "36",
        "blue": "34",
        "yellow": "33"
    }
    return f"\033[{color_codes[color_name]}m{text}\033[0m"

def golf_score(par, strokes):
    if not is_valid_number(par) or not is_valid_number(strokes):
        return color_text("Invalid input, please enter valid numbers", "red")  
        
    if strokes == 1:
        return color_text(score_names[0], "green")  
    elif strokes <= par - 2:
        return color_text(score_names[1], "cyan")  
    elif strokes == par - 1:
        return color_text(score_names[2], "cyan")  
    elif strokes == par:
        return color_text(score_names[3], "blue")  
    elif strokes == par + 1:
        return color_text(score_names[4], "yellow")  
    elif strokes == par + 2:
        return color_text(score_names[5], "yellow")  
    elif strokes > par + 2:
        return color_text(score_names[6], "red")
    else:
        return color_text("error", "red")   
    
def save_match_data(number_of_holes, players):
    match_name = input("\n\nName this match: ")
    current_datetime = datetime.datetime.now()
    date_time_formatted = current_datetime.strftime('%Y%m%d_%H%M%S')
    filename = f"psc_{match_name}_{date_time_formatted}.json"
    
    data_to_save = {
        "match_name": match_name,
        "datetime": date_time_formatted,
        "number_of_holes": number_of_holes,
        "players": players
    }
    
    with open(filename, mode="w") as file:
        json.dump(data_to_save, file, indent=4)
    
    print("Match data saved.")

def list_previous_matches():
    match_files = [file for file in os.listdir() if file.startswith("psc_")]
    if not match_files:
        print("No previous matches found.")
        return
    print("\nPrevious Macthes: ")
    for idx, match_file in enumerate(match_files):
        match_data = match_file[:-5]
        print(f"{idx + 1}. {match_data}")

def display_match_scorecard(match_file):
    with open(match_file, "r") as file:
        match_data = json.load(file)
    
    match_name = match_data["match_name"]
    datetime = match_data["datetime"]
    number_of_holes = match_data["number_of_holes"]
    players = match_data["players"]
    
    print(f"\nScorecard for {match_name} (Date: {datetime}):")
    for player in players:
        print(f"\n{player['name']}'s scorecard:")
        print_scorecard(number_of_holes, player)
    
def print_scorecard(number_of_holes, player):
    total_strokes = sum(score[2] for score in player['scorecard'])
    total_par = sum(score[1] for score in player['scorecard'])
    final_score = total_strokes - total_par
    print(f"\n{player['name']}'s Scorecard:")
    print("Hole: ", end=" | ")
    for i in range(number_of_holes):
        print(f"{player['scorecard'][i][0]:2}", end=" | ")

    print("\nPar:  ", end=" | ")
    for i in range(number_of_holes):
        print(f"{player['scorecard'][i][1]:2}", end=" | ")

    print("\nScore:", end=" | ")
    for i in range(number_of_holes):
        print(f"{player['scorecard'][i][2]:2}", end=" | ")
    
    print(f"\n\nFinal Score: {final_score}")
    
def play_match():
    number_of_players = int(input("How many people are playing?: "))
    players = []

    for player_n in range(number_of_players):
        player_name = input(f"Enter the name of player {player_n+1}: ")
        players.append({"name": player_name, "scorecard": []})

    number_of_holes = int(input("Enter the number of holes: "))
    for hole_n in range(number_of_holes):
        par = int(input(f"Enter the par for hole {hole_n+1}: "))

        for player in players:
            strokes = int(input(f"Enter the number of strokes for {player['name']} hole {hole_n+1}: "))
            hole_score_name = golf_score(par, strokes)
            print(f"For {player['name']} hole {hole_n+1}: {hole_score_name}")
            player['scorecard'].append([hole_n+1,par,strokes])
        
    for player in players:
        print_scorecard(number_of_holes, player)
    
    save_match_data(number_of_holes, players)

while True:
    print(""" 
    Welcome, please choose an option below: 

    1. Play a match.
    2. View Previous matches.
    3. Create a new profile.
    4. Quit.""")

    choice = input("\nEnter your choice: ")
    match_files = []
    match_files = [file for file in os.listdir() if file.startswith("psc_")]
    match choice:
        case "1":
            play_match()
        case "2":
            list_previous_matches()
            selection = input("Enter the index number of the match to view: ")
            if 1 <= int(selection) <= len(match_files):
                selected_match_file = match_files[int(selection) - 1]
                display_match_scorecard(selected_match_file)
            else:
                print("Invalid selection.")
        case "3":
            create_new_profile()
            print(players_directory)
        case "4":
            print("Goodbye!")
            break