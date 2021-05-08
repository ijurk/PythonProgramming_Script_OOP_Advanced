
from quiz import Quiz
from time import ctime

with open('quizTopics.txt', 'r') as file:
    topics = file.readlines()

name = input('Enter your name: ')
print(f'\nWelcome to the Quiz {name}!')

while True:

    print(f'You can take the quiz in any of these {len(topics)} topics:\n')
    for i in range(len(topics)):
        print(f'{i+1}. {topics[i]}', end='')

    topic_number = int(input('\nChoose topic from one of the available options: '))
    topic = topics[topic_number-1].rstrip()

    quiz = Quiz(topic)

    quiz.start()
    result = quiz.get_result()

    print(f'Your score is {result}')
    print('.' * 50)

    with open('users.txt', 'a') as file:
        file.write(f'{name},{topic},{ctime()},{result}\n')

    input(f'Press Enter to view the history of your scores in {topic}\n')
    with open('users.txt', 'r') as file:
        for line in file:
            data = line.split(',')
            if data[0] == name and data[1] == topic:
                print(f'You scored {data[3].rstrip()} on {data[2]}')

    response = input('Do you want to take the quiz again(y/n): ')
    if response.lower() == 'n':
        break
