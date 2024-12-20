from typing import List

from project.route import Route
from project.user import User
from project.vehicles.base_vehicle import BaseVehicle
from project.vehicles.cargo_van import CargoVan
from project.vehicles.passenger_car import PassengerCar


class ManagingApp:
    VALID_TYPE_VEHICLES = {'PassengerCar': PassengerCar, 'CargoVan': CargoVan}

    def __init__(self):
        self.users: List[User] = []
        self.vehicles: List[BaseVehicle] = []
        self.routes: List[Route] = []

    def register_user(self, first_name: str, last_name: str, driving_license_number: str):
        if driving_license_number in [x.driving_license_number for x in self.users]:
            return f"{driving_license_number} has already been registered to our platform."

        self.users.append(User(first_name, last_name, driving_license_number))
        return f"{first_name} {last_name} was successfully registered under DLN-{driving_license_number}"

    def upload_vehicle(self, vehicle_type: str, brand: str, model: str, license_plate_number: str):
        if vehicle_type not in self.VALID_TYPE_VEHICLES:
            return f"Vehicle type {vehicle_type} is inaccessible."

        if license_plate_number in [x.license_plate_number for x in self.vehicles]:
            return f"{license_plate_number} belongs to another vehicle."

        self.vehicles.append(self.VALID_TYPE_VEHICLES[vehicle_type](brand, model, license_plate_number))
        return f"{brand} {model} was successfully uploaded with LPN-{license_plate_number}."

    def allow_route(self, start_point: str, end_point: str, length: float):

        if not self.routes:
            next_route_id = 1
        else:
            next_route_id = max([x.route_id for x in self.routes]) + 1

        existing_routes = [x for x in self.routes if
                           x.start_point == start_point and x.end_point == end_point and x.length == length]
        if existing_routes:
            return f"{start_point}/{end_point} - {length} km had already been added to our platform."

        shorter_routes = [x for x in self.routes if
                          x.start_point == start_point and x.end_point == end_point and x.length < length]
        if shorter_routes:
            return f"{start_point}/{end_point} shorter route had already been added to our platform."

        longer_routes = [x for x in self.routes if
                         x.start_point == start_point and x.end_point == end_point and x.length > length]
        if longer_routes:
            longer_routes[0].is_locked = True

        self.routes.append(Route(start_point, end_point, length, next_route_id))
        return f"{start_point}/{end_point} - {length} km is unlocked and available to use."

    def make_trip(self, driving_license_number: str, license_plate_number: str, route_id: int,  is_accident_happened: bool):

        user = [x for x in self.users if x.driving_license_number == driving_license_number][0]
        if user.is_blocked:
            return f"User {driving_license_number} is blocked in the platform! This trip is not allowed."

        vehicle = [x for x in self.vehicles if x.license_plate_number == license_plate_number][0]
        if vehicle.is_damaged:
            return f"Vehicle {license_plate_number} is damaged! This trip is not allowed."

        route = [x for x in self.routes if x.route_id == route_id][0]
        if route.is_locked:
            return f"Route {route_id} is locked! This trip is not allowed."

        vehicle.drive(route.length)
        if is_accident_happened:
            vehicle.is_damaged = True
            user.decrease_rating()
        else:
            user.increase_rating()
        result = str(vehicle)
        return result

    def repair_vehicles(self, count: int):
        damaged_vehicles = [x for x in self.vehicles if x.is_damaged]
        sorted_vehicles = sorted(damaged_vehicles, key=lambda x: (x.brand, x.model))

        repaired = 0
        if len(damaged_vehicles) >= count:
            for idx in range(count):
                sorted_vehicles[idx].is_damaged = False
                sorted_vehicles[idx].battery_level = 100
                repaired += 1
        else:
            for idx in range(len(damaged_vehicles)):
                sorted_vehicles[idx].is_damaged = False
                sorted_vehicles[idx].battery_level = 100
                repaired += 1

        return f"{repaired} vehicles were successfully repaired!"

    def users_report(self):
        sorted_users = sorted(self.users, key=lambda x: (-x.rating))
        end_user = [str(x) for x in sorted_users]
        result = f'*** E-Drive-Rent ***\n'
        result += '\n'.join(end_user)
        return result
