from typing import List
from Exercise.ex_5_To_do_List.task import Task


class Section:

    def __init__(self, name: str):
        self.name = name
        self.tasks: List[Task] = []

    def add_task(self, new_task: Task) -> str:
        if new_task in self.tasks:
            return f"Task is already in the section {self.name}"
        self.tasks.append(new_task)
        return f"Task {new_task.details()} is added to the section"

    def complete_task(self, task_name: str) -> str:
        try:
            match = next(filter(lambda t: t.name == task_name, self.tasks))
            match.completed = True
            return f"Completed task {task_name}"
        except StopIteration:
            return f"Could not find task with the name {task_name}"

    def clean_section(self) -> str:
        amount = 0
        try:
            while True:
                match = next(filter(lambda t: t.completed == True, self.tasks))
                self.tasks.remove(match)
                amount += 1
        except StopIteration:
            return f"Cleared {amount} tasks."

    def view_section(self) -> str:
        final = f"Section {self.name}:\n"
        for t in self.tasks:
            final += f"{t.details()}\n"
        return final

