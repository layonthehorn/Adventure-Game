# no longer used. Moved to player class...
import time


class MapOfBuilding:
    def __init__(self):
        self.map_of_building = """
   ---------MAP----------
                                        +--------------------+
            SS                          |Legend:             |
            ||                          |                    |
        AD--UP--RR                      |Main Plaza: MP      |
     C   SD ||                          |Upper Hall: UH      |
     ||   \\\\||                          |Pet Shop: PS        |
 PS--WW-----MP----EXIT                  |Shoe Store: SS      |
     ||     ||                          |Restroom: RR        |
     TS     FS--CR                      |Animal Den: AD      |
                                        |Small Den: SD       |
                                        |West wing: WW       |
                                        |Toy Shop: TS        |
                                        |Cemetery: C         |
                                        |Fallout Shelter: FS |
                                        |Computer Room: CR   |
                                        |                    |
                                        +--------------------+  
        """

    # print map of building
    def print_map(self):
        print("Let me check my map.\n*Map crinkling sounds.*")
        time.sleep(1.5)
        print(self.map_of_building)


if __name__ == "__main__":
    map_b = MapOfBuilding()
    map_b.print_map()
