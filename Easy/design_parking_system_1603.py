class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.big = big
        self.medium = medium
        self.small = small

    def addCar(self, carType: int) -> bool:
        if carType == 1 and self.big > 0:
            self.big -= 1
            return True
        elif carType == 2 and self.medium > 0:
            self.medium -= 1
            return True
        elif carType == 3 and self.small > 0:
            self.small -= 1
            return True
        else:
            return False


class ParkingSystem2:

    def __init__(self, big: int, medium: int, small: int):

        # Number of empty slots for each type of car
        self.empty = [big, medium, small]

    def addCar(self, carType: int) -> bool:

        # If space is available, allocate and return True
        if self.empty[carType - 1] > 0:
            self.empty[carType - 1] -= 1
            return True

        # Else, return False
        return False
