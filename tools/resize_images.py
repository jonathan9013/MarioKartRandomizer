from os import listdir
from PIL import Image

# get the path/directory
folder_dir = r"app\media\cups"
for images in listdir(folder_dir):
    image_dir = folder_dir + '\\' + images
    im1 = Image.open(image_dir)

    # use base width
    basewidth = 120
    wpercent = (basewidth/float(im1.size[0]))
    hsize = int((float(im1.size[1])*float(wpercent)))
    im1 = im1.resize((basewidth, hsize), Image.Resampling.LANCZOS)

    # use base height
    # baseheight = 80
    # wpercent = (baseheight/float(im1.size[1]))
    # wsize = int((float(im1.size[0])*float(wpercent)))
    # im1 = im1.resize((wsize, baseheight), Image.Resampling.LANCZOS)

    im1.save(image_dir, mode='r')
    print(images)
