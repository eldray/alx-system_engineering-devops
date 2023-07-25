#!/usr/bin/python3
"""Exports to-do list information for a given employee ID to JSON format."""

import requests as r
import json
import sys

def export_to_json(employee_id, todos_data):
    employee_name = todos_data[0]['name']
    json_data = {
        employee_id: [
            {
                "task": todo['title'],
                "completed": todo['completed'],
                "username": employee_name
            }
            for todo in todos_data
        ]
    }

    file_name = f"{employee_id}.json"
    with open(file_name, mode='w') as json_file:
        json.dump(json_data, json_file, indent=4)

if __name__ == '__main__':
    url = 'https://jsonplaceholder.typicode.com/'
    employee_id = sys.argv[1]
    usr_data = r.get(url + 'users/{}'.format(employee_id)).json()
    to_do = r.get(url + 'todos', params={'userId': employee_id}).json()

    export_to_json(employee_id, to_do)
