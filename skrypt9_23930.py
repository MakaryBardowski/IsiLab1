class Vehicle:
    def __init__(self, name, rok_produkcji, przebieg):
        self._name = name
        self._rok_produkcji = rok_produkcji
        self._przebieg = przebieg
        
    @property # nie wywolujemy tej metody jako metody, tylko jak pole tj. vehicle.is_old
    def is_old(self):
        return self._rok_produkcji<1970
    
    @property # jak wyzej
    def is_long_milage(self):
        return self._przebieg>100_000
            
class Car(Vehicle): 
    def __init__(self, name, rok_produkcji, przebieg): # konstruktor wywolujacy konstruktor superklasy
        super().__init__(name, rok_produkcji, przebieg)

class Boat(Vehicle): 
    def __init__(self, name, rok_produkcji, przebieg): # jak wyzej
        super().__init__(name, rok_produkcji, przebieg)    

if __name__ == "__main__":
    boat = Boat("boat", 1968, 20000)
    car = Car("car", 1939, 625000)
    vehicle = Vehicle("vehicle", 2023, 1234)
    
    print(boat._name, " ->  isOld:" , boat.is_old, "  isLongMileage: ", boat.is_long_milage)
    print(car._name, " ->  isOld:" , car.is_old, "  isLongMileage: ", car.is_long_milage)
    print(vehicle._name, " ->  isOld:" , vehicle.is_old, "  isLongMileage: ", vehicle.is_long_milage)

    
