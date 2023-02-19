
# from <package.module> import <function>
from API.randomGenerator import generateNumber

class Computer:

    def __init__(self):
        self.getRandomNumber = generateNumber()
        self.validInput = False
        self.answer = self.ansToDict()
    

    def getandValidateInput(self):

        while not self.validInput:
            guess = input("Guess a number...\n")

            if guess.isdigit() == False:
                print("Please enter only positive numbers!")
                continue
            elif len(guess) > 4:
                print("Your Input must only be 4 digits!")
                continue
            elif len(guess) < 4:
                print("Your guess must be four digits")
                continue
            elif guess is False:
                print("Invalid input. Please make sure your guess is a 4 digit number.")
                continue
            else:
                self.validInput = True
            return guess
    
    def ansToDict(self):
        answerDict = {}
        for pos, num in enumerate(self.getRandomNumber):
            if num in answerDict:
                answerDict[num][1] += 1
            else:
                answerDict[num] = [pos, 1]
        
        return self.answer


if __name__ == '__main__':
    computer = Computer()

    print("Testing...")
    print(computer.getRandomNumber)
    print(computer.answer)