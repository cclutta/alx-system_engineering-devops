#!/usr/bin/python3
"""
    Python script that exports data in the JSON format.
"""

import json
import requests
import sys

if __name__ == "__main__":
    id = sys.argv[1]
    user_url = "https://jsonplaceholder.typicode.com/users/{}".format(id)
    todos_url = "https://jsonplaceholder.typicode.com/users/{}/todos".format(id)

    user = requests.get(user_url).json()
    todos = requests.get(todos_url).json()

    with open('{}.json'.format(id), 'w') as json_file:
        tasks = []
        for t in todos:
            tasks.append({"task": t.get("title"),
                          "completed": t.get("completed"),
                          "username": user.get("username")})
        data = {"{}".format(id): tasks}
        json.dump(data, json_file)
