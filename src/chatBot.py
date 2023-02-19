"""Chat bot will dispatch helpful communication to the player
"""

class ChatBot:

    def __init__(self):
        self.summary = "{num} correct numbers and {loc} correct locations"
        self.welcome_message = "Welcome to MasterMind!\n"
        self.correct_answer = "All Correct!"
        self.another_guess = "Guess again..."
        self.guess_history_helper = "Your previous guesses are:\n"
        self.mastermind = "You guessed it! You're a MasterMind!"
        self.game_over = "Game Over!"
        self.tries_remaining = "You have {tries} guesses remaining"


    # Welcome Messsage
    def welcome(self):



        print(self.welcome_message)
        
        return
    
    # all digits correct
    def answer_correct(self):
        self.talk = True

        if self.talk is True:
            print(self.correct_answer)
        
        self.talk = False
        return
    

    def guess_summary(self, correctNums, correctLocs):



        print(self.summary.format(num = correctNums, loc = correctLocs))
 
        return self.summary.format(num = correctNums, loc = correctLocs)


    def guess_again(self):



        print(self.another_guess)
        


        return 


    def viewing_guess_history(self):
            
        print(self.guess_history_helper)

        return


    def won(self):

        print(self.mastermind)
        return
    
    def end_game(self):
    
        print(self.game_over)
        
        return 
    
    def remaining_tries(self, numTries):

        print(self.tries_remaining.format(tries = numTries))


        return



    

    


    



