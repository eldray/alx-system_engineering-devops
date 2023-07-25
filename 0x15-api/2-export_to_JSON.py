#!/usr/bin/python3
"""Exports to-do list information for a given employee ID to JSON format."""

import requests as r
import json
import sys

def export_to_json(employee_id, todos_data, employee_name):
    todo_list = []
    for todo in todos_data:
        task_title = todo['title']
        completed = todo['completed']
        todo_list.append({"task": task_title, "completed": completed, "username": employee_name})

    output_data = {employee_id: todo_list}
    file_name = f"{employee_id}.json"

    with open(file_name, 'w') as json_file:
        json.dump(output_data, json_file, indent=4)

if __name__ == '__main__':
    url = 'https://jsonplaceholder.typicode.com/'
    employee_id = sys.argv[1]
    usr_data = r.get(url + 'users/{}'.format(employee_id)).json()
    to_do = r.get(url + 'todos', params={'userId': employee_id}).json()

    employee_name = usr_data['name']
    export_to_json(employee_id, to_do, employee_name)
