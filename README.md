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

## cars.py

This script:
- Uses reports.py
- Uses emails.py
- Uses car_sales.json

## coursera-python-automation-final-project

Contains scripts that:
- Summarize and process sales data into different categories
- Generate a PDF (artifact included)
- Automatically send the PDF by email
- Check the health status of the system
- Send an email if the system has problems
