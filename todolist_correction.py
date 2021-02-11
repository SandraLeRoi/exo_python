from datetime import datetime
import json


class Task:
    def __init__(self, content):
        self.content = content
        self.state = False
        self.created_at = str(datetime.now())


class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self):
        task_text = input("Nom de la tâche: ")
        task = Task(task_text)
        self.tasks.append(task)

    def remove_task(self):
        try:
            task_id = int(input("id de la tache à supprimer: "))
            if 0 <= task_id < len(self.tasks):
                self.tasks.pop(task_id)
            else:
                print("Veuillez rentrer un nombre entre 0 et %d1" % (len(self.tasks) - 1))
        except ValueError:
            print("Veuillez rentrer un nombre entre 0 et %d1" % (len(self.tasks) - 1))

    def validate_task(self):
        task_id = int(input("id de la tache à valider: "))
        # task = self.tasks[task_id]
        # task.state = True
        self.tasks[task_id].state = True

    def list_tasks(self):
        template = "{id} - {date} - {content}[{state}] : "
        for task in self.tasks:
            index = self.tasks.index(task)
            print(template.format(
                id=index,
                date=task.created_at,
                content=task.content,
                state=task.state
            ))


class UserInterface:
    def __init__(self):
        self.manager = TaskManager()
        self.loop = True
        file = open("todolist.json", "r")
        raw_data = file.read()
        data = json.loads(raw_data)
        for element in data:
            task = Task(element["content"])
            task.__dict__ = element
            self.manager.tasks.append(task)

    def run(self):
        functions = {
            "add": self.manager.add_task,
            "remove": self.manager.remove_task,
            "validate": self.manager.validate_task,
            "list": self.manager.list_tasks,
            "exit": self.exit,
            "help": self.display_help
        }

        self.loop = True
        while self.loop:
            user_input = input("Que voulez-vous faire ?\n")
            functions[user_input]()
            # if user_input == "add":
            #     self.manager.add_task()
            # elif user_input == "remove":
            #     self.manager.remove_task()
            # elif user_input == "validate":
            #     self.manager.validate_task()
            # elif user_input == "list":
            #     self.manager.list_tasks()
            # elif user_input == "exit":
            #     self.exit()
            # else:
            #     self.display_help()

    def display_help(self):
        print('''
- list      ->  liste les tâches
- remove    ->  supprimer une tâche
- add       ->  ajouter une tâche
- validate  ->  valider une tâche
- help      ->  Affiche ce message d'aide
- exit      ->  sortir du programme''')

    def exit(self):
        todolist = open("todolist.json", "w")
        todolist.write(json.dumps([
            task.__dict__ for task in self.manager.tasks
        ]))
        todolist.close()
        self.loop = False


user = UserInterface()
user.run()
