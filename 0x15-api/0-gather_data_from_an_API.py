import requests

def get_employee_todo_progress(employee_id):
    # Fetch employee information from the REST API
    base_url = 'https://jsonplaceholder.typicode.com'
    response = requests.get(f'{base_url}/users/{employee_id}')
    user_data = response.json()

    # Fetch TODO list for the employee from the REST API
    response = requests.get(f'{base_url}/todos?userId={employee_id}')
    todos_data = response.json()

    # Get the employee name and TODO list progress
    employee_name = user_data['name']
    total_tasks = len(todos_data)
    completed_tasks = sum(1 for todo in todos_data if todo['completed'])

    # Display employee TODO list progress
    print(f"Employee {employee_name} is done with tasks({completed_tasks}/{total_tasks}):")

    # Display completed task titles
    for todo in todos_data:
        if todo['completed']:
            print("\t", todo['title'])

if __name__ == "__main__":
    import sys

    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Employee ID must be an integer.")
        sys.exit(1)

    get_employee_todo_progress(employee_id)
