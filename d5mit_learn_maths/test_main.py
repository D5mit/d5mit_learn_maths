from .main import Maths_Test
import pandas as pd

# create object
math_test = Maths_Test('Testing')


def test_set_questions_0():
    maths_test = Maths_Test('Some basic questions')
    assert (maths_test.get_test() == 'Some basic questions')


def test_get_questions_1():
    maths_test = Maths_Test('Some basic questions')

    # create dataframe with the questions
    questions = {'Question': ['What is 1 + 1?', 'What is 1 + 2?'],
                 'Answer': ['2', '3']}

    test_questions = pd.DataFrame(questions)

    # set questions
    maths_test.set_questions(test_questions)
    pd.testing.assert_frame_equal(maths_test.get_questions(), test_questions)


def test_ask_question_1():

    # create dataframe with the questions
    questions = {'Question': ['1 + 1 =', '1 + 2 ='],
                 'Answer': ['2', '3'],
                 'nrQuestions': [0, 3]}

    # convert to dataframe
    test_questions = pd.DataFrame(questions)

    maths_test = Maths_Test('Some basic questions', test_questions)

    assert (maths_test.ask_question() == ['1 + 2 =', '3', 3])
