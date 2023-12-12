from project_python_oop_exam_christmas_pastry_shop.delicacies.delicacy import Delicacy


class Gingerbread(Delicacy):
    @property              # getter prevent outside change by mistake
    def get_portion(self):
        return 200

    # PORTION = 200
    # second parameter: portion is passed by super() with self.get_portion()
    def __init__(self, name: str, price: float):
        super().__init__(name, self.get_portion, price)     # if PORTION = 200, then self.get_portion = self.PORTION

    def details(self):
        return f"Gingerbread {self.name}: {self.get_portion}g - {self.price:.2f}lv."
