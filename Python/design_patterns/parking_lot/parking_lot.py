from abc import ABC

class VehicleType(Enum):
    CAR, TRUCK, ELECTRIC, VAN, MOTORBIKE = 1,2,3,4,5

class ParkingSpotType(Enum):
    HANDICAPPED, COMPACT, LARGE, MOTORBIKE, ELECTRIC = 1,2,3,4,5

class AccountStatus(Enum):
    ACTIVE, BLOCKED, BANNED, COMPROMISED, ARCHIVED = 1,2,3,4,5

class ParkingTicketStatus(Enum):
    ACTIVE, PAID, LOST = 1,2,3

# This is for the parking lot.
class Address:
    def __init__(self ,street, city, state, zip_code):
        self.__street_address = street
        self.__city = city
        self.__state = state
        self.__zip_code = zip_code

class Person:
    def __init__(self, name, address, email, phone):
        self.__name = name
        self.__address = address
        self.__email = email
        self.__phone = phone


"""
Now, we have Account, Admin and Parking Assistant 
The 3 actors who interact with out system
"""

class Account:
    def __init__(self, user_name, password, person, status=AccountStatus.ACTIVE):
        self.__user_name = user_name
        self.__password = password
        self.__person = person
        self.__status = status


    def reset_password(self):
        pass

class Admin(Account):
    def __init__(self, user_name, password, person, status=AccountStatus.ACTIVE):
        super().__init_(user_name, password, person, status)

    def add_parking_floor(self, floor):
        pass

    def add_parking_spot(self, floor_name, spot):
        pass

    def add_parking_display_board(self, floor_name, display_board):
        pass

    def add_customer_info_panel(self, floor_name, customer_info_panel):
        pass

    # Similarly for entrance panel, exit panel etc.

class ParkingAttendant(Account):
    def __init__(self, user_name, password, person, status=AccountStatus.ACTIVE):
        super().__init__(user_name, password, person, status)

    def process_ticket(self, ticket_number):
        pass


class ParkingSpot(ABC):
    def __init__(self, number, parking_spot_type):
        self.__number = number
        self.__free = True
        self.__vehicle = None
        self.__parking_spot_type = parking_spot_type

    def is_free(self):
        return self.__free

    def assign_vechicle(self, vehicle):
        self.__vehicle = vehicle
        free = False

    def remove_vehicle(self):
        self.__vehicle = None
        free = True

class HandicappedSpot(ParkingSpot):
    def __init__(self, number):
        super().__init__(number, ParkingSpotType.HANDICAPPED)

class CompactSport(ParkingSpot):
    def __init__(self, number):
        super().__init__(number, ParkingSpotType.COMPACT)

class MotorbikeSpot(ParkingSpot):


# Similarly for other ParkingSpots

class Vehicle(ABC):
    def __init__(self, license_number, vehicle_type, ticket=None):
        self.__license_number = license_number
        self.__type = vehicle_type
        self.__ticket = ticket

    def assign_ticket(self, ticket):
        self.__ticket = ticket

class Car(Vehicle):
    def __init__(self, license_number, ticket=None):
        super().__init__(license_number, VehicleType.CAR, ticker)

# Similarly for Van, Truck Vehicle etc.

"""
Now there are 3 more classes remaining

1. Parking Floor
2. ParkingLot
3. Parking Display Board 
"""

import threading

class ParkingLot:
    """
    We are modelling using the Singleton pattern, so that one object
    of the parking lot exists.

    all Entrance panels will use this object to create new parking ticker
    """
    instance = None

    class Singleton:
        def __init__(self, name, address):
            """
            :param name: Read from DB
            :param address: Read from DB

            Initialize parking spot counts by reading from DB
            Initialize, entrance and exit panels

            """
            self.__name = name
            self.__address = address
            self.__parking_rate = ParkingRate()

            self.__compact_spot_count = 0
            self.__large_spot_count = 0
            self.__motorbike_spot_count = 0
            self.__electric_spot_count = 0

            self.__max_compact_count = 0
            self.__max_motorbike_count = 0
            self.__max_electric_count = 0

            self.__entrance_panels = {}
            self.__exit_panels = {}
            self.__parking_floors = {}

            self.__active_tickets = {}

            self.__lock = threading.Lock()

    def __init__(self, name, address):
        if not ParkingLot.instance:
            ParkingLot.instance = ParkingLot.Singleton(name, address)

        else:
            ParkingLot.instance.__name = name
            ParkingLot.instance.__address = address

    def __getattr__(self, item):
        return getattr(self.instance, name)


    def get_new_parking_ticket(self, vehicle):
        if self.is_full(vehicle.get_type())):
            raise Exception("Parking is Full")
        self.__lock.acquire()

        ticket = ParkingTicket()
        vechicle.assign_ticket(ticket)
        ticket.save_in_DB()

        self.__increment_spot_count(vehicle.get_type())
        self.__active_tickets.put(ticket.get_ticket_number(), ticket)
        self.__lock.release()
        return ticket







    def is_full(self, type):
        pass

    def increment_spot_count(self, type):
        pass

    def add_parking_floor(self, floor):
        # Update DB
        pass

    def add_entrance_panel(self, entrance_panel):
        # Update DB
        pass

    def add_exit_panel(self, exit_panel):
        # Update DB
        None






