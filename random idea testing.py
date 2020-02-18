
# def climb_ladder(room_inventory):
#
#     if "rope" in room_inventory:
#         print("That rope is too weak. I'm not going to climb it.")
#     elif "strong rope" in room_inventory:
#         print("Ok, I'm heading down.")
#     else:
#         print("I need to find something to get down with first.")
#
#
# inv = input("w, or s.")
# if inv == "w":
#     data = ["rope"]
# elif inv == "s":
#     data = ["strong rope"]
# else:
#     data = [None]
# climb_ladder(data)

combo_dict = {
    ("fish","lion"): "1st",
    ("testing", "newthing"): "2nd"
}

print(combo_dict.get(("lion","fish")))
