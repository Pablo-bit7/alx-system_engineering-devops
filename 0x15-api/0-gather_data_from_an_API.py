#!/usr/bin/python3
"""
Fetch and display the TODO list progress of a given employee using requests
"""

import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: {} EMPLOYEE_ID".format(sys.argv[0]))
        sys.exit(1)

    employee_id = sys.argv[1]
    try:
        employee_id = int(employee_id)
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

    employee_name = user.get('name')
    total_tasks = len(todos)
    done_tasks = [task for task in todos if task.get('completed')]
    done_tasks_count = len(done_tasks)

    print("Employee {} is done with tasks({}/{}):".format(employee_name,
                                                          done_tasks_count,
                                                          total_tasks))
    for task in done_tasks:
        print(f"\t {task.get('title')}")
