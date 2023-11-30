import unittest
from project_python_oop_exam_christmas_pastry_shop.worker import Worker


class TestWorker(unittest.TestCase):
    def test_init(self):
        worker = Worker('John', 1000, 10)
        self.assertEqual(worker.name, 'John')
        self.assertEqual(worker.salary, 1000)
        self.assertEqual(worker.energy, 10)

    def test_rest(self):
        worker = Worker('John', 1000, 10)
        worker.rest()
        self.assertEqual(worker.energy, 11)

    def test_work_not_enough_energy(self):
        worker = Worker('John', 1000, -1)
        with self.assertRaises(Exception) as context:
            worker.work()
        self.assertEqual(str(context.exception), 'Not enough energy.')

    def test_work_and_add_money(self):
        worker = Worker('John', 1000, 10)
        worker.work()
        self.assertEqual(worker.money, 1000)

    def test_work_decrease_energy(self):
        worker = Worker('John', 1000, 10)
        worker.work()
        self.assertEqual(worker.energy, 9)

    def test_get_info(self):
        worker = Worker('John', 1000, 10)
        self.assertEqual(worker.get_info(), 'John has saved 0 money.')


if __name__ == '__main__':
    unittest.main()
