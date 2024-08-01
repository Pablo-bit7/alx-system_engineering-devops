#!/usr/bin/python3
"""
Fetch and export the TODO list progress of a given
employee to a JSON file using requests
"""

import json
import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: {} EMPLOYEE_ID".format(sys.argv[0]))
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("EMPLOYEE_ID must be an integer")
        sys.exit(1)

    base_url = 'https://jsonplaceholder.typicode.com'

    user_url = f'{base_url}/users/{employee_id}'
    todos_url = f'{base_url}/todos'

    user_response = requests.get(user_url)
    todos_response = requests.get(todos_url, params={'userId': employee_id})

    user = user_response.json()
    todos = todos_response.json()

    employee_name = user.get('username')
    file_name = f"{employee_id}.json"

    tasks = []
    for task in todos:
        tasks.append({
            "task": task.get('title'),
            "completed": task.get('completed'),
            "username": employee_name
        })

    data = {str(employee_id): tasks}

    with open(file_name, mode='w') as file:
        json.dump(data, file)
