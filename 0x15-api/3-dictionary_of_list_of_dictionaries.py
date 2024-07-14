#!/usr/bin/python3
"""extend your Python script to export data in the JSON format"""
import json
import requests


def make_all(users=None, todos=None):
    """Turns all payloads into JSON format"""
    alljson = {}
    for user in users:
        user_id = user.get("id")
        username = user.get("username")
        user_tasks = [
            {
                "username": username,
                "task": todo.get("title"),
                "completed": todo.get("completed"),
            }
            for todo in todos
            if todo.get("userId") == user_id
        ]
        alljson[user_id] = user_tasks

    with open("todo_all_employees.json", "w") as f:
        json.dump(alljson, f)


if __name__ == "__main__":
    users = requests.get("https://jsonplaceholder.typicode.com/users/").json()
    todos = requests.get("https://jsonplaceholder.typicode.com/todos/").json()

    make_all(users, todos)
