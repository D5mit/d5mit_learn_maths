# imports
from d5mit_learn_maths import Maths_Test
import pandas as pd

# create dataframe with the questions
questions = {'question': ['1 + 1 = ', '1 + 2 = '],
             'answer': ['2', '3'],
             'nrQuestions': [1, 1]}

# convert to dataframe
test_questions = pd.DataFrame(questions)

# create method maths_test
maths_test = Maths_Test('Sum questions', test_questions)

# get first question
my_question = maths_test.ask_question()

while my_question != []:

    # while my_question != []:
    if my_question == []:
        print('No more question left')
    else:
        # read answer
        my_answer = input(my_question[0])

        if maths_test.check_answer(my_answer) == True:
            print('Correct\n')
        else:
            print('Incorrect\n')

    my_question = maths_test.ask_question()


