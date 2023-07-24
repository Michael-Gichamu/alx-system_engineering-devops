#!/usr/bin/python3
import requests
import sys


def main():
    employeeid = int(sys.argv[1])
    total_task = 0
    done_task = 0

    namereq = requests.get('https://jsonplaceholder.typicode.com/users')
    usersdict = namereq.json()

    for user in usersdict:
        if user['id'] == employeeid:
            name = user['name']

    todoreq = requests.get('https://jsonplaceholder.typicode.com/todos')
    tododict = todoreq.json()
    users = []

    for user in tododict:
        if user['userId'] == employeeid:
            users.append(user)

    for user in users:
        total_task += 1
        if user['completed'] is True:
            done_task += 1

    print(f"Employee {name} is done with tasks({done_task}/{total_task}):")
    for user in users:
        if user['completed'] is True:
            title = user['title']
            print(f"\t {title}")


if __name__ == "__main__":
    main()
