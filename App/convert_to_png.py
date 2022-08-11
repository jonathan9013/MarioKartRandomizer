import os
from os import listdir
from PIL import Image

# get the path/directory
folder_dir = "C:\Dev\MarioKartRandomizerApp\MarioKartRandomizer\\app\media\\tires"
for images in os.listdir(folder_dir):

    # check if the image ends with png
    if (images.endswith(".png")):
        image_dir = folder_dir + '\\' + images
        im1 = Image.open(image_dir, mode='r')
        im1.save(image_dir, mode='r')
        print(images)