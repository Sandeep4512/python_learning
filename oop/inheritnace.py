class Car:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model

    def fullname(self):
        return f"{self.brand} {self.model}"

class ElectricCar(Car):
    def __init__(self,brand,model,battry_size):
        super().__init__(brand,model)
        self.battry_size = battry_size

tesla = ElectricCar("tesla","Ayz","85kwh")
print(tesla.fullname())