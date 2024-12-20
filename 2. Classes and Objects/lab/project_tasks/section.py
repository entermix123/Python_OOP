from typing import List
from project_tasks.task import Task


class Section:

    def __init__(self, name: str):
        self.name = name
        self.tasks: List[Task] = []

    def add_task(self, new_task: Task):
        if new_task in self.tasks:
            return f"Task is already in the section {self.name}"

        self.tasks.append(new_task)
        return f"Task {Task.details(new_task)} is added to the section"

    def complete_task(self, task_name: str):
        try:
            task = ''.join(x[0] for x in self.tasks if x.name == task_name)
            # task = next(filter(lambda u: u.name == task_name, self.tasks))
            if task in self.tasks:
                task.completed = True
                return f"Completed task {task_name}"
        except StopIteration:
            return f"Could not find task with the name {task_name}"

    def clean_section(self):
        count_x = 0
        for current_task in self.tasks:
            if current_task.completed:
                count_x += 1
                self.tasks.remove(current_task)

        return f"Cleared {count_x} tasks."

    def view_section(self):
        task_info = '\n'.join([p.details() for p in self.tasks])
        return f"Section {self.name}:\n" \
               f"{task_info}"


task = Task("Make bed", "27/05/2020")
print(task.change_name("Go to University"))
print(task.change_due_date("28.05.2020"))
task.add_comment("Don't forget laptop")
print(task.edit_comment(0, "Don't forget laptop and notebook"))
print(task.details())
section = Section("Daily tasks")
print(section.add_task(task))
second_task = Task("Make bed", "27/05/2020")
section.add_task(second_task)
print(section.clean_section())
print(section.view_section())
