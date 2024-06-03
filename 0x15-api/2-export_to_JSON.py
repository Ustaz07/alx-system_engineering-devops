#!/usr/bin/python3
"""
Script that uses REST API to fetch user's tasks and export them to JSON format.
"""

import json
import requests
import sys


def make_json(users, todos):
    """Turns payloads into JSON format"""
    user_id = users[0]['id']
    username = users[0]['username']
    tasks = [{"task": todo['title'], "completed": todo['completed'],
              "username": username} for todo in todos]

    with open(f"{user_id}.json", "w") as f:
        json.dump({user_id: tasks}, f)


if __name__ == "__main__":
    if len(sys.argv) != 2 or not sys.argv[1].isdigit():
        print("Usage: ./script.py <employee_id>")
        sys.exit(1)

    employee_id = sys.argv[1]
    users = requests.get(
        "https://jsonplaceholder.typicode.com/users", params={"id": employee_id}).json()
    todos = requests.get("https://jsonplaceholder.typicode.com/todos",
                         params={"userId": employee_id}).json()

    make_json(users, todos)
