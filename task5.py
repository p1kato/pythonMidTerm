def add_task():#The add_task function takes user input for a task name and adds it to the tasks dictionary with a completion status of False (i.e., the task is not completed)
    task = input("Введите задачу: ")
    tasks[task] = False
    print(f"Задача \"{task}\" была добавлена в туду лист брат")

def view_all_tasks():#The view_all_tasks function iterates over the tasks dictionary and prints out each task name and its completion status.
    for task, completed in tasks.items():
        print(f"{task}: {'Выполнено!' if completed else 'Не выполнено('}")

def mark_task_as_completed():#The mark_task_as_completed function takes user input for a task name and checks if it exists in the tasks dictionary
    task = input("Введите название задачи: ")
    if task in tasks:
        tasks[task] = True
        print(f"Задача {task} помечено как выполнено")
    else:
        print(f"Задача {task} не нашлась")

def view_all_completed_tasks():#The view_all_completed_tasks function iterates over the tasks dictionary and prints out only the tasks whose completion status is True (i.e., the task is completed).
    for task, completed in tasks.items():
        if completed:
            print(f"{task}: {'Выполнено!' if completed else 'Не выполнено'}")

tasks = {}
while True:
    print("\nПожалуйста, выберите задачу, которую вы хотите выполнить:")
    print("1. Добавить задачу")
    print("2. Просмотр всех задач")
    print("3. Отмеченные как выполнено")
    print("4. Просмотр всех выполненных задач")
    print("5. Выход")

    user_input = int(input("Введите свой выбор: "))

    if user_input == 1:
        add_task()
    elif user_input == 2:
        view_all_tasks()
    elif user_input == 3:
        mark_task_as_completed()
    elif user_input == 4:
        view_all_completed_tasks()
    elif user_input == 5:
        break
    else:
        print("Ошибка ввода брат, повторите еще раз😔")