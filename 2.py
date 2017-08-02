# -*- coding: utf-8 -*-

import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def safe_list_get (l, idx, default):
    try:
        return l[idx]
    except IndexError:
        return default

# global values
tasks = list()

# handlers section
def list_command_handler():
    if len(tasks) == 0:
        print("Список дел пуст")
    for idx, task in enumerate(tasks):
        print("id : {}".format(idx))
        print("Название: {}".format(task["name"]))
        print("Описание: {}".format(task["description"]))
        print("Выполнена: {}".format(task["done"]))

    raw_input("нажмите Enter для продолжения")
    start_point()

def new_command_handler():
    name = raw_input("Введите название: ")
    description = raw_input("Описание: ")
    tasks.append({
        "name": name,
        "description": description,
        "done": False
    })

    print("Задача добавлена")
    raw_input("нажмите Enter для продолжения")
    start_point()

def edit_command_handler():
    idx = int(raw_input("Введите ID задачи, которую вы хотите изменить: "))
    task = safe_list_get(tasks, idx, None)
    if task:
        command = raw_input("Для пометки выполнено команда done: ")
        if command == "done":
            task["done"] = True
            print("Задача помечена как выполненая")
        else:
            print("Никаких изменений не было внесено")
    else:
        print("Задача не найдена")
    raw_input("нажмите Enter для продолжения")
    start_point()

def default_handler():
    print("Команда не распознана")
    start_point()

def exit_handler():
    exit()

# comands list
commands = {
    "list": list_command_handler,
    "new": new_command_handler,
    "edit": edit_command_handler,
    "exit": exit_handler
}

program_intro = """
Здесь всякое описание
может даже на двух строках

Команды:
list - для вывода списка задач
new - для записи новой задачи
edit - изменить задачу
exit - для выхода
"""

def start_point():
    print(program_intro)
    request_and_handle_command()

def request_and_handle_command():
    print("Введите команду")
    command = raw_input()
    clear()
    commands.get(command, default_handler)()

if __name__ == "__main__":
    start_point()
