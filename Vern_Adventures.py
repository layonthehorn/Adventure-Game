#!/usr/bin/env python3
from chapter_one import ChapterOne
# from chapter_two import ChapterTwo
import os
from os import environ
import platform
import getpass

# Temporary ascii art from https://ascii.co.uk/art/lion
ascii_image = """                 
                ,  ,, ,
           , ,; ; ;;  ; ;  ;
        , ; ';  ;  ;; .-''\\ ; ;
     , ;  ;`  ; ,; . / /7b \\ ; ;
     `; ; .;'         ;,\\7 |  ;  ;
      ` ;/   / `_      ; ;;    ;  ; ;
         |/.'  /0)    ;  ; `    ;  ; ;
        ,/'   /       ; ; ;  ;   ; ; ; ;
       /_   /         ;    ;  `    ;  ;
      `?7P"  .      ;  ; ; ; ;     ;  ;;
      | ;  .:: `     ;; ; ;   `  ;  ;
      `' `--._      ;;  ;;  ; ;   ;   ;
       `-..__..--''   ; ;    ;;   ; ;   ;
                   ;    ; ; ;   ;     ;

"""


# saving will not work the same on android
def check_android():
    if 'ANDROID_ARGUMENT' in environ or 'ANDROID_STORAGE' in environ:
        return True
    else:
        return False


operating = platform.system()
if (operating == 'Linux' or operating == "Darwin") and not check_android():
    # save location and clear if on linux or mac
    save_dir = f"/home/{getpass.getuser()}/Documents/vern_saves"
    clear = lambda: os.system("clear")
elif operating == 'Windows':
    # save location and clear if on windows
    save_dir = f"C:/Users/{getpass.getuser()}/Documents/vern_saves"
    clear = lambda: os.system("cls")
elif check_android():
    # android system found
    save_dir = os.path.join(os.getcwd(), "saves")
    clear = lambda: os.system("clear")
else:
    # unknown system
    save_dir = os.path.join(os.getcwd(), "saves")
    clear = lambda: None
# makes sure the save directory is a thing
try:
    if not os.path.isdir(save_dir):
        pick = input("Create Save directory? (y/n) ").lower()
        if pick == "y":
            os.makedirs(save_dir)
            print(f"Made save folder at, {save_dir}")
            input("Press Enter...")
        else:
            print("Saving will not be possible.")
            input("Press Enter...")

except IOError:
    print("Could not create save folder. Save feature will not work.")
    input("Press Enter...")

clear()
choosing = True
while choosing:
    print(ascii_image)
    print("Welcome to my game!")
    user_input = input("Which Chapter to play? (1, 2, or q to quit) ").lower()
    if user_input == "1":
        clear()
        # add True as parameter to enable debugging commands
        ChapterOne()
        clear()
    elif user_input == "2":
        clear()
        print("Not yet built.")
        # ChapterTwo()
    elif user_input == "q":
        clear()
        print("Goodbye!")
        choosing = False
        input("Press Enter...")
