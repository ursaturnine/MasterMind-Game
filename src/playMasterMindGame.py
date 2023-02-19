import constant
from MasterMind import MasterMind
from Computer import Computer

# game play
def playMasterMind():
    computer = Computer()
    computer.getRandomNumber()
    answer = computer.ansToDict()
    randomNumber = computer.randomNumber

    mastermind = MasterMind()


    # start of game - welcome message
    mastermind.helperBot.welcome()

    # initialize number of tries
    tries = constant.TRIES


    # game play
    while tries > 0 and mastermind.isMasterMind is False:
    
        if tries < 10:
            view = input("Would you like to view your history? (Y or N)")
            if view in constant.USER_YES:
                mastermind.viewHistory()

        
        computer.validInput = False
        guess = computer.getandValidateInput()
        
        mastermind.history.append(guess)

        if guess == randomNumber:
            mastermind.helperBot.answer_correct()
            mastermind.isMasterMind = True
            break
        else:
            correctNums = mastermind.matchNums(guess, answer)
            if correctNums:
                correctLocs = mastermind.matchLocs(guess, answer)
            else:
                correctLocs = 0


            mastermind.history.append(mastermind.helperBot.guess_summary(correctNums, correctLocs))
            if tries - 1 != 0:
                mastermind.helperBot.guess_again()
            tries -= 1
            mastermind.helperBot.remaining_tries(tries)


    if mastermind.isMasterMind:
        mastermind.helperBot.won()
        return
    else:
        mastermind.helperBot.end_game()
        return


playMasterMind()










