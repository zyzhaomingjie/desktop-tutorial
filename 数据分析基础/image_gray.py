from numpy.core.multiarray import ndarray
import numpy as np
from PIL import Image


def image_gray(image_ar: ndarray) -> ndarray:
    row, col, channel = image_ar.shape
    grey_image_array = np.zeros((row, col))
    for i in range(row):
        for j in range(col):
            grey_image_array[i, j] = 1/3*image_ar[i,j,0] + 1/3*image_ar[i,j,1] +1/3*image_ar[i,j,2]
    return grey_image_array


def read_image(image_path: str) -> ndarray:
    image = Image.open(image_path)
    return np.array(image)


def show_image_array(image_ar: ndarray):
    image = Image.fromarray(image_ar)
    image.show()


if __name__ == "__main__":
    image_array = read_image('image.jpg')
    array = image_gray(image_array)
    show_image_array(array)