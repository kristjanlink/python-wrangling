#!/usr/bin/env python3

import os
import requests


def run():
    desc_dir = "supplier-data/descriptions/" # This works only when in directory "Python Coding/6 Automating Real-World Tasks with Python/Project 4/"
    desc_list = []
    fruit_dicts_list = []

    desc_list = os.listdir(desc_dir)

    for desc in desc_list:
        fruit_dict = {} # Initialize dictionary to hold current fruit
        desc_with_path = desc_dir + desc
        with open(desc_with_path) as file:
            line = file.readline()
            fruit_dict["name"] = line.rstrip("\n")
            line = file.readline()
            fruit_dict["weight"] = line.rstrip(" lbs\n")
            line = file.readline()
            fruit_dict["description"] = line.rstrip("\n")
            fruit_dict["image_name"] = os.path.splitext(desc)[0] + ".jpeg"
            fruit_dicts_list.append(fruit_dict) # Stash current fruit into a dictionary


	# Post reviews
    i = 0
    dicts_count = len(fruit_dicts_list)
    for dict in fruit_dicts_list:
        i += 1
        response = requests.post("http://<Django web server IP>/fruits/", data = dict) # DON'T FORGET THE SLASH AT THE END!!!
        print("Processed fruit {} of {},  Status code: {}".format(i, dicts_count, response.status_code))


def main():
    run()


main()