#!/usr/bin/python3
"""Script to export data in the CSV format"""
import requests as r
import csv
import sys

def get_employee_name(employee_id):
    url = f'https://jsonplaceholder.typicode.com/users/{employee_id}'
    response = r.get(url)
    if response.status_code == 200:
        return response.json()['name']
    else:
        raise ValueError(f"Could not fetch user information for employee ID {employee_id}")

def export_to_csv(employee_id, todos_data):
    employee_name = get_employee_name(employee_id)
    file_name = f"{employee_id}.csv"

    with open(file_name, mode='w', newline='') as csv_file:
        fieldnames = ['USER_ID', 'USERNAME', 'TASK_COMPLETED_STATUS', 'TASK_TITLE']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()

        for todo in todos_data:
            writer.writerow({
                'USER_ID': employee_id,
                'USERNAME': employee_name,
                'TASK_COMPLETED_STATUS': str(todo['completed']),
                'TASK_TITLE': todo['title']
            })

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Employee ID must be an integer.")
        sys.exit(1)

    url = 'https://jsonplaceholder.typicode.com/todos'
    params = {'userId': employee_id}
    response = r.get(url, params=params)

    if response.status_code != 200:
        print("Error: Could not fetch TODO data for the specified employee ID.")
        sys.exit(1)

    to_do = response.json()
    export_to_csv(employee_id, to_do)
