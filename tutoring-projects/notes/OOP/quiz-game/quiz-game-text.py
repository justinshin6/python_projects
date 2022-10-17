"""
Overview: For this project, we are making a quiz game where you are given a list of ten true-false questions. If
the user correctly answers a question, the score goes up by one and the user moves onto the next question. If they
miss the question, then they don't get a point. The game ends when there are no more questions left and the final
score is then outputted to the user.
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
- (a) Navigate over to the quiz_brain.py file. Create a new class called QuizBrain that takes in one parameter 
called q_list. 
- (b) Create two variables inside of the def __init__ function for the QuizBrain class. One of the variables is called 
self.question_number which is set equal to zero initially. The other variable is called self.question_list which is 
set equal to the q_list parameter. 
Reflection Question: Why is self.question_number set to 0 and self.question_list set equal to the q_list parameter? 
What is the difference between these two variables? 
- (c) Create a new function inside of the QuizBrain class called next_question() that has no parameters. 
Reflection Question: How do you think that we should take this next_question() function? 
- (d) Create a variable called current_question that uses the self.question_list and the self.question_number parameters
to get the the current question from the list. 
- (e) Increase the question number by one 
- (f) Create a variable called user_answer that takes in an input from the user of the following format: 
Q.{question number}: {question text} (True/False): 
Reflection Question: What should go in the fields {question number} and {question text}
- (g) Inside of main.py, import the QuizBrain class and create a new object of the class that takes in the question_bank
that we created previously as an argument to the q_list parameter. 
"""

"""
Step 4: How to continue showing new questions 

- (a) Create a new function called still_has_questions() inside of the QuizBrain class that will return a boolean of 
true or false. This function will return true if there are still some questions left and false if we have reached the end
of the question bank. 
- Hint: How can we use the len() and the length of the question bank to return a boolean? 
Reflection Question: How can we get the questions to keep on showing up? 
- Hint: What type of loop have we used in the past where we do certain actions until a certain condition tells us to stop? 
- (b) Inside of the main.py(), use a while loop and the function that we just created to make questions continue 
to show up. 
"""

"""
Step 5: Checking Answers and Keeping Score
- The whole purpose of this step is to keep track of the score throughout the game. 
- (a) Create a new instance variable in the def __init__ function of the QuizBrain class called self.score and set it 
equal to 0. 
- (b) Create a function called check_answer() inside of the QuizBrain class that takes in two parameters: user_answer
and correct_answer. 
Reflection: Why do you think this function will take in a user_answer and a correct_answer? 
- Follow Up Question: What thing can we use in the past to check to see if the user_answer equals the correct answer? 
- Hint: It has to do with conditionals. 
- (c) If the answer is correct, increase the self.score by one and print out an informative message saying that 
you got the question right. 
- (d) If the answer is not correct, then do nothing to the self.score and then print out a message saying that the 
user got the question wrong. 
- (e) In this function, also print out the correct answer to the question and the person's score relative to the 
question number in the following format: 
print(f"Your current score is: {score}/{question_number}")
Reflection Question: Now, where do you think that we should call this function? Inside of main.py? Inside of QuizBrain? 
- If inside of QuizBrain, where inside of QuizBrain should we call this function? 
- Hint: Where do we have access to both a user_answer and the correct_answer for a particular question? 
- (f) Call the check_answer() function and enter in the proper parameters. 
- (g) Print out the final score outside of the while loop in the main.py class with the following lines: 
print("You've completed the quiz")
print(f"Your final score was: {score}/{question_number}")

"""

"""
Step 6: Use Open Trivia DB to Get New Questions 
- (a) Go to the following link https://opentdb.com/
- (b) Navigate over to the API section and then choose 10 questions, a category, a difficulty, True/False questions, 
and default encoding. 
- (c) Copy the link into a new tab and then copy over the results over into your data.py 
- (d) Now, run your program
Reflection Question: Why are the errors showing up in your terminal? 
- (e) Fix the bugs and run your program again with your new questions. 
"""

"""
Congratulations! You've finished the project! Great work! 
"""