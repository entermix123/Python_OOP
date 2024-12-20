from unittest import TestCase

from project.robot import Robot


class RobotTest(TestCase):
    def setUp(self):
        self.robo1 = Robot('3', 'Military', 25, 2.5)

    def test_init_(self):
        self.assertEqual('3', self.robo1.robot_id)
        self.assertEqual('Military', self.robo1.category)
        self.assertEqual(25, self.robo1.available_capacity)
        self.assertEqual(2.5, self.robo1.price)
        self.assertEqual([], self.robo1.hardware_upgrades)
        self.assertEqual([], self.robo1.software_updates)

    def test_category__expect_raises(self):
        with self.assertRaises(ValueError) as ve:
            Robot('3', 'Militaree', 25, 2.5)

        expected_result = f"Category should be one of '{Robot.ALLOWED_CATEGORIES}'"
        self.assertEqual(expected_result, str(ve.exception))

    def test_price__expect_raises(self):
        with self.assertRaises(ValueError) as ve:
            Robot('3', 'Military', 25, -2.5)

        result = "Price cannot be negative!"
        self.assertEqual(result, str(ve.exception))

    def test_upgrade__expect_ok(self):
        hardware_component = 'long gun'
        component_price = 1.00
        self.robo1.hardware_upgrades = ['big gun']
        act = self.robo1.upgrade(hardware_component, component_price)
        self.assertEqual(f"Robot 3 was upgraded with long gun.", act)
        self.assertEqual(4.0, self.robo1.price)

    def test_upgrade_with_no_existing_part(self):
        self.robo1.hardware_upgrades = ['big gun']
        hardware_component = 'big gun'
        component_price = 2.00
        act = self.robo1.upgrade(hardware_component, component_price)
        self.assertEqual(f"Robot 3 was not upgraded.", act)
        self.assertEqual(2.5, self.robo1.price)

    def test_update__expect_not_updated(self):
        self.robo1.software_updates = [10]
        self.robo1.available_capacity = 7
        needed_capacity = 5
        version = 7.7
        act = self.robo1.update(version, needed_capacity)
        result = f"Robot 3 was not updated."

        self.assertEqual(f"Robot 3 was not updated.", act)

    def test_update__expect_updated(self):
        self.robo1.software_updates = [3, 5]
        self.robo1.available_capacity = 15
        needed_capacity = 11
        version = 11
        act = self.robo1.update(version, needed_capacity)
        result = f"Robot 3 was not updated."

        self.assertEqual(f'Robot 3 was updated to version 11.', act)

    def test_gt_self_gt_other__expect_msg(self):
        self.robo1.price = 5.6
        self.robo2 = Robot('4', 'Military', 25, 4.0)

        result = self.robo1.__gt__(self.robo2)
        expected_msg = f'Robot with ID 3 is more expensive than Robot with ID 4.'
        self.assertEqual(expected_msg, result)

    def test_gt_other_gt_self__expect_msg(self):
        self.robo1.price = 3
        self.robo2 = Robot('4', 'Military', 25, 4.0)

        result = self.robo1.__gt__(self.robo2)
        expected_msg = f'Robot with ID 3 is cheaper than Robot with ID 4.'
        self.assertEqual(expected_msg, result)

    def test_gt_other_eq_self__expect_msg(self):
        self.robo1.price = 3.0
        self.robo2 = Robot('4', 'Military', 25, 3.0)

        result = self.robo1.__gt__(self.robo2)
        expected_msg = f'Robot with ID 3 costs equal to Robot with ID 4.'
        self.assertEqual(expected_msg, result)


