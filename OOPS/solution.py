class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def get_brand(self):
        return self.brand + " !"

    def full_name(self):
        return f"{self.brand} {self.model} {self.battery_size}"

class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size

my_tesla = ElectricCar("Tesla", "Model S", "90kWh")
print(my_tesla.model)



# my_car = Car("Honda", "venue")
# print(my_car.brand)