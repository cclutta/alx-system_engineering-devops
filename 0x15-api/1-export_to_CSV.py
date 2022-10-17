#!/usr/bin/python3
"""
    Python script that exports data to CSV
"""

import csv
import requests
import sys

if __name__ == "__main__":
    id = sys.argv[1]
    user_url = "https://jsonplaceholder.typicode.com/users/{}".format(id)
    todo_url = "https://jsonplaceholder.typicode.com/users/{}/todos".format(id)

    usr = requests.get(user_url).json()
    todos = requests.get(todo_url).json()

    with open('{}.csv'.format(id), 'w') as csv_file:
        csv_writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
        for t in todos:
            row = [id, usr.get("username"), t.get("completed"), t.get("title")]
            row = [str(value) for value in row]
            csv_writer.writerow(row)
