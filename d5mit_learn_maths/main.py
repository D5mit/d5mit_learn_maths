class Maths_Test:
    """ Maths Test class.  This class is the actual math test that is being presented to a person to write.

    Parameters:
    description (string): Description of the test that is being written
    start_time  #toDo
    end_Time    #toDo
    questions (DF)
        question (str) -  The question
        answer (str) - The correct answer of the question
        nrQuestions -  How many times to ask the question
        How many times question answered correctly    #toDo
        How many times question answered incorrectly  #toDo
    person    #toDo
    question_index
    """

    def __init__(self, description, questions=[], questionIndex=0):
        self.description = description
        self.questions = questions
        self.questionIndex = questionIndex

    def get_test(self):
        return self.description

    def set_questions(self, questions):
        self.questions = questions

    def get_questions(self):
        return self.questions

    def ask_question(self):
        import numpy as np

        # test_questions = self.questions
        test_questions = self.questions

        # get the total number of questions, note the program can ask the same question more than once
        nrOfQuest = np.sum(test_questions['nrQuestions'])

        if nrOfQuest > 0:
            # calculate percentage of each question, this is something like [0.5 0.5]
            questLeft_ratio_array = test_questions['nrQuestions'] / nrOfQuest

            # choose one question randomly and assign a higher prob to this question
            questLeft_ratio_multi_array = np.random.multinomial(1, list(questLeft_ratio_array))

            # choose one question to ask
            questionIndex = np.argmax(questLeft_ratio_multi_array)
            self.questionIndex = questionIndex

            return list(test_questions.iloc[questionIndex])

        else:
            return list([])

    def get_question_index(self):
        return self.questionIndex

    def check_answer(self, answer):
        question_index = self.questionIndex
        my_answer = answer

        iquestions_df = self.questions

        if my_answer == iquestions_df.iloc[question_index]['answer']:
            iquestions_df.at[question_index, 'nrQuestions'] = iquestions_df.iloc[question_index]['nrQuestions'] - 1
            iCorrect = True
        else:
            iCorrect = False

        return iCorrect

