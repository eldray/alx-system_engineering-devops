#!/usr/bin/python3
"""Script to export data in the CSV format"""
import requests as r
import csv
import sys

def export_to_csv(employee_id, todos_data):
    employee_name = todos_data[0]['name']
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
    url = 'https://jsonplaceholder.typicode.com/'
    employee_id = sys.argv[1]
    usr_data = r.get(url + 'users/{}'.format(employee_id)).json()
    to_do = r.get(url + 'todos', params={'userId': employee_id}).json()

    export_to_csv(employee_id, to_do)