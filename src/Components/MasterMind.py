import copy
from src.Components.ChatBot import ChatBot
from src.constant import HINTS_DICT
from random import randint


class MasterMind:

    def __init__(self):
        self.history = []
        self.viewed = []
        self.isMasterMind = False
        self.helperBot = ChatBot()
    

    def matchNums(self, guess, word):
        wordCopy = copy.deepcopy(word)

        correctChars = 0
        for char in guess:
            if char in wordCopy:
                occurrences = wordCopy[char][1]
                if occurrences > 0:
                    correctChars += 1
                    wordCopy[char][1] -= 1
        
        return correctChars


    def matchLocs(self, guess, word):

        correctPlacement = 0

        for pos, char in enumerate(guess):
            if char in word:
                occurrences = word[char][0]
                if  pos in occurrences:
                    correctPlacement += 1


        return correctPlacement

    def viewHistory(self):

        self.helperBot.viewing_guess_history()

        while self.history:
            guesses = self.history.pop(0)
            print(guesses)
            self.viewed.append(guesses)
        while self.viewed:
            self.history.append(self.viewed.pop(0))
    

    def giveHint(self, answerDict):

        # random # from 1 - 4 - both ends inclusive
        indPos = randint(0, 3)
        findAdj = randint(1, 10)

        print("indPos is..")
        print(indPos)
        print("findadj is...")
        print(findAdj)

        # set pos
        pos = indPos + 1

        print("Pos is..")
        print(pos)

        # find number in answer to rhyme with
        for key, values in answerDict.items():
            if indPos in values[0]:
                end_num = int(key)
                            

        
        # set suff
                for num, values in HINTS_DICT.items():
                    if pos == num:
                        print("suff is...")
                        print( HINTS_DICT[num][1][0])
                        suff = HINTS_DICT[num][1][0]
        # set adj
        for key, values in HINTS_DICT.items():
            if end_num == key:
                print("end_num and key is...")
                print(end_num, key)
                for ind, word in enumerate(values[0]):
                    if ind == findAdj:
                        print("ind and findadj is...")
                        print(ind, findAdj)
                        adj = word
                        self.helperBot.helpful_hint(pos, suff, adj)







    

