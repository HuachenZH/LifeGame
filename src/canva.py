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
    """Prune the arrary.
    Before prune, all white dots are 256, black dots are 0
    After prune, all white dots are 0, black dots are 1

            Parameters:
                    arr (np.array): array transformed from the image

            Returns:
                    arr (np.array): array pruned.
    """
    # fun fact: if you change the order of the following two lines,
    # there will be error with the vector
    arr[arr < 128] = 1
    arr[arr >= 128] = 0
    return arr



# ------------------------79---------------------------------------------------
def canva2array(path_img:str):
    """Read vector from an image file. Returns an np arrary whose shape 
    corresponds to the image's width and height. In the array, all darker
    pixels become 1, all lighter pixels become 0.

    This function is sopposed to be called by another script.

            Parameters:
                    path_img (str): path to the input image

            Returns:
                    arr (np.array): image transformed into vector.
    """
    arr = img2arr(path_img)
    arr = prune_array(arr)
    return arr



if __name__ == "__main__":
    canva2array("../canvas/canva_small.jpg")