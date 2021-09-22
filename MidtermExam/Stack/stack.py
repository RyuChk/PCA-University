import math
import random

class stack:
    def __init__(self, car: int = []):
        self.stack = car
        self.new_row = []

    def add(self, data: int):
        if type(data) == list:
            for i in data:
                if not self.contain(i):
                    self.stack.append(i)
        else:
            self.stack.append(data)

    def rm_top(self):
        return self.stack.pop()

    def empty(self):
        if self.stack:
            return False
        else:
            return True

    def size(self):
        return len(self.stack)

    def contain(self, data):
        if data in self.stack:
            return True
        else:
            return False

class valet_park(stack):
    def __init__(self, car: int = []):
        super().__init__(car=car)
        
    def exit(self, car_id: int):
        if(self.contain(car_id)):
            temp = self.rm_top()
            if(temp == car_id):
                print(f"In temp lane .... : {self.new_row}")
                self.add(self.new_row[::-1])
                self.new_row = []
                return print(f"car {temp} is now exit ; remain {self.stack}" )
            else:
                self.new_row.append(temp)
                return self.exit(car_id)
        else:
            return print("Your car doesn't exits or Invalid Car ID")
    
    def park_car(self, car_id: int):
        if not self.contain(car_id):
            self.add(car_id)
        else:
            return print("car already parked")

parking_lot_1 = valet_park()

parking_lot_1.park_car(input("parking ; "))

for _ in range(random.randint(3,5)):
    parking_lot_1.add([random.randint(10000,99999)])

ip = input(f"What car you want to get - {parking_lot_1.stack} : ")
print(f"Checking car {ip} ......")
try: 
    parking_lot_1.exit(int(ip))
except ValueError:
    print("Invalid Input syntax : etc. 'ABC, !@#*' ")
            