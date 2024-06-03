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

def validate_csv(user, todos):
    user_id = user["id"]
    user_name = user["username"]
    expected_file_name = f"{user_id}.csv"
    expected_num_tasks = len(todos)

    # Check if CSV file exists
    try:
        with open(expected_file_name, newline='') as file:
            reader = csv.reader(file)
            header = next(reader)
            actual_num_tasks = sum(1 for row in reader)
            return header == ["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"] and \
                   actual_num_tasks == expected_num_tasks
    except FileNotFoundError:
        return False

if __name__ == "__main__":
    if len(sys.argv) != 2 or not sys.argv[1].isdigit():
        print("Usage: ./1-export_to_CSV.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    user, todos = fetch_user_and_todos(employee_id)
    valid_csv = validate_csv(user, todos)
    if not valid_csv:
        print("CSV file validation failed")
    else:
        print("CSV file validation passed")

