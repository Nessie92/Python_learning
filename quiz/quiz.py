import requests
from random import shuffle
import html #import html for decoding html entities

#remake by storing index number instead of text in correct answer key

questions = []
score = 0

def get_q_a():
    questions_internal = []
    difficulty = input("Choose your difficulty: Easy, Medium, Hard:\n ").lower()
    url = f"http://opentdb.com/api.php?amount=50&category=9&difficulty={difficulty}&type=multiple"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

        for question_data in data['results']:
            question = html.unescape(question_data['question'])  # Decode HTML entities
            correct_answer = html.unescape(question_data['correct_answer'])  # Decode HTML entities
            incorrect_answers = [html.unescape(answer) for answer in question_data['incorrect_answers']]  # Decode HTML entities


            answers = incorrect_answers + [correct_answer]            
            shuffle(answers)
            correct_answer_index = answers.index(correct_answer)

            q_a_dic = {
                'Question': question,
                'Answers': answers,
                'Correct Answer': correct_answer,
                'Correct Answer Index': correct_answer_index
            }

            questions_internal.append(q_a_dic)
        return questions_internal
    else:
        print("Failed to fetch questions.")

def is_answer_correct(user_answer, correct_answer_index):
    try:
        user_answer_index = int(user_answer) -1 #error indexing starts from 0
        return user_answer_index == correct_answer_index
    except ValueError:
        print("Bad answer!")
        return False

def receive_answers(questions, score):
    
    for idx_q, question in enumerate(questions, start=1):
        print(f"Question {idx_q}: {question['Question']}")
        print("Answers:")
        for idx_a, answer in enumerate(question['Answers'], start=1):
            print(f"  {idx_a}. {answer}")
        print("\nScore:",score)

        user_answer = input("\nEnter the index of your answer: ")
        
        if is_answer_correct(user_answer, question['Correct Answer Index']):
            print("Correct!\n") #place the function .index(question['Correct Answer']) after shuffle
            score += 1
        else:
            print(f"Wrong! The correct answer is: {question['Correct Answer']}\n")
    return score


def game():
    questions = get_q_a()
    score = 0
    print("\nGame Over!\nYour Final score is:", receive_answers(questions, score))

while True:
    print('''
1. Play Quiz
2. Quit
    ''')
    player_choice = input("\nSelect the index of what you want to do: ")
    match player_choice:
        case '1':
            game()
        case '2':
            print('Goodbye!')
            break

