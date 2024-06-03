#!/usr/bin/python3
"""
Export user's tasks to a CSV file.
"""

import csv
import requests
import sys


def fetch_user_and_todos(employee_id):
    user_response = requests.get(f"https://jsonplaceholder.typicode.com/users/{employee_id}")
    todos_response = requests.get(f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}")

    if user_response.status_code != 200 or todos_response.status_code != 200:
        print("Error: Unable to fetch data")
        sys.exit(1)

    user = user_response.json()
    todos = todos_response.json()

    return user, todos


def export_to_csv(user, todos):
    user_id = user["id"]
    user_name = user["username"]
    file_name = f"{user_id}.csv"

    with open(file_name, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])

        for todo in todos:
            writer.writerow([user_id, user_name, todo["completed"], todo["title"]])


if __name__ == "__main__":
    if len(sys.argv) != 2 or not sys.argv[1].isdigit():
        print("Usage: ./1-export_to_CSV.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    user, todos = fetch_user_and_todos(employee_id)
    export_to_csv(user, todos)

