import numpy as np

def access_tiles(file):
    #empty list
    departure = []
    classic_tiles = []
    arrival = []
    row_ind = 0
    #open csv file
    data = np.loadtxt(file,dtype=str, delimiter=';')
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
    return departure + classic_tiles + arrival

free_tiles = access_tiles('Structure.csv')
print(free_tiles.index((0,4)))
free_tiles