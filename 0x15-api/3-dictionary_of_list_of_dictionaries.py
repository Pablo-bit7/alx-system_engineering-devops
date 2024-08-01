#!/usr/bin/python3
"""
Fetch and export the TODO list progress of all
employees to a JSON file using requests
"""

import json
import requests


if __name__ == "__main__":
    base_url = 'https://jsonplaceholder.typicode.com'

    users_url = f'{base_url}/users'
    todos_url = f'{base_url}/todos'

    users_response = requests.get(users_url)
    todos_response = requests.get(todos_url)

    users = users_response.json()
    todos = todos_response.json()

    data = {}

    for user in users:
        user_id = user.get('id')
        username = user.get('username')
        tasks = []
        for task in todos:
            if task.get('userId') == user_id:
                tasks.append({
                    "username": username,
                    "task": task.get('title'),
                    "completed": task.get('completed')
                })
        data[str(user_id)] = tasks

    file_name = "todo_all_employees.json"

    with open(file_name, mode='w') as file:
        json.dump(data, file)
