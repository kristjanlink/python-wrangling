#!/usr/bin/env python3

import os
import requests

def upload_images():
    dir = "supplier-data/images/"
    url = "http://localhost/upload/" # DON'T FORGET THE SLASH AT THE END!!!

    for image in os.listdir(dir):
        # To only process jpeg files
        if image.endswith(".jpeg"):
            with open(dir + image, "rb") as img:
                response = requests.post(url, files = {"file": img})

def main():
    upload_images()

main()