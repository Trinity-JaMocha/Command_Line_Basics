# TERMINOLOGY CRASH COURSE

Linux
 # Open-Source & Free: The source code is free to study, modify, and redistribute, fostering a massive collaborative community.
 # The Kernel: At its core, the Linux kernel manages system resources, hardware, and memory.
 # Distributions (Distros): Instead of one single OS, users choose "flavors" (distros) that bundle the kernel with software, 
  # desktop environments, and tools tailored for specific needs (e.g., gaming, server management, or desktop use).

Shell
 # Command-Line Interpreter: The shell reads user input, parses it, and executes the requested programs.
 # Interaction Type: While often a Command-Line Interface (CLI), shells can also refer to Graphical User Interfaces (GUI).
 # Functionality: Beyond executing commands, shells can be used for file manipulation, environment variable configuration, 
  # and automation via scripting.
 # Automation: Users can store sequences of commands in a file (a shell script) to automate repetitive tasks. 

 -----------------------------------------------------

 Options
  # modifiers used with a command to alter its default behavior or customize its actions. They are distinct from arguments, 
  # which are the inputs the command acts upon.

# Delete a directory
rm -r [dir_name] 

# List items with detailed info
ls -l

--------------------------------------------------------

# ASIDE OPTIONS

rm -r [dir_name] # short options
rm --recursive [dir_name] # long options

--------------------------------------------------------

# TYPES OF OPTIONS

Short Options: # These are single letters preceded by a single hyphen (e.g., -v). They are concise and can often be 
 # combined (e.g., -la is the same as -l -a in many Unix-like systems).
Long Options: # These use descriptive keywords preceded by two hyphens (e.g., --verbose or --version). 
# They are easier to read and understand, especially in scripts.
Options with Values: # Many options require an additional value, such as a number or a path. For short options, 
# the value can immediately follow the option letter or be separated by a space (e.g., -h localhost or -hlocalhost), while long options often use an equal sign (e.g., --host=localhost).
Boolean Flags: # Some options act as simple on/off switches without an associated value (e.g., --force or --ignore-hold).
System-Specific Variations: # While Unix-based systems (Linux, macOS) primarily use hyphens, some Windows command-line tools 
# might use a forward slash (/) instead (e.g., /S for silent install).

------------------------------------------------------------

# FIND FILES AND DIRECTORIES

# Find Basics
 # Syntax
 find [path] [option] [expression]
 # EXAMPLE
 find . -name 'forest*'

# Find Options
- name 'forest*' # search by name
- iname 'forest*' # case insensitive search by name
type f / type d # search by type
-type d -iname 'forest*' # combine options

# Paths
../forests # relative file paths
- # current directory
.. # parent directory
~ # home directory
/ # root directory

-------------------------------------------------

# ASIDE: KILL A PROCESS

# Terminating a process
Ctrl + C: # This is the standard and most common way to gracefully terminate the program running in the current, 
 #active terminal session. It sends a SIGINT (interrupt) signal, allowing the process to perform cleanup before exiting.

# When to terminate a process
 # when it is unresponsive, consuming excessive system resources, or behaving maliciously or unexpectedly.

---------------------------------------------------

# RENAME, MOVE AND COPY

# Rename
mv old_name new_name # syntax
mv file1.txt newfile.txt # EXAMPLE

# Move
mv name location # syntax # if the location does not exist, mv will rename the item instead of moving it
mv capitals.txt geography_game/cities # EXAMPLE

# Copy
cp original name copy name # syntax
cp team.txt team_backup.txt # copy file EXAMPLE
cp -r cities cities_backup # copy directory

------------------------------------------------------
