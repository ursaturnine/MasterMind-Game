import copy
import constant
from randomGenerator import  generateNumber
from chatBot import ChatBot


# validate user input
def getandValidateInput():
    validInput = False
    while not validInput:
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
            validInput = True
        return guess
        



# options menu for game - to do
def options():
    pass


# marshall answer string to dictionary format
def ansToDict(ans):
    answerDict = {}
    for pos, num in enumerate(ans):
        if num in answerDict:
            answerDict[num][1] += 1
        else:
            answerDict[num] = [pos, 1]
    
    return answerDict

# game play
def masterMind():
    # answerString = generateNumber()

    # # toDict
    # answer = ansToDict(answerString)

    answerString = '4128'

    answer = {
        '4': [0, 1],
        '1': [1, 1],
        '2': [2, 1],
        '8': [3, 1]
    }


    # print("Shhh...the answer is...")
    # print(answerString)

    # initialize helperBot
    helperBot = ChatBot()


    # start of game - welcome message
    helperBot.welcome()

    # history of guesses queue - enqueue O(1) dequeue O(1)
    history = []

    # queue
    viewed = []

    isMasterMind = False
    tries = constant.TRIES


    # game play
    while tries > 0 and isMasterMind is False:
    
        if tries < 10:
            view = input("Would you like to view your history? (Y or N)")

            # view previous guesses
            if view in constant.USER_YES:
                    viewHistory(history, viewed, helperBot)
        

        guess = getandValidateInput()

        
        history.append(guess)

        # if guess is correct or not
        if guess == answerString:
            helperBot.answer_correct()
            isMasterMind = True
            break
        else:
            correctNums = matchNums(guess, answer)
            if correctNums:
                correctLocs = matchLocs(guess, answer)
            else:
                correctLocs = 0

            # this should print out msg during game play AND add to hitory stack
            history.append(helperBot.guess_summary(correctNums, correctLocs))
            if tries - 1 != 0:
                helperBot.guess_again()
            tries -= 1
            helperBot.remaining_tries(tries)
    

    if isMasterMind:
        helperBot.won()
        return
    else:
        helperBot.end_game()
        return

# view history of guesses and feedback - O(1)
def viewHistory(history, viewed, helperBot):

    helperBot.viewing_guess_history()

    while history:
        guesses = history.pop(0)
        print(guesses)
        viewed.append(guesses)
    while viewed:
        history.append(viewed.pop(0))
    return

# quanity of numbers guessed correctly - O(n^2)
def matchNums(guess, word):

    wordCopy = copy.deepcopy(word)

    correctChars = 0
    for char in guess:
        if char in word:
            occurrences = wordCopy[char][1]
            if occurrences > 0:
                correctChars += 1
                wordCopy[char][1] -= 1
    
    return correctChars

# quantity of locations guessed correctly - O(1)
def matchLocs(guess,  word):

    correctPlacement = 0

    for pos, char in enumerate(guess):
        if char in word and word[char][0] == pos:
            correctPlacement += 1

    return correctPlacement


masterMind()








