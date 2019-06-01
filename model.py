import numpy as np

class Map:
    """arg = csv with 0, 1, D, A with separator ;"""

    def __init__(self, map):
        #empty list
        departure = []
        classic_tiles = []
        arrival = []
        row_ind = 0
        #open csv file
        data = np.loadtxt(map,dtype=str, delimiter=';')
        # iterate on rows and cols to get accessible tiles
        for row in data:
            col_ind = 0
            for cell in row:
                if cell == '1':
                    classic_tiles.append((row_ind, col_ind))
                elif cell == 'D':
                    departure.append((row_ind, col_ind))
                elif cell == 'A':
                    arrival.append((row_ind, col_ind))
                col_ind += 1
            row_ind +=1
        #return complete list [D, accessibles, A]
        self.map = departure + classic_tiles + arrival

class Object:
    """Object type """
    def __init__(self, type, position):
        self.type = type
        self.position = position

    @classmethod
    def taken(cls):
        pass

class Person:
    def __init__(self, type, position, dress):
        self.type = type
        self.position = position
        self.dress = dress

    @classmethod
    def initialize(cls):
        #position
        #dress
        pass

    def move(cls):
        #wounded/die
        #take
        pass

def main():
    #initialize Map
    main_map = Map('Structure.csv')
    #place object on the Map
    #place persons on the Map
    print(main_map.map)

main()
