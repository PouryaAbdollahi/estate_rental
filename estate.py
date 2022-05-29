from abc import abstractmethod, ABC

from base import BaseClass


class AbstractEstate(ABC):
    def __init__(self, user, area, room_count, built_year, region, address, *args, **kwargs):
        self.user = user
        self.area = area
        self.room_count = room_count
        self.built_year = built_year
        self.region = region
        self.address = address
        super().__init__(*args, **kwargs)

    @abstractmethod
    def show_description(self):
        pass


class Apartment(AbstractEstate):
    def __init__(self, has_parking, has_elevator, floor, *args, **kwargs):
        self.has_parking = has_parking
        self.has_elevator = has_elevator
        self.floor = floor
        super().__init__(*args, **kwargs)

    def show_description(self):
        print(f"Apartment {self.id}")


class House(AbstractEstate):
    def __init__(self, has_yard, floors_count, *args, **kwargs):
        self.has_yard = has_yard
        self.floors_count = floors_count
        super().__init__(*args, **kwargs)

    def show_description(self):
        print(f"House {self.id}")

class Store(AbstractEstate): # shop
    # no init, inherited atts is necessary

    def show_description(self):
        print(f"Store {self.id}")

