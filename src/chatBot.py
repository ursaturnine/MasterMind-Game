"""Chat bot will dispatch helpful communication to the player
"""

class ChatBot:

    def __init__(self):
        self.talk = False
        self.summary = "{num} correct numbers and {loc} correct locations"
        self.welcome_message = "Welcome to MasterMind!\n"
        self.correct_answer = "All Correct!"
        self.another_guess = "Guess again..."
        # self.guess_history = "Would you lke to view your guess history?"
        self.guess_history_helper = "Your previous guesses are:\n"
        self.mastermind = "You guessed it! You're a MasterMind!"
        self.game_over = "Game Over!"
        self.tries_remaining = "You have {tries} guesses remaining"


    # Welcome Messsage
    def welcome(self):
        self.talk = True

        if self.talk is True:
            print(self.welcome_message)
        
        self.talk = False
        return
    
    # all digits correct
    def answer_correct(self):
        self.talk = True

        if self.talk is True:
            print(self.correct_answer)
        
        self.talk = False
        return
    
    # summary
    # to do - refactor for appending to guess history
    # double-check this
    def guess_summary(self, correctNums, correctLocs):
        self.talk = True

        if self.talk is True:
            print(self.summary.format(num = correctNums, loc = correctLocs))
            self.talk = False
        return self.summary.format(num = correctNums, loc = correctLocs)


    def guess_again(self):
        self.talk = True

        if self.talk is True:
            print(self.another_guess)
        
        self.talk = False

        return 

    # def view_guess_history(self):
    #     self.talk = True

    #     if self.talk is True:
    #         print(self.guess_history)
        
    #     self.talk = False

    #     return 

    def viewing_guess_history(self):
        self.talk = True

        if self.talk is True:
            print(self.guess_history_helper)
        
        self.talk = False
        return


    def won(self):
        self.talk = True

        if self.talk is True:
            print(self.mastermind)
        self.talk = False
        return
    
    def end_game(self):
        self.talk = True

        if self.talk is True:
            print(self.game_over)
        
        self.talk = False
        return 
    
    def remaining_tries(self, numTries):
        self.talk = True

        if self.talk is True:
            print(self.tries_remaining.format(tries = numTries))


        self.talk = False
        return



    

    


    



