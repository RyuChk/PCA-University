def exit(self, car_id: int):
    if(self.contain(car_id)):
        temp = self.rm_top()
        if(temp == car_id): ## Check base cases
            print(f"In temp lane .... : {self.new_row}")
            self.add(self.new_row[::-1])
            self.new_row = []
            return print(f"car {temp} is now exit ; remain {self.stack}" ) ## --> base cases
        else:
            self.new_row.append(temp)
            return self.exit(car_id) ## recursive 
    else:
        return print("Your car doesn't exits or Invalid Car ID")