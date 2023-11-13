# ver-00 PROTOTYPE
# author: Rei

import numpy as np
from PIL import Image
import time
import os

def prepareArr(filepath:str) -> np.array:
    '''
    Prepare the array (the initial state)

    Parameters
    ----------
    filepath : str
        file path + name of the input image.
        e.g. D:/folder/initialState.png

    Returns
    -------
    arr : numpy array
        The initial state presented in numpy array.
        0 = dead cell
        1 = live cell

    '''
    # get canva
    # canva must be black and white, white for dead cell, black for live cell
    img = Image.open(filepath)
    arr_rgb = np.array(img)
    # arr_rgb is three dimensional.
    # as canva is in black white, we only need one of the three pages
    
    arr = arr_rgb.copy()[:,:,0]
    # here we have 255 for dead cell and 0 for live cell
    # transform arr to the following: 0 for dead cell and 1 for live cell
    with np.nditer(arr, op_flags=['readwrite']) as it:
    # iterate through np array and modify array values
    # https://numpy.org/doc/stable/reference/arrays.nditer.html
        for x in it:
            x[...] = 0 if x[...] > 100 else 1
            # whenTrue if condition else whenFalse
        del x
        del it
    return arr


def painting(arr: np.array, mappingDict: dict) -> str:
    canvas = ''
    for row in arr:
        for element in row:
            canvas += mappingDict[str(int(element))]
        canvas += "\n"
    return canvas


  
if __name__ == "__main__":
    arr = prepareArr("canva1.png")
    mappingDict = {'0': ' ', '1': '@'}
    # print the initial state
    canvas = painting(arr, mappingDict)
    print(canvas)
    
    
    # deux pistes
    # soit créer next à partir de zéro
    # soit cloner next depuis arr
    
    
    # start iteration
    # while True:
    while True:
        # iterate through each element of the array
        nextgen = arr.copy()
        for irow in range(arr.shape[0]):
            for icol in range(arr.shape[1]):
                # check its neighbours, 
                neighboursAlive = np.sum(arr[irow-1:irow+2, icol-1:icol+2]) - arr[irow,icol]
                # determine whether the cell is dead or live for the next generation
                # any live cell with 2 or 3 live neighbours survives
                # otherwise the live cell dies for the next generation
                if arr[irow,icol] == 1: # if it s a live cell
                    if neighboursAlive == 2 or neighboursAlive == 3:
                        nextgen[irow,icol] = 1
                    else:
                        nextgen[irow,icol] = 0
                # any dead cell with exactly 3 neighbours becomes a live cell
                # otherwise its still dead
                else: # if it s a dead cell
                    if neighboursAlive == 3:
                        nextgen[irow,icol] = 1
                    else:
                        nextgen[irow,icol] = 0
        arr = nextgen.copy()
                # # if cur[r, c] == 1 and num_alive < 2 or num_alive > 3:
                # if arr[irow, icol] == 1 and neighboursAlive < 2 or neighboursAlive > 3:
                #     # about to die
                #     arr[irow, icol] = 0
                # # elif (cur[r, c] == 1 and 2 <= num_alive <= 3) or (cur[r, c] == 0 and num_alive == 3):
                # elif (arr[irow, icol] ==1 and 2 <= neighboursAlive <= 3) or arr[irow, icol] == 0 and neighboursAlive == 3:
                #     # about ot live
        canvas = painting(arr, mappingDict)
        # clean the screen then print the result
        time.sleep(0.25)
        # print('\x1b[2J')
        os.system('cls')
        print(canvas)