# imports
from main import Maths_Test
import numpy as np
import pandas as pd

# create dataframe with the questions
questions = {'Question': ['What is 1 + 1?', 'What is 1 + 2?'],
             'Answer': ['2', '3'],
             'nrQuestions': [0, 3]}

# convert to dataframe
test_questions = pd.DataFrame(questions)

maths_test = Maths_Test('Some basic questions', test_questions)

my_question = maths_test.ask_question()

print(list(my_question))

print(my_question[2])