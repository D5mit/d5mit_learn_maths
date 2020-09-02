# imports
from main import Maths_Test
import pandas as pd


# create dataframe with the questions
questions = {'question': ['1 + 1 = ', '1 + 2 = '],
             'answer': ['2', '3'],
             'nrQuestions': [5, 6]}

# convert to dataframe
test_questions = pd.DataFrame(questions)

# create method maths_test
maths_test = Maths_Test('Sum questions', test_questions)

# ask spesific question
my_question = maths_test.ask_question()
print(my_question)

# while my_question != []:
if my_question == []:
    print('No more question left')
else:
    # read answer
    my_answer = input(my_question[0])

    if maths_test.check_answer(my_answer) == True:
        print('Correct')
    else:
        print('Incorrect')



