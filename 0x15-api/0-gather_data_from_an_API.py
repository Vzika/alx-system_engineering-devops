import requests
import sys

def get_employee_todo_progress(employee_id):
    # API endpoint for employee data
    url_user = 'https://jsonplaceholder.typicode.com/users/{}'.format(employee_id)
    # API endpoint for user's todos
    url_todos = 'https://jsonplaceholder.typicode.com/todos?userId={}'.format(employee_id)

    # Fetching employee data
    response_user = requests.get(url_user)
    user_data = response_user.json()
    employee_name = user_data.get('name')

    # Fetching todos of the employee
    response_todos = requests.get(url_todos)
    todos_data = response_todos.json()

    # Counting completed tasks
    completed_tasks = [task for task in todos_data if task['completed']]
    total_completed_tasks = len(completed_tasks)
    total_tasks = len(todos_data)

    # Displaying progress
    print("Employee {} is done with tasks({}/{}):".format(employee_name, total_completed_tasks, total_tasks))
    for task in completed_tasks:
        print("\t{}".format(task['title']))

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    get_employee_todo_progress(employee_id)

