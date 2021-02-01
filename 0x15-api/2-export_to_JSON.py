#!/usr/bin/python3
"""
return all of the information using API request
"""
import csv
import json
import requests
from sys import argv


def get_information(user_id):
    """returns information about his/her TODO list progress
    exporting data in a json format by specific id.
    """
    response = requests.get(
        'https://jsonplaceholder.typicode.com/users/{}'.format(user_id))
    response_json = response.json()  # retrieve a dict

    response_todos = requests.get(
        'https://jsonplaceholder.typicode.com/todos?userId={}'.format(
            user_id))
    r_json_todos = response_todos.json()  # retrieve a dict

    file_json = "{}.json".format(user_id)

    list_objects = []
    for task in r_json_todos:
        dic = {}
        dic['task'] = task.get('title')
        dic['completed'] = task.get('completed')
        dic['username'] = response_json.get('username')
        list_objects.append(dic)  # include task in a list of dictionaries
        json_data = {"{}".format(user_id): list_objects}

    with open(file_json, 'w') as fd:
        json.dump(json_data, fd)


if __name__ == '__main__':
    get_information(argv[1])
