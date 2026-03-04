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

--------------------------------------------------

# CREATE AND DELETE FILES

touch = # CREATE -- The most common use is to quickly generate a new, empty file without opening a text editor.
# EXAMPLE -- touch filename.txt

rm = # DELETE -- used to permanently delete files and directories from the filesystem.
# EXAMPLE -- rm mountains.txt

///////////////

Challenge: Create & delete files
1. Find the file "virus.exe" and delete it. Lists the contents of the parent directory of "virus.exe" to check that the file was deleted correctly.
2. Inside "geography_game", create a new file called "rules.txt", and list the contents of "geography_game".

Hint: What should you always do as the first thing before typing any other commands?

# TIPS = can open a new terminal to look for other files as well!!!

-----------------------------------------

# CREATE AND DELETE DIRECTORIES

mkdir = # (make directories) -- EXAMPLE -- mkdir cities 
rmdir = # (remove directories) -- EXAMPLE -- rmdir cities (only works if directory is empty)
rm -r cities = # if directory not empty use rm -r

/////////////////////////

Challenge: Create & delete directories
1. Find and delete the directory called "family_photos_1988". List the contents of the parent directory of "family_photos_1988" to check that this directory was deleted correctly.
2. Inside "geography_game", create a new directory called "cities". List the contents of "geography_game" to check that "cities" was created correctly.

# Use cd .. to go back to previous step and then ls to list details

------------------------------------------------------

# WRITE TO FILES

echo = # a fundamental shell command used to display a line of text or a string on the standard output
 # EXAMPLE -- echo 'Hello World!' # prints 'Hello World!'

# Redirect Output
# If hello.txt does not exist, echo will create a file
# CREATE A FILE w/ echo
echo 'Hello, World' > hello.txt # prints 'Hello, World' to the file hello.txt

///////////////////////////
Main challenge: Write to files
1. Inside "geography_game", create a new directory called "about_the_game".
2. Write the string 'AB, CEO and creative genius' to a new file called "team_members.txt". This file should be placed inside "about_the_game".
3. Append the string '<your initials>, hard-working intern' to the file "team_members.txt".
4. Open the file in the sidebar to check that everything went well.

Important: Wrap your strings in single quotes.

-----------------------------------------------

# READ FROM FILES

cat = # stands for concatenate and is primarily used to read, display, combine, and manipulate text files. 
 # EXAMPLE -- cat hello.txt -- # prints Hello World! to terminal

# Redirect Output -- CREATE FILE as well if it does not already exists
cat hello.txt > hello.copy.txt  

# NOTES NOTED
> # overwrites
>> # appends
 # ECHO vs CAT
  # echo command is used to display a line of text or string arguments provided directly to it, while the cat command is 
  # used to read, display, and concatenate the contents of files.

/////////////////////////////////////////
Challenge: Read from files
1. Find the file "external_people.txt" and print its contents to the terminal to see what it is.
2. Read the contents of "external_people.txt" again, but this time, redirect and append it to "team_members.txt".
3. Print the contents of "team_members.txt" to the terminal to check that everything went well.
4. Delete "external_people.txt".

# 1 -- cd geography/cities

--------------------------------------------------------
