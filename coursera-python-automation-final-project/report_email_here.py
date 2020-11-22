#!/usr/bin/env python3

import datetime
import os
import reports


def run():
    desc_dir = "supplier-data/descriptions/" # This works only when in directory "Python Coding/6 Automating Real-World Tasks with Python/Project 4/"
    desc_list = os.listdir(desc_dir)
    formatted_date = datetime.date.today().strftime("%B %d, %Y")
    fruit_paragraph = ""

    for desc in desc_list:
        desc_with_path = desc_dir + desc
        with open(desc_with_path) as file:
            line = file.readline()
            fruit_paragraph += "name: " + line.rstrip("\n") + "<br/>"
            line = file.readline()
            fruit_paragraph += "weight: " + line.rstrip("\n") + "<br/><br/>"
    
    reports.generate_report("processed.pdf", "Processed Update on " + formatted_date, fruit_paragraph)

def main():
    run()


main()