 # 1.6hrs on SCRIMBA
 
 # Command Line = a text-based user interface used to interact with a computer's operating system by typing commands at a prompt. 
  # Unlike a graphical user interface (GUI), which uses a mouse to click on icons and menus, the command line relies solely on the keyboard 
  # for input and displays output as text.

# Why type?
 # File Management
 # Control Development Environment
 # Automate Repetitive Tasks

-----------------------------------------------------

# INSPECT THE FILE TREE

pwd = # pwd is solely for displaying your current location; it cannot be used to change directories. The cd command is used for that purpose.

ls = # a fundamental utility in Unix-like operating systems used to list the contents of a directory.

cd = # short for change directory, is a fundamental shell command used to navigate and change the current working directory in command-line 
 # interface

clear = # used to clear the terminal screen, improving readability by removing previous output. No actions are stopped, just visual clutter.

///////

Challenge: Inspect the file tree
1. Print the current working directory.
2. Navigate into the directory "geography_game".
3. List the contents of "geography_game".
4. Clear the terminal.

# 1 --- pwd
# 2 --- ls
# 3 --- cd geography_game --- (afterwards) ls (names contents in geography_game)
# 4 --- clear

---------------------------------------------------------

# RULES OF NAVIGATION

cd .. = # to change the current working directory to its parent directory (the directory one level up) EXAMPLE --- cd ../countries

Challenge: Rules of navigation
1. Navigate into the directory "forests".
2. Find the following files:
    a. "rainforests.txt"
    c. "large_contries_by_population.txt".
    d. "capitals.txt"
3. Clear the terminal from visual clutter.

NB: Make sure to use everything you have learned so far: 'pwd', 'ls', 'cd', '..', and 'clear'.

# 1 --- pwd -- ls -- cd geography_game -- ls
# 2 --- cd forests -- pwd -- ls - ls .. -- cd .. -- cd ../.. (take 2 levels ups) # looking for files continues...
# 3 --- clear