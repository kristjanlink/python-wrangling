#!/usr/bin/env python3

import os
from PIL import Image

def process_icons():
	"""Rotates images 90 degrees clockwise, resizes them to 128 x 128 and saves them in *.jpeg format."""

	for image in os.listdir("images"):
		if not image.startswith('.'): # To skip system files such as ".DS_Store"
			with Image.open("images/" + image) as im:
				im = im.rotate(90)
				im = im.resize((128, 128))
				im = im.convert("RGB") # To be able to convert from *.tiff
				# Split path to file into path with filename and extension, then take path only
				# (which is just the filename in the current case)
				im.save("/opt/icons/" + os.path.splitext(image)[0], "JPEG")

def main():
	process_icons()

main()
