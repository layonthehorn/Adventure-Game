#!/usr/bin/env python3
from chapter_one import ChapterOne
# from chapter_two import ChapterTwo
import os
import platform
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

# makes sure the save directory is a thing
try:
    save_dir = os.path.join(os.getcwd(), "saves")
    # print(save_dir)
    if not os.path.isdir(save_dir):
        os.makedirs(save_dir)
except IOError:
    print("Could not create save folder. Save feature will not work.")


# allows me to clear the screen when playing
def clear():
    operating = platform.system()
    if operating == 'Linux' or operating == "Darwin":
        os.system("clear")
    elif operating == 'Windows':
        os.system('cls')


choosing = True
while choosing:
    print(ascii_image)
    print("Welcome to my game!")
    user_input = input("Which Chapter to play? (1, 2, or q to quit) ").lower()
    if user_input == "1":
        clear()
        ChapterOne(True)
        clear()
    elif user_input == "2":
        clear()
        print("Not yet built.")
        # ChapterTwo()
    elif user_input == "q":
        clear()
        print("Good bye!")
        choosing = False
        input("")
