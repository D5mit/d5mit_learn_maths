class Maths_Test:
    """ Maths Test class.  This class is the actual math test that is being presented to a person to write.

    Parameters:
    argument1 (int): Description of arg1

    description (string): Description of the test that is being written
    start_time  #toDo
    end_Time    #toDo
    questions (DF)
        Question
        Answer
        How many times to ask the question
        How many times question answered correctly    #toDo
        How many times question answered incorrectly  #toDo
    person    #toDo
    """

    def __init__(self, description, questions=[]):
        self.description = description
        self.questions = questions

    def set_questions(self, questions):
        self.questions = questions

    def get_questions(self):
        return self.questions

