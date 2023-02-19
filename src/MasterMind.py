import copy
from ChatBot import ChatBot


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
            if char in word:
                occurrences = wordCopy[char][1]
                if occurrences > 0:
                    correctChars += 1
                    wordCopy[char][1] -= 1
        
        return correctChars


    def matchLocs(self, guess, word):
        correctPlacement = 0

        for pos, char in enumerate(guess):
            if char in word and word[char][0] == pos:
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

    

