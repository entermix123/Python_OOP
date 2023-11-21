from typing import List


class Task:

    def __init__(self, name: str, due_date: str):
        self.name = name
        self.due_date = due_date
        self.comments: List[str] = []
        self.completed: bool = False

    def change_name(self, new_name: str):
        if self.name == new_name:
            return f"Name cannot be the same."

        self.name = new_name
        return self.name

    def change_due_date(self, new_due_date: str):
        if self.due_date == new_due_date:
            return f"Date cannot be the same."

        self.due_date = new_due_date
        return self.due_date

    def add_comment(self, comment: str):
        self.comments.append(comment)

    def edit_comment(self, comment_number: int, new_comment: str):
        if 0 <= comment_number <= len(self.comments)-1:
            self.comments[comment_number] = new_comment
            return ', '.join(x for x in self.comments)
        else:
            return f"Cannot find comment."

    def details(self):
        return f"Name: {self.name} - Due Date: {self.due_date}"
