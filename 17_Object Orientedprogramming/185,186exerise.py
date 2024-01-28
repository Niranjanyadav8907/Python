
# create a laptop class with attributes like brand name , model name price
# creat two object/ instance of your laptop class

class Laptop:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

# Creating two instances of the Laptop class
laptop1 = Laptop(brand="HP", model="Pavilion", price=800)
laptop2 = Laptop(brand="Dell", model="Inspiron", price=1000)

# Accessing and printing attributes of the instances
print("Laptop 1:")
print("Brand:", laptop1.brand)
print("Model:", laptop1.model)
print("Price:", laptop1.price)

print("\nLaptop 2:")
print("Brand:", laptop2.brand)
print("Model:", laptop2.model)
print("Price:", laptop2.price)
