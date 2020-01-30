class ItemDictionary:
    def __init__(self):
        self.item_dictionary = {
            "wrench": "Used for unstucking random things. Always handy with robots.",
            "fuse": "Lots of old world tech uses this to keep power flowing.",
            "bag of catnip": "Hey now. You need to stay sober.",
            "lion plush": "A cute lion plush. I wonder who left this here?",
            "strange keys": "For some reason you recognise them. Maybe they belong to a friend?",
            "meat": "Maybe something will want this?",
            "toy raygun": "It's flashing random colors. Not useful but fun!",
            "knife": "It cuts. I mean what else do you think it does?",
            "fur sample": "It's fur. Maybe you could use it to get in the pet store?",
            "map": "A map to the mall! Someone must have updated it recently.",
            "drugged meat": "This would knockout anything that eats it.",
            "battery": "This could be used to power something, or overpower it.",
            "mane comb": "You could use this on your mane. Not that you ever need it."
        }

    # this allows the program to get descriptions for items
    def get_description(self, item):
        if item in self.item_dictionary:
            return self.item_dictionary[item]
        else:
            return "Missing Value! ERROR!"


if __name__ == "__main__":
    i_dict = ItemDictionary()
    for item in ["wrench", "map", "fuse", "bag of catnip", "lion plush", "meat", "toy raygun", "knife", "fur sample", "error testing"]:
        print("{:20}{:<5}".format(item, i_dict.get_description(item)))