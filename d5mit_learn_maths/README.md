# d5mit_learn_maths
A simple class to load a test and present the test to a person.   


## Packages needed:
### 1. pytest
        pip install -U pytest
        
### 2. d5mit_learn_maths
        pip install -U d5mit_learn_maths

### 3. Class
    Maths_Test:
    Maths Test class.  This class is the actual math test that is being presented to a person to write.

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

### 4. Methods
#### 4.1 get_test
     Get current dest description
     Parameters: none
     Return: description (String): Description if the current test

#### 4.2 set_questions(self, questions):
     Set test questions
     Parameters: questions (dataframe): Questions
     Return: none

#### 4.3 get_questions(self):
     Get test questions
     Parameters: none
     Return: questions (dataframe): table with questions

#### 4.4 ask_question(self):
     Ask a random questions
     Parameters: none
     Return: return a list with the actual question ['question' 'answer' 'nrQuestions']

#### 4.5 get_question_index(self):
     Get the current question index
     Parameters: none
     Return: questionIndex (int): current question index

#### 4.6 check_answer(self, answer):
     Get the current question index
     Parameters: answer (str): users answer
     Return: iCorrect (bool): True if question is correct
            
### 5. Example Program
    See program example.py. 
    1. This program creates a dataframe containing questions
    2. Create method maths_test
    3. Loops through questions and via terminal pose question and allow user to answer