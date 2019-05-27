import numpy as np

def access_tiles2(file):
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
            #J'AURAIS AIMÉ FAIRE UN CASE MAIS CE N'EST PAS POSSIBLE
            #ET AVEC UN DICTIONNAIRE, J'AI L'IMPRESSION QUE JE NE PEUX PAS METTRE DE ROW_IND COL_IND
            if cell == '1':
                classic_tiles.append((row_ind, col_ind))
            else:
                if cell == 'D':
                    departure.append((row_ind, col_ind))
                else:
                    if cell == 'A':
                        arrival.append((row_ind, col_ind))
            col_ind += 1
        row_ind +=1
    #return complete list
    return (departure, classic_tiles, arrival)

free_tiles = access_tiles2('Structure.csv')
free_tiles[1]