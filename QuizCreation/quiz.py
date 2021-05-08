from question import Question
import pickle
import random


class Quiz:

    points_correct_answer = 2
    points_wrong_answer = -1

    def __init__(self, topic):
        self.topic = topic
        self.filename = topic.lower().replace(' ', '') + '.pck'
        self.number_of_questions = 0
        self.correct_answers = 0
        self.wrong_answers = 0
        self.score = 0
        self.max_score = 0

    def start(self):
        with open(self.filename, 'rb') as file:
            questions_list = pickle.load(file)
        print(f'There are {len(questions_list)} questions in the {self.topic}')
        self.number_of_questions = int(input('How many questions do you want to attempt: '))

        while self.number_of_questions > len(questions_list):
            print(f'Number of questions should be less or equal to {len(questions_list)}')
            self.number_of_questions = int(input('How many questions do you want to attempt: '))
            print()

        self.max_score = self.number_of_questions * Quiz.points_correct_answer

        random.shuffle(questions_list)

        for i in range(self.number_of_questions):
            question = questions_list[i]
            a = question.ask()
            if a is True:
                self.correct_answers += 1
            else:
                self.wrong_answers += 1

        print('.'*20, 'Quiz over', '.'*20)

    def get_result(self):
        print(f'You gave {self.correct_answers} correct answers', end=' ')
        print(f'You gave {self.wrong_answers} wrong answers', end=' ')
        self.score = self.correct_answers * Quiz.points_correct_answer + self.wrong_answers * Quiz.points_wrong_answer
        return f'{self.score}/{self.max_score}'


if __name__ == '__main__':
    quiz = Quiz('Maths')
    quiz.start()
    print(quiz.get_result())
