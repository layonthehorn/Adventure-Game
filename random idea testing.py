possible_locations = ("plaza",
                      "bunker",
                      "side room",
                      "small den",
                      "west wing",
                      "cemetery",
                      "toy shop",
                      "pet shop",
                      "upstairs hallway",
                      "animal den",
                      "shoe store",
                      "bathroom",)

map_dictionary = {
    "plaza": "MP",
    "bunker": "FS",
    "side room": "CR",
    "small den": "SD",
    "west wing": "WW",
    "cemetery": "C ",
    "toy shop": "TS",
    "pet shop": "PS",
    "upstairs hallway": "UH",
    "animal den": "AD",
    "shoe store": "SS",
    "bathroom": "RR",
}

location = "west wing"
if location:

#   0    1   2     3    4     5    6    7     8    9     10   11
    mp, up, pet, shoe, rest, ani, den, west, toy, cem, fall, com = ("MP", "UH", 'PS', 'SS', 'RR', 'AD', 'SD', 'WW', 'TS', 'C ', 'FS', 'CR')
    places = [mp, up, pet, shoe, rest, ani, den, west, toy, cem, fall, com]
    rooms = []
    for room in places:
        if map_dictionary.get(location) == room:

            rooms.append("@@")
        else:
            rooms.append(room)

    print(f"""
      ---------MAP----------
                                           +--------------------+
               {rooms[3]}                          |Legend:             |
               ||                          |                    |
           {rooms[5]}--{rooms[1]}--{rooms[4]}                      |Main Plaza: MP      |
        {rooms[9]}  {rooms[6]} ||                          |Upper Hall: UH      |
        ||   \\\\||                          |Pet Shop: PS        |
    {rooms[2]}--{rooms[7]}-----{rooms[0]}----EXIT                  |Shoe Store: SS      |
        ||     ||                          |Restroom: RR        |
        {rooms[8]}     {rooms[10]}--{rooms[11]}                      |Animal Den: AD      |
                                           |Small Den: SD       |
                                           |West wing: WW       |
                                           |Toy Shop: TS        |
                                           |Cemetery: C         |
                                           |Fallout Shelter: FS |
                                           |Computer Room: CR   |
                                           |You: @@             |
                                           +--------------------+  
           """)
# else:
#     print(map_of_building)
