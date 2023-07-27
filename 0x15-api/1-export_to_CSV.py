import requests
import csv
import sys

def fetch_employee_data(employee_id):
    base_url = 'https://jsonplaceholder.typicode.com'
    user_url = f'{base_url}/users/{employee_id}'
    todos_url = f'{base_url}/todos?userId={employee_id}'

    try:
        user_response = requests.get(user_url)
        todos_response = requests.get(todos_url)

        user_data = user_response.json()
        todos_data = todos_response.json()

        return user_data, todos_data
    except requests.exceptions.RequestException as e:
        print(f"Error occurred while fetching data: {e}")
        sys.exit(1)

def display_todo_list_progress(employee_name, done_tasks, total_tasks, completed_tasks):
    print(f"Employee {employee_name} is done with tasks({done_tasks}/{total_tasks}):")
    for task in completed_tasks:
        print(f"\t{task['title']}")

def export_to_csv(user_id, username, todos_data):
    file_name = f"{user_id}.csv"
    with open(file_name, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])

        for task in todos_data:
            task_id = task['id']
            title = task['title']
            completed = task['completed']

            writer.writerow([user_id, username, completed, title])

    print(f"Data exported to {file_name} successfully.")

def main():
    if len(sys.argv) != 2 or not sys.argv[1].isdigit():
        print("Please provide a valid employee ID as a parameter.")
        sys.exit(1)

    employee_id = int(sys.argv[1])

    user_data, todos_data = fetch_employee_data(employee_id)

    employee_name = user_data['name']
    total_tasks = len(todos_data)
    completed_tasks = [task for task in todos_data if task['completed']]

    display_todo_list_progress(employee_name, len(completed_tasks), total_tasks, completed_tasks)

    # Export data to CSV file
    export_to_csv(employee_id, employee_name, todos_data)

if __name__ == "__main__":
    main()
