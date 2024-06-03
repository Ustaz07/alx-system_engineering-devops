import json
import requests


def make_all(users=None, todos=None):
    """Turns all payloads into JSON format"""
    alljson = {}
    for user in users:
        user_id = user.get("id")
        user_tasks = []
        for todo in todos:
            if user_id == todo.get("userId"):
                user_tasks.append({"username": user.get("username"),
                                   "task": todo.get("title"),
                                   "completed": todo.get("completed")})
        alljson[str(user_id)] = user_tasks

    with open("todo_all_employees.json", "w") as f:
        json.dump(alljson, f)


if __name__ == "__main__":
    users = requests.get("https://jsonplaceholder.typicode.com/users/").json()
    todos = requests.get("https://jsonplaceholder.typicode.com/todos/").json()

    make_all(users, todos)
