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


def canva(path_img:str):
    img2arr(path_img)



if __name__ == "__main__":
    canva("../canvas/canva_small.jpg")