from random import randint
player_choices = ["Rock", "Paper", "Scissors"]

continue_playing = True
you_lose_txt = "haha, you lose! "
you_win_txt = "winner winner chicken dinner " 
Rock_win = "Rock smashes Scissors!"
Paper_win = "Paper covers Rock!"
Scissors_win = "Scissors shreds Paper!"
Player_score = 0
computer_score = 0 
while continue_playing == True:
    computer_choice = player_choices[randint(0,2)]
    print(f"Player {Player_score}, {computer_score} Computer")
    human_input = input("Please enter your choice: Rock, Paper, Scissors? ")
    print("Computer choice is:", computer_choice)
    if human_input == computer_choice:    print("it's a draw!")

    elif human_input == "Rock"     and computer_choice == "Paper":    print(you_lose_txt + Paper_win); computer_score +=1
    elif human_input == "Paper"    and computer_choice == "Scissors": print(you_lose_txt + Scissors_win); computer_score +=1
    elif human_input == "Scissors" and computer_choice == "Rock":     print(you_lose_txt + Rock_win); computer_score +=1
    elif human_input == "Rock"     and computer_choice == "Scissors": print(you_win_txt  + Rock_win); Player_score +=1
    elif human_input == "Paper"    and computer_choice == "Rock":     print(you_win_txt  + Paper_win); Player_score +=1
    elif human_input == "Scissors" and computer_choice == "Paper":    print(you_win_txt  + Scissors_win); Player_score +=1

    else:   print("WTF! you can't do that! check your spelling, moron!") 

continue_playing = True

