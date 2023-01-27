#Extra Text Files
#Librarys

from post import post
from datetime import datetime
import os

#Deffs

#setting the variables
def set_vars(userpastime):
    username = str(userpastime[0])
    password2 = userpastime[1]
    temp = userpastime[2].split(" ")
    pasttime = temp[0].split("-")
    pasttime += temp[1].split(":")
    lstlgmath = datetime.now().minute - int(pasttime[4])
    return username,password2,pasttime,lstlgmath

#Sets the username stuff from a text file
with open(rf'{os.getcwd()}\python\CSEfiles\3.2.2\unpasllin.txt', "r+") as file:
    userpastime = file.read().split(',')
    username, password2, pasttime, lstlgmath = set_vars(userpastime)
    file.close()
#Sets there posts from a text file
with open(rf'{os.getcwd()}\python\CSEfiles\3.2.2\posts.txt', "r+") as file:
    all_posts_archive = file.read().split(',')
    file.close()
#Writes stuff to the files
def wrighttofile(username, password2, all_posts_archive):
    #Wrights username and past and the time of day to the file
    with open(rf'{os.getcwd()}\python\CSEfiles\3.2.2\unpasllin.txt', "w") as file:
        file.write(f"{username},{password2},{datetime.now().replace(microsecond=0)}")
        file.close()
    #Writes all the posts to there file
    with open(rf'{os.getcwd()}\python\CSEfiles\3.2.2\posts.txt', "w") as file:
        for i in all_posts_archive:
                file.write(i + ",")
        file.close()
#Changes there username and writes it
def userchange(username):
    username = input("What do you want your username?\n")
    wrighttofile(username, password2, all_posts_archive)
    return username
#Checks what they want to do at the start
def userinput():
    user_input = str.lower(input("Do you want to;\n\033[1;33mAdd\033[1;0m a new post, \033[1;31mRemove\033[1;0m a post,\n\033[1;32mChange\033[1;0m your \033[1;34mUsername\033[1;0m, \033[1;32mChange\033[1;0m your \033[1;34mPassword\033[1;0m, \n\033[1;35mPrint\033[1;0m all posts, or \033[1;31mQuit\033[1;0m the program?\n"))
    return user_input

#Variables

loop = 0
username, password2, pasttime, lstlgmath = set_vars(userpastime)
breakk = 0
logged = 0

#Setting the username if it is empty
if username == " ":
    username = userchange(username)
print(f"Welcome back, {username}!")
#The main loop that goes untill it is no longer needed
while breakk != 1:
    #Check the when they last logged into, to see if it was < 5 mins ago
    if logged != 0 or datetime.now().year == int(pasttime[0]) and datetime.now().month == int(pasttime[1]) and datetime.now().day == int(pasttime[2]) and datetime.now().hour == int(pasttime[3]) and lstlgmath < 5:
        user_input = userinput()
        # Checking if they asked to add something, but not the other things
        if "add" in user_input or "new" in user_input:
            message = input("What do you want to add in the post\n")
            all_posts_archive.append(str(post(username, message))) #adds new post to the list
            wrighttofile(username, password2, all_posts_archive)
        #Checks if you asked to Check if you asked to Change or Username or password
        elif "change" in user_input or "username" in user_input or "password":
            breakk = 0
            while True:
                #Checking if they asked for username
                if "username" in user_input:
                    username = userchange(username)
                    print(f"Your new name is {username}!")
                    break
                #Checking if they asked for Password
                elif "password" in user_input:
                    user_input = input("What do you want to change your passward to?\n")
                    input2 = input("What is your current passward?\n")
                    while True:
                        if input2 == password2:
                            #Conferming that they wanted to change
                            input2 = str.lower(input("Conferm you want to change your passward. Y, N\n"))
                            #if you wanted to it sets it and wrights it to the text file
                            if "y" in input2:
                                password2 = user_input
                                wrighttofile(username, password2, all_posts_archive)
                                breakk = 1
                                break
                            #If no then it leaves
                            elif "n" in input2:
                                print("Ok leaving new passward")
                                breakk = 1
                                break
                            else:
                                print("Incorrect input try again!")
                        #If they got the password wrong then they only get 3 trys
                        elif loop < 2:
                            print(f"Incorrect passward, you have {3-loop} trys left.")
                            loop+1
                        #if wrong 3 times then kill
                        else:
                            print("Incorrect passward, leaving selection")
                            break
                        breakk = 0
                #If they don't set username or password to change.
                elif("change" in user_input):
                    user_input = str.lower(input("What do you want to change your Username or Passward?\n"))
                if breakk != 0:
                    break
        #Checks if they want to remove something from there list
        elif "remove" in user_input:
            while True:
                print("\n")
                for i in all_posts_archive:
                    print(i)
                print("\n")
                #Tells them how many things there are
                index2 = input(f"What post do you want to remove there are {len(all_posts_archive)+1} posts in your archive.\nWhich one do you want to remvove? 1-{len(all_posts_archive)+1}\n")-1
                #if there input is a number then remove it
                while True:
                    if index2.isnumeric():
                        print("incorrect input")
                    #Else remove the string
                    else:
                        all_posts_archive.remove(index2)
                        break
        #See if they want to Print all posts
        elif "print" in user_input or "all" in user_input:
            print("\n")
            for i in all_posts_archive:
                print(i)
                #Checks to not print the last thing in the list that will always be " "
                if loop != len(all_posts_archive):
                    print(i)
            #print("\n")
        #See if they want to quit
        elif "quit" in user_input:
            breakk = 0
            print('in')
            while True:
                yn = str.lower(input("Conferm you want to exit. Y, N\n"))
                if "y" in yn:
                    wrighttofile(username, password2, all_posts_archive)
                    breakk = 1
                    break
                elif "n" in yn:
                    break
                else:
                    print("error")
        else:
            print("error try inputing again.")
        user_input = userinput()
    else:
        #If they have been logged lot because of time.
        while True:
            input2 = input("You have been logged out.\nWhat is your password?\n")
            if input2 == password2:
                print("You have been logged in!")
                wrighttofile(username, password2, all_posts_archive)
                username, password2, pasttime, lstlgmath = set_vars(userpastime)
                logged = 1
                break
            elif loop < 2:
                print(f"Incorrect password! You have {3-loop} trys left!")
                loop += 1
            else:
                print("Incorrect password! Will now kill the program")