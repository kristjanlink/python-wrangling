# python-wrangling
Python code portfolio

## process-icons.py

This script:
- Opens all files in subdirectory "images"
- Rotates them clockwise 90 degrees
- Resizes them to 128 x 128 pixels
- Converts them to JPEG format
- Saves them to "/opt/icons/"

## post-to-django.py

This script:
- Iterates through a directory of text files with 4 rows
- Adds each row to a dictionary with the following keys, respectively:
  * "title"
  * "name"
  * "date"
  * "feedback"
- Adds each dictionary to a list
- Iterates through the list of dictionaries
- Posts each dictionary to a Django page using the requests module
