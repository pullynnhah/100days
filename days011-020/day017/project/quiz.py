from data import question_data
from quiz_brain import QuizBrain
from question_model import Question

question_bank = []

for question in question_data:
    question_bank.append(Question(question['text'], question['answer']))

quiz = QuizBrain(question_bank)
quiz.next_question()
