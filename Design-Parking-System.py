class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.big=big
        self.medium = medium 
        self.small = small

        self.mp =defaultdict(int)
        

    def addCar(self, carType: int) -> bool:

        self.mp[carType] +=1

        if carType ==1 :
            if self.mp[carType]<=self.big:
                return True
            else:
                return False

        if carType ==2 :
            if self.mp[carType]<=self.medium:
                return True
            else:
                return False

        if carType ==3 :
            if self.mp[carType]<=self.small:
                return True
            else:
                return False
            

        


# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)