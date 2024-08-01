#!/usr/bin/python3
"""
Fetch and export the TODO list progress of a given
employee to a CSV file using requests
"""

import csv
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
    file_name = f"{employee_id}.csv"

    with open(file_name, mode='w', newline='') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        for task in todos:
            writer.writerow([
                employee_id,
                employee_name,
                task.get('completed'),
                task.get('title')
            ])
