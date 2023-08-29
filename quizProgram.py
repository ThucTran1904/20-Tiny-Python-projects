quiz = {
    "question1":  {
        'question': 'What is the capital of France',
        'answer': 'Paris',
    },
    "question2": {
        'question': 'What is the capital of Germany',
        'answer': 'Berlin',
    },
    "question3": {
        'question': 'What is the capital of Italy',
        'answer': 'Rome',
    },
    "question4": {
        'question': 'What is the capital of Spain',
        'answer': 'Madrid',
    },
    "question5": {
        'question': 'What is the capital of Portugal',
        'answer': 'Lisbon',
    },
    "question6": {
        'question': 'What is the capital of Switzerland',
        'answer': 'Bern',
    },
    "question7 ": {
        'question': 'What is the capital of Australia',
        'answer': 'Canberra',
    },
}

score = 0
questionNumber = 0

for key, value in quiz.items():
    lengthKey = len(key)
    print('')
    print(value['question'])
    yourAnswer = input('Type your answer here: ')
    if yourAnswer.lower() == value['answer'].lower():
        print('Correct')
        score += 1
    else:
        print('I bitterly to say that you are not correct yet')
        print('The correct answer must be : '+ value['answer'])
        print('Your current score is: ' + str(score))

    if (score == 7):
        print('Congratulations!!! You deserve to have 10 girlfriends')
        print('Your percentage is ' + str(round(int(score)/7) * 100) + '%')


