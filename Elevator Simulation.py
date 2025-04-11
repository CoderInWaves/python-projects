import time

class Elevator_Simulation:
    def __init__(self):
        self.current_floor = 1
    
    def lift(self):
        while True:
            try:
                outside = int(input("Enter your floor: "))
                if outside < 1 or outside > 20:
                    print("Enter a valid floor")
                    continue

                while True:
                    if outside > self.current_floor:
                        if self.current_floor == outside:
                            print(f"You reached {outside} floor")
                            break
                        self.current_floor += 1
                        print(f"You currently at {self.current_floor}")
                        time.sleep(1)

                    elif outside <= self.current_floor:
                        if self.current_floor == outside:
                            print(f"You reached {outside} floor")
                            break
                        self.current_floor -= 1
                        print(f"You currently at {self.current_floor}")
                        time.sleep(1)

            except ValueError:
                print("Invalid no: Enter a number between 1 to 20")

if __name__=="__main__":
    x = Elevator_Simulation()
    x.lift()