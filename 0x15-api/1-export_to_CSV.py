#!/usr/bin/python3
"""
return all of the information using API request
"""
import csv
import requests
from sys import argv


def get_information(user_id):
    """returns information about his/her TODO list progress
    exporting data in the CSV format.
    """
    response = requests.get(
        'https://jsonplaceholder.typicode.com/users/{}'.format(user_id))
    response_json = response.json()
    name = response_json.get('username')

    response_todos = requests.get(
        'https://jsonplaceholder.typicode.com/todos?userId={}'.format(
            user_id))
    r_json_todos = response_todos.json()

    file_csv = "{}.csv".format(user_id)
    with open(file_csv, 'a') as fd:
        for task in r_json_todos:
            csv_data = "\"{}\",\"{}\",\"{}\",\"{}\"\n".format(
                user_id, name,
                task.get('completed'), task.get('title'))
            fd.write(csv_data)


if __name__ == '__main__':
    get_information(argv[1])
