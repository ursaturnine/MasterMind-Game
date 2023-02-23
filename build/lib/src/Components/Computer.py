from src.API.randomGenerator import generateNumber


class Computer:

    def __init__(self):
        self.validInput = False
        self.randomNumber = None
    

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
    
    def getRandomNumber(self):
        random = generateNumber()
        self.randomNumber = random
        return 
    
    def ansToDict(self):

        if self.randomNumber == None:
            return
        
        answerDict = {}
        for pos, num in enumerate(self.randomNumber):
            if num in answerDict and self.randomNumber.count(num) > 1:
                count = self.randomNumber.count(num)
                posVal = self.calcMultiplePos(num, count, self.randomNumber)
                answerDict[num] = [(posVal), count ]
            else:
                answerDict[num] = [(pos,), 1]


        return answerDict

    def calcMultiplePos(self, num, count, randomNumber):
        allPos = []
        i = count
        while i:
            for pos, ele in enumerate(randomNumber):
                if ele == num:
                    allPos.append(pos)
                    i -= 1

        
        return tuple(allPos)





        
