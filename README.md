# bootcamp
# Part A - Account Creation
## 0: Creating a GitHub account
Go to github.com and create an account. After you have verified your email, create an empty repository in your new account, and name it bootcamp

# Part B - Terminal Commands
## 1: Our first command
Write a command that prints out the string “hello, world”. Extra credit: As in Listing 1, do it two different ways, both with and without using quotation marks.

print("Hello, World!")

> greeting = "Hello, World"
> print(greeting)

## 2: Cleaning up
Clear the contents of the current tab.

1. exit the program you were running - for example if you were using python on power shell use the function exit() and enter

1. type 'clear' and enter

## 3: Listing
What’s the command to list all the files (and directories) on your Desktop directory?

ensure you are in the desktop directory before using the command 
the command is - ls

if you are not in the desktop directory use the comand 'pwd' to check the current path to the directory you are in 
check if the desktop directory exist in the current directory by listing all directories with the comand 'ls'
change from the current directory to the desktop directory by using the below comand 'cd' followed by the path to the desktop directoy e.g 
cd \Users\username\Desktop

you can use the comand cd .. to move back up one directory if you navigate to wrong directory 

'username being my username on my PC'
## 4: Making directories
Make the directory bootcamp on your Desktop and, within it, the directory labs (i.e., ~/Desktop/bootcamp/labs).

mkdir \Users\username\Desktop\bootcamp
mkdir \Users\username\Desktop\bootcamp\labs

'username being my username on my PC'
## 5: Navigating directories
Change to your Desktop, then change to bootcamp directory, and then the lab directory.

cd \Users\username\Desktop
cd \Users\username\Desktop\bootcamp
cd \Users\username\Desktop\bootcamp\labs

'username being my username on my PC'
## 6: Creating files
Create an empty file called file01 in the lab directory.

cat >file1.txt
press exit to return to comand

## 7: Deleting directories
What is the command used to remove a directory named food and everything inside it.

rm -r food

# Part C - Github
## 8: Download the GitHub desktop application
Download the GitHub desktop application.

## 9: Pushing work to GitHub
Using the GitHub desktop application, push your code to your new repository.
 
