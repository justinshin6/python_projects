"""
Overview: For this project, we are making a quiz game where you are given a list of ten true-false questions. If
the user correctly answers a question, the score goes up by one and the user moves onto the next question. If they
miss the question, then they don't get a point. The game ends when there are no more questions left and the final
score is outputted to the user.
"""
"""
Step 1: Creating the Question Model Class 
- (a) Inside of the question_model.py file, create a class called "Question" that takes in two parameters inside of 
the __init__ function: q_text, and q_answer. 
- These two fields stand for the question text and the question answer which are the two components that make up 
a question in this game. 
- (b) Then, create two new variables called self.text and self.answer and set them equal to these parameters 
Reflection Questions: 
1.) Why are we setting self.text and self.answer equal to q_text and q_answer? 
2.) Why does text and answer have self in front of it while q_text and q_answer do not? 
3.) What does the def __init__ function do again and why is it so important? 
"""

"""
Step 2: Creating the List of Question Objects from the Data 
- (a) Inside of main.py import your Question class from the question_model.py file 
- (b) Inside of main.py also import the question_data from the data.py file 
- (c) Create a new, empty array called question_bank which will be used to track the Question objects
- (d) Use a for loop to loop through the question_data
- (e) Extract the text and answer from each question in the question_data and set that equal to two variables that are 
called q_text and q_answer respectively. 
- (f) Using q_text and q_answer create a new variable called question whose value is a Question object that takes in 
the q_text and q_answer as parameters. 
- (g) Add this question to the question bank and print out the question_bank outside of the for loop 
Reflection Questions: 
1.) Explain what is going on inside of the for loop
2.) Why are we making the empty array outside of the for loop and not inside 
3.) With that said, why are we making a new question object inside of the for loop for each question 
4.) Why does the Question object take in two parameters? 
5.) Is there anything confusing about this from an Object-Oriented Programming perspective? 
"""

"""
Step 3: The QuizBrain and the next_question() method
"""

"""
Step 4: How to continue showing new questions 
"""

"""
Step 5: Checking Answers and Keeping Score
"""

"""
Step 6: Use Open Trivia DB to Get New Questions 
"""
