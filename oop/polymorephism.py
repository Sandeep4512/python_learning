class UPI:
    def pay(self):
        print("Payment through UPI")


class Card:
    def pay(self):
        print("Payment through Card")


class Cash:
    def pay(self):
        print("Payment through Cash")


payments = [UPI(), Card(), Cash()]

for payment in payments:
    payment.pay()  # This will call the pay method of each class, demonstrating polymorphism

# 

class Animal:
    def sound(self):
        print("Animal makes sound")


class Dog(Animal):
    def sound(self):
        print("Bark")


class Cat(Animal):
    def sound(self):
        print("Meow")

animals = [Dog(), Cat()]

for animal in animals:
    animal.sound()