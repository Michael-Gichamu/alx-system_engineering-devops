#!/usr/bin/python3
"""
Records all Tasks from all employees
Exports data in JSON format.
"""
import requests
import json


def get_username(userdict, empid):
    """
    Gets the username for an employeee from user dictionary.

    args:
        userdict (dict): dictionary containing employee data.
        empid (int): The employee id.
    Returns:
        str : The username corresponding to the empid.
    """
    for user in userdict:
        if user['id'] == empid:
            return user['username']


def get_list(userdict, empid, username):
    """
    Creates a list of tasks for a given empid from the user dictionary

    args:
        userdict (dict): dictionary containing employee data.
        empid (int): The employee id.
        username (str): username of the user.

    Returns:
        list of dictionaries: A list of dictionaries containing the tasks
                              and completion status
                              for the given empid and username.
    """
    users = []

    for user in userdict:
        if user['userId'] == empid:
            users.append(user)

    json_data = []
    for user in users:
        json_dict = {}
        json_dict['username'] = username
        json_dict['task'] = user['title']
        json_dict['completed'] = user['completed']
        json_data.append(json_dict)

    return json_data


def main():
    """
    Main function to generate the JSON data for all employees and their tasks.

    The function fetches user and task data from two different endpoints
    using the requests library.
    Then, it creates a JSON dictionary where the keys are employee ids and the
    values are lists of dictionaries containing tasks and completion status.
    Finally, it writes the JSON data to a file
    """
    employeeid = 0
    total_task = 0
    done_task = 0

    namereq = requests.get('https://jsonplaceholder.typicode.com/users')
    usersdict = namereq.json()

    todoreq = requests.get('https://jsonplaceholder.typicode.com/todos')
    tododict = todoreq.json()

    Jdict = {}
    for user in usersdict:
        employeeid = user['id']
        username = get_username(usersdict, employeeid)
        json_data = get_list(tododict, employeeid, username)
        Jdict[str(employeeid)] = json_data
    json_string = json.dumps(Jdict)

    file_path = "todo_all_employees.json"
    with open(file_path, 'w') as json_file:
        json_file.write(json_string)


if __name__ == "__main__":
    main()
