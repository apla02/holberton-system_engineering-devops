#!/usr/bin/python3
"""
return all of the information about an user_id
"""
import requests
from sys import argv


def get_information(employee_id):
    """returns information about his/her TODO list progress.
    """
    response = requests.get(
        'https://jsonplaceholder.typicode.com/users/{}'.format(employee_id))
    response_json = response.json()  # retrieve a dict

    response_todos = requests.get(
        'https://jsonplaceholder.typicode.com/todos?userId={}'.format(
            employee_id))
    response_json_todos = response_todos.json()  # retrieve a dict

    total_tasks = len(response_json_todos)
    done_tasks = 0
    tasks_titles = ""
    for task in response_json_todos:
        if task.get('completed') is True:
            done_tasks += 1
            tasks_titles += "\t {}\n".format(task.get('title'))

    print("Employee {} is done with tasks({}/{}):".format(
        response_json.get('name'), done_tasks, total_tasks))
    print(tasks_titles[:-1])


if __name__ == "__main__":
    get_information(argv[1])
