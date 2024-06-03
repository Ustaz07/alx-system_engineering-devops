#!/usr/bin/python3
"""
Fetches and displays TODO list progress for a given employee ID.
"""

import requests
import sys


def fetch_employee_data(employee_id):
    user_url = f'https://jsonplaceholder.typicode.com/users/{employee_id}'
    todos_url = f'https://jsonplaceholder.typicode.com/todos?userId={employee_id}'

    user_response = requests.get(user_url)
    todos_response = requests.get(todos_url)

    if user_response.status_code != 200 or todos_response.status_code != 200:
        print("Error: Unable to fetch data")
        sys.exit(1)

    user = user_response.json()
    todos = todos_response.json()

    return user, todos


def display_todo_progress(employee_id):
    user, todos = fetch_employee_data(employee_id)

    employee_name = user.get('name')
    total_tasks = len(todos)
    done_tasks = [todo for todo in todos if todo.get('completed')]
    num_done_tasks = len(done_tasks)

    print(f"Employee {employee_name} is done with tasks({num_done_tasks}/{total_tasks}):")
    for task in done_tasks:
        print(f"\t {task.get('title')}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Error: Employee ID must be an integer")
        sys.exit(1)

    display_todo_progress(employee_id)

