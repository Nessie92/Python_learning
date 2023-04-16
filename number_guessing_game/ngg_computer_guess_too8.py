import random
invalid_number_warning = "You must choose a WHOLE number."
computer_score = 0
player_score = 0
def validated_number_input(prompt, invalid_number_warning_param):
    while True:
        try:
            number = int(input(prompt)) 
            return number
        except:
            print(invalid_number_warning_param)

while True:
    high_number = validated_number_input("What is the high number?", invalid_number_warning)
    while True:
        try:
            low_number = validated_number_input("What is the low number?", invalid_number_warning)
            if low_number >= high_number:
                print("The low number cannot be higher than the high number")
            else:
                break
        except:
            print(invalid_number_warning)

    #human guesses
    computer_number = random.randint(low_number,high_number)
    human_attempts = 0
    player_guess = 0
    while True: 
        player_guess = validated_number_input("Choose a number:" if human_attempts == 0 else "Try again:", invalid_number_warning)  
        if player_guess < low_number or player_guess > high_number:
            print(f"You have to guess between {low_number} - {high_number}, choose again")
            continue
        human_attempts += 1  
        if computer_number == player_guess:
            print(f"correct, you got it in {human_attempts} attempts")
            break  
        print("too low!" if player_guess < computer_number else "too high!")      

    #ask user if ready to play
    input("Please think of a number between {} and {} and press enter when ready ".format(low_number, high_number))
    print("I'll try and guess your number. Please enter 'h' if the guess is too high, 'l' if it's too low, or 'c' if it's correct: " )
    #Computer guesses  
    computer_attempts = 0
    user_feedback = ' '
    valid_answers = ('h', 'l', 'c')
    enable_guesing = True

    while user_feedback != 'c':
        if  enable_guesing:
            computer_guess = (low_number + high_number) // 2 #computer_guess is the mid number
            print('I think it is', computer_guess, '?')
            computer_attempts += 1
            enable_guesing = False
        user_feedback = input("enter 'h', 'l', or 'c'")
        if user_feedback not in valid_answers:
            print("Invalid answer!")
            continue
        if user_feedback == 'h':
            high_number = computer_guess - 1
        elif user_feedback == 'l':
            low_number = computer_guess + 1

        if high_number < low_number:
            print("Your answers aren't logical") 
        else:
            enable_guesing = True

    print('The computer guessed your number', computer_guess, 'correctly in', computer_attempts, 'attempts.')

    #showing results

    result = f"you got it in {human_attempts} and I got it in {computer_attempts}, "
    if human_attempts < computer_attempts:
        result += "you win!"
        player_score += 1
    elif human_attempts > computer_attempts:
        result += "you lose!"
        computer_score += 1
    else:
        result += "it's a draw!"

    print(result)

    #ask player if he wants to play again
    print(f"so far you have won {player_score} and I have won {computer_score}")
    play_again = input("Do you want to play again? (y/n)")
    if play_again.lower() != "y":
        print("thanks for playing!")
        break
