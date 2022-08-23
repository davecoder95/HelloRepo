'''
Author : INR@MoonStar9099 (Los Angeles CA) 


'''
class Question:
    
  def __init__(self, level,quesName,answerChoices, corrAns,multiChoice=False):
    self.quesName = quesName
    self.level = level
    self.answerChoices = answerChoices
    self.corrAns = corrAns
    self.multiChoice = multiChoice


  def getQuestionDetails(self):
    print(self.quesName)
    print(self.answerChoices)
    
  def getAnswer(self):
    print(self.corrAns)


  def getQuestionLevel(self):
    print(self.level, self.multiChoice)


q1 = Question("Easy", "Which is more radioactive?", ["a) banana", "b) grape", "c) avocado", "d) pineapple"],
              "a)", True)

q2 = Question("Easy", "Which is least radioactive, yet still is radioactive?", ["a) banana", "b) grape", "c) avocado", "d) pineapple"],
              "b)", True)

q3 = Question("Easy", "Which is not radioactive?", ["a) banana", "b) grape", "c) avocado", "d) pineapple"],
              "d)", True)

q4 = Question("Easy", "Which is more sweet?", ["a) banana", "b) grape", "c) avocado", "d) pineapple"],
              "d)", True)


q5 = Question("Easy", "Which is most common?", ["a) banana", "b) grape", "c) avocado", "d) pineapple"],
       "a)", True)

questioBank = [q1, q2, q3, q4, q5]

for current in questioBank:
    print(current.getQuestionDetails())
    print(current.getQuestionLevel())
    print(current.getAnswer())
    print("\n")


