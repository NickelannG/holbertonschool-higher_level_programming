#!/usr/bin/python3
"""
task_02_requests:
    This moudle contains the fetch_and_print_posts and
    fetch_and_save_posts functions
"""
import requests
import csv


def fetch_and_print_posts():
    """
    This function fetches all posts from JSONPlaceholder and
    prints out the titles of these posts if the GET request
    was successful.
    """
    r = requests.get('https://jsonplaceholder.typicode.com/posts')
    print(f"Status Code: {r.status_code}")

    if r.status_code == 200:
        parsed = r.json()
        for post in parsed:
            print(post['title'])


def fetch_and_save_posts():
    """
    This function fetches all posts from JSONPlaceholder and
    structures the data in a list of dictionaries according to
    "id", "title", and "body" and writes this data into a CSV file
    if the GET request was successful.
    """
    r = requests.get('https://jsonplaceholder.typicode.com/posts')
    if r.status_code == 200:
        list_dict = []  # list to put dictionaries
        parsed = r.json()
        for post in parsed:
            my_dict = {"id": post["id"], "title": post["title"],
                       "body": post["body"]}
            list_dict.append(my_dict)

        with open("posts.csv", "w", newline='') as f:  # Writing to csv file
            writer = csv.DictWriter(f, fieldnames=["id", "title", "body"])
            writer.writerows(list_dict)
