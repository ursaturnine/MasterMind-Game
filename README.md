MasterMind CLI Game

Can you guess the 4-digit number? Play against the computer via your CLI! You get 10 chances to prove you're a MasterMind. 

Features:
- Options Menu created with the Python 'click' package to run as a CLI program
- A helpful ChatBot helps you through the game play
- The random number to figure out is generated with the random.org API 
- You have the option to view your history of guesses at each try 
- You have the option to view a hint after your 6th try ([STRETCH GOAL] - this was an attempted extension and is a little bug-y)
- A helpful progress bar, created with the Python 'click' package, initiates game play ([STRETCH GOAL] - this was an extension to explore the Python 'click' package further and to provide helpful feedback)

Structure (back-end focused):
- Modular - I separated functions, classes, and constants into separate packages or modules for readability and maintainability
- Tested  - I wrote some unittests to ensure the code will work as expected and to catch bugs in main functionality of the program
- CLI     - I used the Python 'click' package to style the command-line to be able to run this truly as a game w/o too much time spent on frontend functionality
- Requirements - I added a requirements.txt for easy setup for anyone to run the game
- Setup.py   - I added a setup.py so the program can be installed as a package 
- Versioning - I tried to follow best coding practices by version bumping (major.minor.patch); 



Packages:
- click to provide a command line interface for the optionsMenu module
- requests to make an API request
- colorama for coloring prompts and output

Set-Up:

1. Git clone this repository
2. Cd into the directory you've saved the game
3. Activate the virtual environment
      - source venv/bin/activate
3. Install package and requirements
   - 3b. Package
       - pip install .
   - 3a. Requirements
       - pip install -r requirements.txt
  
4. Enter 'game' in your CLI to start the game! (or run src/optionsMenu.py to run the game as a module instead of a CLI program)


Tests:
 1. Run pytest to ensure all unittests are passing
    - [DEBUG] Make sure you have pytest installed in your virtual environment to run the unittests.

       
       
   


