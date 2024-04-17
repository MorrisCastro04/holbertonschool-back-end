#!/usr/bin/python3
""""list of all todos"""
import json
import requests


def list_of_todos():
    response = requests.get(
        f"https://jsonplaceholder.typicode.com/users")
    users = response.json()
    users_id = []
    for user in users:
        users_id.append(user['id'])

    data_dict = {}
    for ids in users_id:
        response = requests.get(
            f"https://jsonplaceholder.typicode.com/users/{ids}")
        response2 = requests.get(
            f"https://jsonplaceholder.typicode.com/todos?userId={ids}")
        employee_name = response.json()["username"]

        tasks = response2.json()

        data_dict[ids] = []
        for task in tasks:
            json_format = {
                "username": employee_name,
                "task": task["title"],
                "completed": task["completed"]
            }
            data_dict[ids].append(json_format)
    with open("todo_all_employees.json", "w") as json_file:
        json.dump(data_dict, json_file)


if __name__ == '__main__':
    list_of_todos()
