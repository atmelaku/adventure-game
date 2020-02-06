import product
class items(object):
    def __init__(self, ten, one, three, x, y):
        self.ten = 10
        self.one = 1
        self.three = 3
        self.zero = 0
        self.x = x
        self.y = y

    def enter(self):
        return 'multiplying_Positive_Numbers_Question1'

class multiplyingPositiveNumbersQuestion1(items):
    def enter(self):
        print("well come to the second simple math knowlodge test. the second section is going to be evatuating some problems using multiplication oprators")
        print("let's begin!")
        print(f"what is the productof {self.ten} and {self.zero}?")
        Answer = input("> ")
        if Answer == "0":
            print("that is right!")
            return 'multiplying_Positive_Numbers_Question2'
        elif Answer == "100":
            print("you broke the rule")
            return 'multiplying_Positive_Numbers_Question1'
        else:
            print("wrong!")
            return 'multiplying_Positive_Numbers_Question1'

class multiplyingPositiveNumbersQuestion2(items):
    def enter(self):
        print("you got the first one let's do the next one")
        print(f"what is the product of {self.three} and {self.one}?")
        Answer = input("> ")
        if Answer == "3":
            print("correct!")
            return 'multiplying_Positive_Numbers_Question3'

        elif Answer == "4":
            print("you broke the rule")
            return 'multiplying_Positive_Numbers_Question2'
        else:
            print("wrong!")
            return 'multiplying_Positive_Numbers_Question2'

class multiplyingPositiveNumbersQuestion3(items):
    def enter(self):
        print("so far you are doing good do the next question")
        print(f"what is the value of {self.ten} * {self.one} * {self.zero}?")
        Answer = input("> ")
        if Answer == "0":
            print("correct")
            return "multiplying_Positive_Numbers_Question4"

        elif Answer == "11":
            print("you broke the rule")
            return "multiplying_Positive_Numbers_Question3"
        else:
            print("wrong!")
            return "multiplying_Positive_Numbers_Question3"

class multiplyingPositiveNumbersQuestion4(items):
    def enter(self):
        print("next one is word problem")
        print(f"thom bought {self.ten} car yesterday and today, he bought two times {self.three} cars. so, how many cars does have thom?")
        Answer = input("> ")
        if Answer == "16":
             print("correct")
             return "multiplying_Positive_Numbers_Question5"
        elif Answer == "13":
             print("you broke the rule")
             return "multiplying_Positive_Numbers_Question4"
        else:
            print("wrong")
            return "multiplying_Positive_Numbers_Question4"

class multiplyingPositiveNumbersQuestion5(items):
    def enter(self):
        print("first section of last question")
        print(f"let say you have you won a lottery ten times {self.ten} and zero times{self.zero}. how many times did you wine the lottery?")
        Answer = input("> ")
        if Answer == "100":
            print("correct")
            return "multiplying_Negative_Numbers_Question1"
        elif Answer == "110":
            print("you broke the rule and you need study more")
            return "multiplyingPositiveNumbersQuestion5"
        else:
            print("wrong. and I think you don't understand that")
            return "multiplyingPositiveNumbersQuestion5"

class multiplyingNegativeNumbersQuestion1(items):
    def enter(self):
        print("second section is adding negative numbers")
        print(f"waht is the product of -{self.zero} and {self.one}?")
        Answer = input("> ")
        if Answer == "0":
            print("that is perfect! move on the next one.")
            return "multiplying_Negative_Numbers_Question2"
        elif Answer == "-01":
            print("you broke the rule!")
            return "multiplying_Negative_Numbers_Question1"
        else:
            print("wrong! you need study more")
            return "multiplying_Negative_Numbers_Question1"

class multiplyingNegativeNumbersQuestion2(items):
    def enter(self):
        print("try the next one also")
        print(f"{self.three}{self.x} * {self.one}{self.x} = 27. what is the value of {self.x}?")
        Answer = input("> ")
        if Answer == "3":
            print("correct")
            return "multiplying_Negative_Numbers_Question3"
        elif Answer == "9":
            print("you broke the rule")
            return "multiplying_Negative_Numbers_Question2"
        else:
            print("wrong")
            return "multiplying_Negative_Numbers_Question2"
class multiplyingNegativeNumbersQuestion3(items):
    def enter(self):
        print("next question")
        print(f"what is the product of -{self.three} and -(-{self.one})?")
        Answer = input("> ")
        if Answer == "-3":
            print("correct")
            return "multiplying_Variables_Question1"
        elif Answer == "3":
            print("you broke the rule")
            return "multiplying_Negative_Numbers_Question3"
        else:
            print("wrong")
            return "multiplying_Negative_Numbers_Question3"
class multiplyingVariablesQuestion1(items):
    def enter(self):
        print("third section is adding variables:")
        print(f"what is the product of {self.ten}{self.x} and {self.zero}{self.x}?")
        Answer = input("> ")
        if Answer == "0":
            print("that is great!")
            return "evaluating_Variables_Question1"
        elif Answer == "0x":
            print("you broke the rule!")
            return "multiplying_Variables_Question1"
        else:
            print("wrong!")
            return "multiplying_Variables_Question1"
class evaluatingVariablesQuestion1(items):
    def enter(self):
        print("fourht section is going to finding the value of variables")
        print(f"{self.ten} * {self.x} = {self.zero}. what is the value of x?")
        Answer = input("> ")
        if Answer == "0":
            print("nice work!. try again if you want to.")
            return 'finished'
        elif Answer == "10":
            print("you broke the rule")
            return "evaluating_Variables_Question1"
        else:
            print("wrong")
            return "evaluating_Variables_Question1"
class Map(object):
    parts = {
    'items': items(10, 1, 3, 'x', 'y'),
    'multiplying_Positive_Numbers_Question1': multiplyingPositiveNumbersQuestion1(10, 1, 3, 'x', 'y'),
    'multiplying_Positive_Numbers_Question2': multiplyingPositiveNumbersQuestion2(10, 1, 3, 'x', 'y'),
    'multiplying_Positive_Numbers_Question3': multiplyingPositiveNumbersQuestion3(10, 1, 3, 'x', 'y'),
    'multiplying_Positive_Numbers_Question4': multiplyingPositiveNumbersQuestion4(10, 1, 3, 'x', 'y'),
    'multiplying_Positive_Numbers_Question5': multiplyingPositiveNumbersQuestion5(10, 1, 3, 'x', 'y'),
    'multiplying_Negative_Numbers_Question1': multiplyingNegativeNumbersQuestion1(10, 1, 3, 'x', 'y'),
    'multiplying_Negative_Numbers_Question2': multiplyingNegativeNumbersQuestion2(10, 1, 3, 'x', 'y'),
    'multiplying_Negative_Numbers_Question3': multiplyingNegativeNumbersQuestion3(10, 1, 3, 'x', 'y'),
    'multiplying_Variables_Question1': multiplyingVariablesQuestion1(10, 1, 3, 'x', 'y'),
    'evaluating_Variables_Question1': evaluatingVariablesQuestion1(10, 1, 3, 'x', 'y')
    }
    def __init__(self, start_part):
        self.start_part = start_part
    def next_part(self, part_name):
        val = Map.parts.get(part_name)
        return val
    def opening_part(self):
        return self.next_part(self.start_part)
