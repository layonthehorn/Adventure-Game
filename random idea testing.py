class Simple:
    def __init__(self):
        self.stat_dictionary = {"look": 1000,
                                "inventory": 0,
                                "get": 10,
                                "help": 100,
                                "": 0,
                                "operate": 0,
                                "combine": 0,
                                "drop": 0,
                                "score": 0,
                                "use": 0,
                                "go": 0,
                                "save": 0,
                                "hint": 0,
                                "end": 0,
                                "unknown": 0,
                                "stat": 0}

#     def print_outro(self):
#         print(f"""
# Statics Of Command Usage
# {"Used look":<16} {self.stat_dictionary["look"]:<3} times. {"":>6} {"Used go":<16} {self.stat_dictionary["go"]:<3} times.
# {"Used inventory":<16} {self.stat_dictionary["inventory"]:<3} times. {"":>6} {"Used go":<16} {self.stat_dictionary["go"]:<3} times.
# {"Used get":<16} {self.stat_dictionary["get"]:<3} times.
# {"Used help":<16} {self.stat_dictionary["help"]:<3} times.
# {"Entered Nothing":<16} {self.stat_dictionary[""]:<3} times.
# {"Used operate":<16} {self.stat_dictionary["operate"]:<3} times.
# {"Used combine":<16} {self.stat_dictionary["combine"]:<3} times.
# {"Used drop":<16} {self.stat_dictionary["drop"]:<3} times.
# {"Used score":<16} {self.stat_dictionary["score"]:<3} times.
# {"Used use":<16} {self.stat_dictionary["use"]:<3} times.
# {"Used go":<16} {self.stat_dictionary["go"]:<3} times.
# {"Used save":<16} {self.stat_dictionary["save"]:<3} times.
# {"Used hint":<16} {self.stat_dictionary["help"]:<3} times.
# {"Used end":<16} {self.stat_dictionary[""]:<3} times.
# {"Used unknown":<16} {self.stat_dictionary["unknown"]:<3} times.""")
    def print_stats(self):
        print(f"""
\t\t\t\t\tStatistics Of Command Usage

{"Used 'look'":<16} {self.stat_dictionary["look"]:<4} times. {"":>6} {"Used 'get'":<16} {self.stat_dictionary["get"]:<4} times.
{"Used 'inventory'":<16} {self.stat_dictionary["inventory"]:<4} times. {"":>6} {"Used 'help'":<16} {self.stat_dictionary["help"]:<4} times.
{"Used 'end'":<16} {self.stat_dictionary[""]:<4} times. {"":>6} {"Used 'operate'":<16} {self.stat_dictionary["operate"]:<4} times.
{"Used 'combine'":<16} {self.stat_dictionary["combine"]:<4} times. {"":>6} {"Used 'drop'":<16} {self.stat_dictionary["drop"]:<4} times.
{"Used 'score'":<16} {self.stat_dictionary["score"]:<4} times. {"":>6} {"Used 'use'":<16} {self.stat_dictionary["use"]:<4} times.
{"Used 'go'":<16} {self.stat_dictionary["go"]:<4} times. {"":>6} {"Used 'save'":<16} {self.stat_dictionary["save"]:<4} times.
{"Used 'hint'":<16} {self.stat_dictionary["help"]:<4} times. {"":>6} {"Used 'stat'":<16} {self.stat_dictionary["stat"]:<4} times.
{"Unknown command":<16} {self.stat_dictionary["unknown"]:<4} times. {"":>6} {"Entered nothing":<16} {self.stat_dictionary[""]:<4} times.""")

thingy = Simple()
thingy.print_stats()
