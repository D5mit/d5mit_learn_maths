from .main import Maths_Test
import pandas as pd


def test_set_questions_0():
    """
        Test that a test can be created
    """
    maths_test = Maths_Test('Some basic questions')
    assert (maths_test.get_test() == 'Some basic questions')


def test_get_questions_0():
    """
        Test that questions can be set and questions can be retrieved
    """
    maths_test = Maths_Test('Some basic questions')

    # create dataframe with the questions
    questions = {'Question': ['What is 1 + 1?', 'What is 1 + 2?'],
                 'Answer': ['2', '3']}

    test_questions = pd.DataFrame(questions)

    # set questions
    maths_test.set_questions(test_questions)
    pd.testing.assert_frame_equal(maths_test.get_questions(), test_questions)


def test_ask_question_0():
    """
        test that questions can be set and then one question can be asked
    """
    # create dataframe with the questions
    questions = {'question': ['1 + 1 =', '1 + 2 ='],
                 'answer': ['2', '3'],
                 'nrQuestions': [0, 3]}

    # convert to dataframe
    test_questions = pd.DataFrame(questions)

    maths_test = Maths_Test('Some basic questions', test_questions)

    assert (maths_test.ask_question() == ['1 + 2 =', '3', 3])


def test_ask_question_1():
    """
        test that no questions are asked and it still works
    """
    # create dataframe with the questions
    questions = {'question': ['1 + 1 =', '1 + 2 ='],
                 'answer': ['2', '3'],
                 'nrQuestions': [0, 0]}

    # convert to dataframe
    test_questions = pd.DataFrame(questions)

    maths_test = Maths_Test('Some basic questions', test_questions)

    assert (maths_test.ask_question() == [])


def test_check_answer_0():
    """
        Check if question is asked that correct answer is flagged as True
    """
    # create dataframe with the questions
    questions = {'question': ['1 + 1 = ', '1 + 2 = '],
                 'answer': ['2', '3'],
                 'nrQuestions': [0, 1]}

    # convert to dataframe
    test_questions = pd.DataFrame(questions)

    # create method maths_test
    maths_test = Maths_Test('Sum questions', test_questions)

    # ask spesific question
    maths_test.ask_question()

    assert (maths_test.check_answer('3') == True)


def test_check_answer_1():
    """
        Check if question is asked that incorrect answer is flagged as False
    """
    # create dataframe with the questions
    questions = {'question': ['1 + 1 = ', '1 + 2 = '],
                 'answer': ['2', '3'],
                 'nrQuestions': [0, 1]}

    # convert to dataframe
    test_questions = pd.DataFrame(questions)

    # create method maths_test
    maths_test = Maths_Test('Sum questions', test_questions)

    # ask spesific question
    maths_test.ask_question()

    assert (maths_test.check_answer('5') == False)
