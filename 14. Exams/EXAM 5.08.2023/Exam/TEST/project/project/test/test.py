from unittest import TestCase

from project.second_hand_car import SecondHandCar


class TestSecondHandCar(TestCase):

    def setUp(self):
        self.car = SecondHandCar('a3', 'audi', 150000, 2500.0)

    def test_init(self):
        self.assertEqual('a3', self.car.model)
        self.assertEqual('audi', self.car.car_type)
        self.assertEqual(150000, self.car.mileage)
        self.assertEqual(2500.0, self.car.price)
        self.assertEqual([], self.car.repairs)

    def test_wrong_price(self):
        with self.assertRaises(ValueError) as ve:
            self.car.price = 0.5

        expected_msg = 'Price should be greater than 1.0!'

        self.assertEqual(expected_msg, str(ve.exception))

    def test_wrong_mileage(self):
        with self.assertRaises(ValueError) as ve:
            self.car.mileage = 90

        expected_msg = 'Please, second-hand cars only! Mileage must be greater than 100!'

        self.assertEqual(expected_msg, str(ve.exception))

    def test_set_price__expect_changed_price(self):
        new_price = 2400.0

        expected_msg = 'The promotional price has been successfully set.'
        self.assertEqual(expected_msg, self.car.set_promotional_price(new_price))

    def test_set_wrong_price__expect_raises(self):
        new_price = 2600.0
        with self.assertRaises(ValueError) as ve:
            self.car.set_promotional_price(new_price)

        expected_msg = 'You are supposed to decrease the price!'
        self.assertEqual(expected_msg, str(ve.exception))

    def test_repair__expect_ok_msg(self):
        repair_price = 1000.0

        expected_msg = f'Price has been increased due to repair charges.'
        self.assertEqual(expected_msg, self.car.need_repair(repair_price, 'engine'))
        self.assertEqual(3500.0, self.car.price)
        self.assertEqual(['engine'], self.car.repairs)

    def test_repair_wrong_price__expect_msg(self):
        repair_price = 1500.0
        result = self.car.need_repair(repair_price, 'engine')

        expected_msg = 'Repair is impossible!'
        self.assertEqual(expected_msg, result)
        self.assertEqual([], self.car.repairs)

    def test_gt_self_gt_than_other__expect_ok_msg(self):
        other = SecondHandCar('a1', 'audi', 140000, 2000.0)

        result = self.car > other
        expected_msg = True
        self.assertEqual(expected_msg, result)

    def test_gt_wrong_type__expect_not_ok_msg(self):
        other = SecondHandCar('a1', 'skoda', 140000, 2000.0)

        result = self.car > other
        expected_msg = 'Cars cannot be compared. Type mismatch!'
        self.assertEqual(expected_msg, result)

    def test_str_expect_msg(self):
        repair_price = 1000.0
        self.car.need_repair(repair_price, 'engine')
        self.car.need_repair(repair_price, 'electric system')

        expected_msg = f"""Model a3 | Type audi | Milage 150000km
Current price: 4500.00 | Number of Repairs: 2"""

        self.assertEqual(expected_msg, str(self.car))

