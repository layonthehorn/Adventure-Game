#!/usr/bin/env python3
from chapter_one import ChapterOne

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

choosing = True

while choosing:
    print(ascii_image)
    print("Welcome to my game!")
    user_input = input("Which Chapter to play? (1, 2, or q to quit) ").lower()
    if user_input == "1":
        ChapterOne()
    elif user_input == "2":
        print("Not Yet Made.")
    elif user_input == "q":
        print("Good bye!")
        choosing = False
        input("")
