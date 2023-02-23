"""Chat bot will dispatch helpful communication to the player
"""

import colorama
from colorama import Fore, Back, Style

# initialize colorama
colorama.init(autoreset=True)

class ChatBot:

    def __init__(self):
        self.summary = "{num} correct numbers and {loc} correct locations"
        self.welcome_message = "Welcome to MasterMind!\n"
        self.correct_answer = "All Correct!"
        self.another_guess = "Guess again..."
        self.guess_history_helper = "Your previous guesses are:\n"
        self.mastermind = "You guessed it! You're a MasterMind!"
        self.game_over = "The correct number was {num}! Game Over!"
        self.tries_remaining = "You have {tries} guesses remaining"
        self.hint = "The {pos}{suff} number rhymes with {adj}"


    # Welcome Messsage
    def welcome(self):
        print(Fore.LIGHTBLUE_EX + self.welcome_message)
        
        return
    
    # all digits correct
    def answer_correct(self):
        self.talk = True

        if self.talk is True:
            print(self.correct_answer)
        
        self.talk = False
        return
    

    def guess_summary(self, correctNums, correctLocs):



        print(Fore.WHITE + Back.CYAN + self.summary.format(num = correctNums, loc = correctLocs))

        return (Fore.WHITE  + Back.CYAN + self.summary.format(num = correctNums, loc = correctLocs))


    def guess_again(self):



        print(self.another_guess)
        


        return 


    def viewing_guess_history(self):
            
        print(self.guess_history_helper)

        return


    def won(self):

        print(self.mastermind)
        return
    
    def end_game(self, randomNumber):
        
        print(self.game_over.format(num=randomNumber))
        return 
    
    def remaining_tries(self, numTries):

        print(self.tries_remaining.format(tries = numTries))
        return
    

    def helpful_hint(self, ind, suffix, word):
        print(Fore.MAGENTA + Back.BLUE + "Your Hint is...")
        print(Fore.BLUE + self.hint.format(pos = ind, suff = suffix, adj = word))
        return




    

    


    



