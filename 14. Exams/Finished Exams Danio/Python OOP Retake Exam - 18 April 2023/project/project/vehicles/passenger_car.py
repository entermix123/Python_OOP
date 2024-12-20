from project.vehicles.base_vehicle import BaseVehicle


class PassengerCar(BaseVehicle):
    def __init__(self, brand, model, license_plate_number, max_mileage=450.00):
        super().__init__(brand, model, license_plate_number, max_mileage)

    def drive(self, mileage: float):
        percentage = abs(round((mileage/450.00)*100))
        self.battery_level -= percentage


# car = PassengerCar('BMW', 'M3', '34565', 550000)
# print(car.drive(225))
# print(str(car))
