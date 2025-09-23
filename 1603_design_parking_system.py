class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.big = big
        self.medium = medium
        self.small = small

    def addCar(self, carType: int) -> bool:
        match carType:
            case 1:
                if self.big == 0:
                    return False
                self.big -= 1
            case 2:
                if self.medium == 0:
                    return False
                self.medium -= 1
            case 3:
                if self.small == 0:
                    return False
                self.small -= 1
        return True
        

