#!/usr/bin/python3
"""
Records all tasks that are owned by employee.
"""
import requests
import sys
import json


def main():
    """
    Main function to generate the JSON data for an employee and their tasks.

    The function fetches user and task data from two different endpoints
    using the requests library.
    Then, it creates a JSON dictionary where the keys is employee id and the
    value is a lists of dictionaries containing tasks and completion status.
    Finally, it writes the JSON data to a file
    """
    employeeid = int(sys.argv[1])
    total_task = 0
    done_task = 0

    namereq = requests.get('https://jsonplaceholder.typicode.com/users')
    usersdict = namereq.json()

    for user in usersdict:
        if user['id'] == employeeid:
            username = user['username']

    todoreq = requests.get('https://jsonplaceholder.typicode.com/todos')
    tododict = todoreq.json()
    users = []

    for user in tododict:
        if user['userId'] == employeeid:
            users.append(user)

    json_data = []
    for user in users:
        json_dict = {}
        json_dict['task'] = user['title']
        json_dict['completed'] = user['completed']
        json_dict['username'] = username
        json_data.append(json_dict)

    Jdict = {}
    Jdict[str(employeeid)] = json_data
    json_string = json.dumps(Jdict)

    file_path = f"{employeeid}.json"
    with open(file_path, 'w') as json_file:
        json_file.write(json_string)


if __name__ == "__main__":
    main()
