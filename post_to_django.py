#!/usr/bin/env python3

import os
import requests

def run():
        """Takes reviews from files, adds them to dictionaries and posts them to a website"""
        review_dir = "/data/feedback/"
        reviews_list = []
        reviews_dicts_list = []

        reviews_list = os.listdir(review_dir)

        for review in reviews_list:
                review_dict = {} # Initialize dictionary to hold current review
                review = review_dir + review
                with open(review) as file:
                        line = file.readline()
                        review_dict["title"] = line.rstrip("\n")
                        line = file.readline()
                        review_dict["name"] = line.rstrip("\n")
                        line = file.readline()
                        review_dict["date"] = line.rstrip("\n")
                        line = file.readline()
                        review_dict["feedback"] = line.rstrip("\n")
                        reviews_dicts_list.append(review_dict) # Stash current review into a list

        # Post reviews
        i = 0
        dicts_count = len(reviews_dicts_list)
        for dict in reviews_dicts_list:
                i +=1
                response = requests.post("http://<Django web server IP>/feedback/", data = dict)  # DON'T FORGET THE SLASH AT THE END!!!
                print("Processing review {} of {},  Status code: {}".format(i, dicts_count, response.status_code))

def main():
        run()


main()