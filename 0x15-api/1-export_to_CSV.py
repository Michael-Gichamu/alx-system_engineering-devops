#!/usr/bin/python3
import requests
import sys
import csv


def main():
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

    csv_data = []
    for user in users:
        csv_dict = {}
        csv_dict['USER_ID'] = employeeid
        csv_dict['USERNAME'] = username
        csv_dict['TASK_COMPLETED_STATUS'] = str(user['completed'])
        csv_dict['TASK_TITLE'] = user['title']
        csv_data.append(csv_dict)

    userinfo = csv_data[0].keys()
    file_path = f"{employeeid}.csv"
    with open(file_path, 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=userinfo,
                                quoting=csv.QUOTE_ALL)
        writer.writerows(csv_data)


if __name__ == "__main__":
    main()
