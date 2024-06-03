#!/usr/bin/python3
"""
Script that uses REST API to fetch user's tasks and export them to CSV format.
"""

import csv
import requests
import sys


def make_csv(users, todos):
    """Turns payloads into CSV format"""
    titles = ["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"]

    with open(f"{users[0]['id']}.csv", "w", newline='') as f:
        writer = csv.DictWriter(f, fieldnames=titles, quoting=csv.QUOTE_ALL)
        writer.writeheader()
        for todo in todos:
            writer.writerow({
                "USER_ID": todo["userId"],
                "USERNAME": users[0]["username"],
                "TASK_COMPLETED_STATUS": todo["completed"],
                "TASK_TITLE": todo["title"]
            })


if __name__ == "__main__":
    if len(sys.argv) != 2 or not sys.argv[1].isdigit():
        print("Usage: ./script.py <employee_id>")
        sys.exit(1)

    employee_id = sys.argv[1]
    users = requests.get("https://jsonplaceholder.typicode.com/users", params={"id": employee_id}).json()
    todos = requests.get("https://jsonplaceholder.typicode.com/todos", params={"userId": employee_id}).json()

    make_csv(users, todos)

