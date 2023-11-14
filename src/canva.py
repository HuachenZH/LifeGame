from PIL import Image
import numpy as np

import pdb

# ------------------------79---------------------------------------------------

def img2arr(path_img:str) -> np.array:
    """Read an image and transform to np array.

            Parameters:
                    path_img (str): path to the input image

            Returns:
                    arr (np.array): the image in vector format.
    """
    img = Image.open(path_img)
    # convert to greyscale, so that instead of having an array of three
    # dimensions (RGB), there is only one dimension left
    img = img.convert("L")
    arr = np.array(img)
    return arr


def prune_array(arr:np.array) -> np.array:
    # before prune, all white dots are 256, black dots are 0
    # i want that after prune, all white dots are 0, black dots are 1
    
    # fun fact: if you change the order of the following two lines,
    # there will be error with the vector
    arr[arr < 128] = 1
    arr[arr >= 128] = 0
    return arr

def canva(path_img:str):
    arr = img2arr(path_img)
    arr = prune_array(arr)



if __name__ == "__main__":
    canva("../canvas/canva_small.jpg")