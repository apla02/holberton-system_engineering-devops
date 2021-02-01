#!/usr/bin/python3
import json
import requests
from sys import argv


def get_information():
    """returns information about his/her TODO list progress
    exporting data in the json format for all of Ids.
    """
    user_id = 1
    all_objects = {}
    while True:
        response = requests.get(
            'https://jsonplaceholder.typicode.com/users/{}'.format(user_id))
        response_json = response.json()  # dict with information of users
        if len(response_json) == 0:
            break

        response_todos = requests.get(
            'https://jsonplaceholder.typicode.com/todos?userId={}'.format(
                user_id))
        r_json_todos = response_todos.json()

        list_objects = []
        for task in r_json_todos:
            dic = {}
            dic['task'] = task.get('title')
            dic['completed'] = task.get('completed')
            dic['username'] = response_json.get('name')
            list_objects.append(dic)  # include task in a list of dictionaries

        all_objects[user_id] = list_objects  # dic with all the list of dicts
        user_id += 1

    file_json = "todo_all_employees.json"
    with open(file_json, 'w') as fd:
        json.dump(all_objects, fd)

if __name__ == '__main__':
    get_information()
