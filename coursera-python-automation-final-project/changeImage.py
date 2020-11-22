#!/usr/bin/env python3

import os
from PIL import Image

def change_images():
    """Resizes images to 600 x 100 and converts them from *.tif to *.jpeg format."""
    dir = "supplier-data/images/"

    for image in os.listdir(dir):
        # To skip system files such as ".DS_Store" and only process tiff files
        if not image.startswith('.') and image.endswith(".tif") or image.endswith(".tiff"):
            with Image.open(dir + image) as im:
                im = im.resize((600, 400))
                im = im.convert("RGB") # To be able to convert from *.tiff

                # Split path to file into path with filename and extension, then take path only
                # (which is just the filename in the current case)
                im.save(dir + os.path.splitext(image)[0] + ".jpeg")

def main():
    change_images()

main()