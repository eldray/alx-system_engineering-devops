#!/usr/bin/python3
"""Exports to-do list information of all employees to JSON format."""

import json
import requests
from sys import argv


def export_all_to_json():
    if len(argv) != 1:
        return

    url = "https://jsonplaceholder.typicode.com/users"
    users_response = requests.get(url)
    users_data = users_response.json()

    all_tasks = {}

    for user in users_data:
        user_id = str(user["id"])
        url = "https://jsonplaceholder.typicode.com/todos?userId=" + user_id
        todos_response = requests.get(url)
        todos_data = todos_response.json()

        tasks = []
        for task in todos_data:
            task_dict = {
                "username": user["username"],
                "task": task["title"],  # Use "title" instead of "name"
                "completed": task["completed"],
            }
            tasks.append(task_dict)

        all_tasks[user_id] = tasks

    with open("todo_all_employees.json", "w") as json_file:
        json.dump(all_tasks, json_file)


if __name__ == "__main__":
    export_all_to_json()
