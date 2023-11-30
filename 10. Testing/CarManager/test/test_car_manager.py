import unittest

from project_python_oop_exam_christmas_pastry_shop.car_manager import Car


class TestCar(unittest.TestCase):

    def setUp(self):
        self.my_car = Car("made somehow", "Audi", 8, 70)        # Arrange: create a car instance
        self.fuel_amount = 0                                    # Arrange: set class attribute fuel_amount to 0

    def test_init(self):                                        # test the init method
        self.assertEqual("made somehow", self.my_car.make)      # test make attribute
        self.assertEqual("Audi", self.my_car.model)             # test model attribute
        self.assertEqual(8, self.my_car.fuel_consumption)       # test fuel consumption
        self.assertEqual(70, self.my_car.fuel_capacity)         # test fuel capacity
        self.assertEqual(0, self.my_car.fuel_amount)            # test fuel_amount

    def test_make_setter_with_exception(self):                  # test make setter with exception
        with self.assertRaises(Exception) as ex:                # Arrange: set exception
            self.my_car = Car("", "Audi", 8, 70)                # Act: create a car instance with an empty make

        # Assert: compare the exception message with result message
        self.assertEqual("Make cannot be null or empty!", str(ex.exception))

    def test_model_as_empty_string(self):                       # test model setter with empty string
        with self.assertRaises(Exception) as ex:                # Arrange: set exception
            self.my_car = Car("somehow", "", 8, 70)             # Act: create a car instance with an empty model

        # Assert: compare the exception message with result message
        self.assertEqual("Model cannot be null or empty!", str(ex.exception))

    def test_fuel_consumption_setter_exception(self):           # test fuel consumption setter with exception
        with self.assertRaises(Exception) as ex:                # Arrange: set exception
            self.my_car = Car("somehow", "Audi", 0, 70)   # Act: create a car instance with an empty fuel_consumption

        # Assert: compare the exception message with result message
        self.assertEqual("Fuel consumption cannot be zero or negative!", str(ex.exception))

    def test_fuel_capacity_setter_exception(self):          # test fuel capacity setter with exception
        with self.assertRaises(Exception) as ex:            # Arrange: set exception
            self.my_car = Car("somehow", "Audi", 8, 0)      # Act: create a car instance with 0 fuel capacity attribute

        # Assert: compare the exception message with result message
        self.assertEqual("Fuel capacity cannot be zero or negative!", str(ex.exception))

    def test_fuel_amount_setter_with_exception(self):       # test fuel amount setter with exception
        with self.assertRaises(Exception) as ex:            # Arrange: set exception
            self.my_car.fuel_amount = -1           # Act: create a car instance with negative fuel amount attribute

        # Assert: compare the exception message with result message
        self.assertEqual("Fuel amount cannot be negative!", str(ex.exception))

    def test_refuel_with_exception(self):               # test usual refuel and refuel with exception

        # check usual refuel
        self.my_car.refuel(5)                           # Act: refuel the car with 5 liters of fuel usual
        self.assertEqual(5, self.my_car.fuel_amount)    # Assert: check expected fuel amount with result amount

        # check refuel with exception
        with self.assertRaises(Exception) as ex:        # Arrange: set exception
            self.my_car.refuel(-5)                      # Act: refuel with negative fuel amount

        # Assert: compare the exception message with result message
        self.assertEqual("Fuel amount cannot be zero or negative!", str(ex.exception))

    def test_drive(self):                               # test drive method usual and with exception

        # test usual drive method
        self.my_car.fuel_amount = 30                    # Arrange: set fuel amount to 30
        self.my_car.drive(100)                          # Act: execute drive method
        self.assertEqual(22, self.my_car.fuel_amount)   # Assert: check expected fuel amount with result amount

        # test drive with exception
        with self.assertRaises(Exception) as ex:        # Arrange: set exception
            self.my_car.drive(1000)                     # Act: execute drive method

        # Assert: compare the exception message with result message
        self.assertEqual("You don't have enough fuel to drive!", str(ex.exception))


if __name__ == '__main__':
    unittest.main()
