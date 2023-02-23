# API Constants
LENGTH_OF_ANSWER = 4
MIN_VALUE = 0
MAX_VALUE = 7
NUM_OF_COLUMNS = 4
BASE_SYSTEM = 10
RESPONSE_FORMAT = 'plain'
RANDOMIZATION = 'new'


# Gameplay Constants
TRIES = 10
USER_QUIT = ['Q', 'q']
USER_HISTORY = ['H', 'h']

# User Input Constants
USER_YES = ['y', 'Y']
USER_NO = ['n', 'N']


# Options Menu Constants
INSTRUCTION_MENU = "Instructions:\n1. A random 4-digit number will be generated.\n2. You must guess the 4-digit number.\n3. You will have 10 tries.\nAre You Ready to Play? "



# Helpful Hinst Constants - must have 10 items in list each
HINTS_DICT = {
    1 : [[
    "fun",
    "bun",
    "sun",
    "run",
    "pun",
    "hon'",
    "spun",
    "done",
    "none",
    "stun"
], ['st']],

2: [[
    "new",
    "shoe",
    "grew",
    "you",
    "blue",
    "clue",
    "chew",
    "stew",
    "goo",
    "view"
], ['nd']],

3 : [[
    "pea",
    "tree",
    "ski",
    "knee",
    "key",
    "sea",
    "tea",
    "free",
    "glee",
    "spree"
], ['rd']],

4 :[[
    "door",
    "floor",
    "chore",
    "more",
    "oar",
    "store",
    "core",
    "score",
    "pour",
    "soar"
], ['th']],

5 : [[
    "hive",
    "drive",
    "thrive",
    "dive",
    "chive",
    "wives",
    "knives",
    "find",
    "time",
    "rind",
], ['th']],

6 : [[
    "sticks",
    "licks",
    "kicks",
    "tricks",
    "fix",
    "mix",
    "bricks",
    "chicks",
    "clique",
    "styx"
], ['th']],

7 : [[
    "heaven",
    "second",
    "question",
    "lemon",
    "reckon",
    "lesson",
    "melon",
    "Helen",
    "yemen",
    "ellen"
], ['th']]
}