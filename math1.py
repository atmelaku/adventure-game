
class items(object):
    def __init__(self, ten, one, three, x, y):
        self.ten = 10
        self.one = 1
        self.three = 3
        self.zero = 0
        self.x = x
        self.y = y

    def enter(self):
        return 'adding_Positive_Numbers_Question1'

class addingPositiveNumbersQuestion1(items):
    def enter(self):
        print("well come to simple math knowlodge test. the first section is going to be evatuating some problems using addition oprator")
        print("let's begin!")
        print(f"what is the sum of {self.ten} and {self.zero}?")
        Answer = input("> ")

        if Answer == "10":
            print("that is right!")
            return 'adding_Positive_Numbers_Question2'

        elif Answer == "100":
            print("you broke the rule")
            return 'adding_Positive_Numbers_Question1'
        else:
            print("wrong!")
            return 'adding_Positive_Numbers_Question1'

class addingPositiveNumbersQuestion2(items):
    def enter(self):
        print("you got the first one let's do the next one")
        print(f"what is the sum of {self.three} and {self.one}?")
        Answer = input("> ")
        if Answer == "4":
            print("correct!")
            return 'adding_Positive_Numbers_Question3'

        elif Answer == "3":
            print("you broke the rule")
            return 'adding_Positive_Numbers_Question2'
        else:
            print("wrong!")
            return 'adding_Positive_Numbers_Question2'

class addingPositiveNumbersQuestion3(items):
    def enter(self):
        print("so far you are doing good do the next question")
        print(f"what is the value of {self.ten} + {self.one} + {self.zero}?")
        Answer = input("> ")
        if Answer == "11":
            print("correct")
            return "adding_Positive_Numbers_Question4"

        elif Answer == "13":
            print("you broke the rule")
            return "adding_Positive_Numbers_Question3"
        else:
            print("wrong!")
            return "adding_Positive_Numbers_Question3"

class addingPositiveNumbersQuestion4(items):
    def enter(self):
        print("next one is word problem")
        print(f"thom bought {self.ten} car yesterday and today, he bought {self.three} cars. so, how many cars does have thom?")
        Answer = input("> ")
        if Answer == "13":
             print("correct")
             return "adding_Positive_Numbers_Question5"
        elif Answer == "7":
             print("you broke the rule")
             return "adding_Positive_Numbers_Question4"
        else:
            print("wrong")
            return "adding_Positive_Numbers_Question4"

class addingPositiveNumbersQuestion5(items):
    def enter(self):
        print("first section of last question")
        print(f"let say you have you won a lottery ten times {self.zero} and hundred times{self.zero}. how many times did you wine the lottery?")
        Answer = input("> ")
        if Answer == "0":
            print("correct")
            return "adding_Negative_Numbers_Question1"
        elif Answer == "110":
            print("you broke the rule and you need study more")
            return "addingPositiveNumbersQuestion5"
        else:
            print("wrong. and I think you don't understand that")
            return "addingPositiveNumbersQuestion5"

class addingNegativeNumbersQuestion1(items):
    def enter(self):
        print("second section is adding negative numbers")
        print(f"waht is the sum of -{self.zero} and {self.one}?")
        Answer = input("> ")
        if Answer == "-1":
            print("that is perfect! move on the next one.")
            return "adding_Negative_Numbers_Question2"
        elif Answer == "-01":
            print("you broke the rule!")
            return "adding_Negative_Numbers_Question1"
        else:
            print("wrong! you need study more")
            return "adding_Negative_Numbers_Question1"

class addingNegativeNumbersQuestion2(addingNegativeNumbersQuestion1):
    def enter(self):
        print("try the next one also")
        print(f"{self.ten}{self.x} - {self.three}{self.x} - {self.one}{self.x} = {self.three}. what is the value of {self.x}?")
        Answer = input("> ")
        if Answer == "0.5":
            print("correct")
            return "adding_Negative_Numbers_Question3"
        elif Answer == "2":
            print("you broke the rule")
            return "adding_Negative_Numbers_Question2"
        else:
            print("wrong")
            return "adding_Negative_Numbers_Question2"
class addingNegativeNumbersQuestion3(items):
    def enter(self):
        print("next question")
        print(f"what is the difference of -{self.zero} and -(-{self.one})?")
        Answer = input("> ")
        if Answer == "-1":
            print("correct")
            return "adding_Variables_Question1"
        elif Answer == "1":
            print("you broke the rule")
            return "adding_Negative_Numbers_Question3"
        else:
            print("wrong")
            return "adding_Negative_Numbers_Question3"
class addingVariablesQuestion1(items):
    def enter(self):
        print("third section is adding variables:")
        print(f"what is the sum of {self.ten}{self.x} and {self.zero}{self.x}?")
        Answer = input("> ")
        if Answer == "10x":
            print("that is great!")
            return "evaluating_Variables_Question1"
        elif Answer == "100x":
            print("you broke the rule!")
            return "adding_Variables_Question1"
        else:
            print("wrong!")
            return "adding_Variables_Question1"
class evaluatingVariablesQuestion1(items):
    def enter(self):
        print("fourht section is going to finding the value of variables")
        print(f"{self.ten} + {self.x} = {self.zero}. what is the value of x?")
        Answer = input("> ")
        if Answer == "-10":
            print("nice work!. try again if you want to.")
            return "finish_Game"
        elif Answer == "10":
            print("you broke the rule")
            return "evaluating_Variables_Question1"
        else:
            print("wrong")
            return "evaluating_Variables_Question1"
class finishGame(object):
    def enter(self):
        exit(1)
class Map(object):
    parts = {
    'items': items(10, 1, 3, 'x', 'y'),
    'adding_Positive_Numbers_Question1': addingPositiveNumbersQuestion1(10, 1, 3, 'x', 'y'),
    'adding_Positive_Numbers_Question2': addingPositiveNumbersQuestion2(10, 1, 3, 'x', 'y'),
    'adding_Positive_Numbers_Question3': addingPositiveNumbersQuestion3(10, 1, 3, 'x', 'y'),
    'adding_Positive_Numbers_Question4': addingPositiveNumbersQuestion4(10, 1, 3, 'x', 'y'),
    'adding_Positive_Numbers_Question5': addingPositiveNumbersQuestion5(10, 1, 3, 'x', 'y'),
    'adding_Negative_Numbers_Question1': addingNegativeNumbersQuestion1(10, 1, 3, 'x', 'y'),
    'adding_Negative_Numbers_Question2': addingNegativeNumbersQuestion2(10, 1, 3, 'x', 'y'),
    'adding_Negative_Numbers_Question3': addingNegativeNumbersQuestion3(10, 1, 3, 'x', 'y'),
    'adding_Variables_Question1': addingVariablesQuestion1(10, 1, 3, 'x', 'y'),
    'evaluating_Variables_Question1': evaluatingVariablesQuestion1(10, 1, 3, 'x', 'y'),
    'finish_Game': finishGame()
    }
    def __init__(self, start_part):
        self.start_part = start_part
    def next_part(self, part_name):
        val = Map.parts.get(part_name)
        return val
    def opening_part(self):
        return self.next_part(self.start_part)
