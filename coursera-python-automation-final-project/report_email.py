#!/usr/bin/env python3

import datetime
import emails # custom module
import os
import reports # custom module
# does sys need to be imported?


def run():
    desc_dir = "supplier-data/descriptions/" # This works only when in directory "Python Coding/6 Automating Real-World Tasks with Python/Project 4/"
    desc_list = os.listdir(desc_dir)
    formatted_date = datetime.date.today().strftime("%B %d, %Y")
    fruit_paragraph = ""
    report_path = "/tmp/processed.pdf"

    for desc in desc_list:
        desc_with_path = desc_dir + desc
        with open(desc_with_path) as file:
            line = file.readline()
            fruit_paragraph += "name: " + line.rstrip("\n") + "<br/>"
            line = file.readline()
            fruit_paragraph += "weight: " + line.rstrip("\n") + "<br/><br/>"

    reports.generate_report(report_path, "Processed Update on " + formatted_date, fruit_paragraph)

    # Send the PDF report as an email attachment
    message = emails.generate_email(
                                   "automation@example.com",
                                   "{}@example.com".format(os.environ.get('USER')),
                                   "Upload Completed - Online Fruit Store",
                                   "All fruits are uploaded to our website successfully. A detailed list is attached to this email.",
                                   report_path
                                   )
    emails.send_email(message)

def main(): # Does it need an argv parameter?
    run()


if __name__ == "__main__":
    main() # Does it need a sys.argv parameter?