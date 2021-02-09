from datetime import datetime


class Task:
    def __init__(self, text):
        self.text = text
        self.ended = False
        self.datetime = datetime.now()

    def task_ended(self):
        self.ended = True


class List:
    def __init__(self):
        self.tasks = []

    def list_task(self):
        print([task.text + " " + str(task.ended) + " " + str(task.datetime) for task in list.tasks])

    def delete_task(self, number):
        self.tasks.pop(number - 1)

    def add_task(self, task):
        self.tasks.append(task)
        print("add")

    def tasks_ended(self, index):
        task = self.tasks[index - 1]
        task.task_ended()
        print("task-ended")

    def task_help(self):
        print("task-help")


list = List()
# doc = open("todo.txt", "r")
# lines = doc.readlines()
# print(lines)
# for task in lines:
#     list.add_task(task)
# print(lines)
# print(list.tasks)

start = input("Que souhaitez-vous faire ?")
while start != "exit":
    if start == "help":
        start = input("Pour ajouter une tâche tapez 'add' "
                      "Pour supprimer une tâche tapez 'delete' "
                      "Pour terminer une tâche tapez 'fini' "
                      "Pour lister toutes les tâches tapez 'liste' "
                      "Pour sortir du programme tapez exit")
    elif start == "list":
        list.list_task()
        start = input("Que voulez-vous faire ? ")
    elif start == "delete":
        list.list_task()
        id_task = input("quelle est le numéro de la tâche que vous voulez supprimer ? ")
        id_task = int(id_task)
        list.delete_task(id_task)
        list.list_task()
        start = input("Que voulez-vous faire ? ")
    elif start == "add":
        text_task = input("Texte de la tâche: ")
        new_task = Task(text_task)
        list.add_task(new_task)
        list.list_task()
        start = input("Que voulez-vous faire ? ")
    elif start == "fini":
        list.list_task()
        id_task_ended = input("Quel est le numéro de la tâche terminé ? ")
        id_task_ended = int(id_task_ended)
        list.tasks_ended(id_task_ended)
        list.list_task()
        start = input("Que voulez-vous faire ? ")
    else:
        list.list_task()
        start = input("Que voulez-vous faire ? ")
