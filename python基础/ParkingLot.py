class Car:
    def __init__(self, carid):
        self.carid = carid
    
    def get_car_id(self):
        return self.carid

class ParkingLot:
    def __init__(self, capacity, name):
        self.name = name
        self.capacity = capacity
        self.cars = {}
    
    def is_empty(self):
        if len(self.cars) < self.capacity:
            return True
        else:
            return False

    def park_car(self, car: Car):
        if self.is_empty():
            ticket = len(self.cars)
            self.cars[ticket] = car
            print('%s 的票是 %s' % (car, ticket))
            return ticket
        else:
            print('%s 满了' % self.name)
            return None

    def take_car(self, ticket):
        if ticket in self.cars.keys():
            print('%s 取出' % self.cars[ticket])
            return self.cars.pop(ticket)
        else:
            print('票错了')
            return None
        

'''
if __name__ == "__main__":
    parking_lot = ParkingLot(1, '小停车场')
    car = Car('001')
    carid = car.get_car_id()
    ticket = parking_lot.park_car(carid)
    car = parking_lot.take_car(ticket)
    
    car1 = Car('002')
    carid1 = car1.get_car_id()
    ticket1 = parking_lot.park_car(carid1)
    car1 = parking_lot.take_car(ticket1)
'''
class ParkingBoy():
    def count(self, lots):
        lot_cn = {}
        for lot in lots:
            if len(lot.cars) < lot.capacity:
                lot_cn[lot] = lot.capacity - len(lot.cars)
        return lot_cn

    def park_cars(self, cars, lots):
        tickets = {}
        for car in cars:
            lot_cn = self.count(lots)
            if not lot_cn:
                print('所有停车场都没地方了')
            else:
                lot = list(lot_cn.keys())[0]
                t = lot.park_car(car)
                tickets[(lot, t)] = car
        return tickets
            
    def take_cars(self, tickets):
        for m, n in tickets.item():
            lot, ticket= m 
            lot.take_car(ticket)
            
            
class SmartParkingBoy(ParkingBoy):
    def park_cars(self, cars, lots):
        tickets = {}
        for car in cars:
            lot_cn = self.count(lots)
            if not lot_cn:
                print('所有停车场都没地方了')
            else:
                max_lot = sorted(lot_cn.items(), key=lambda x: -x[1])[0][0]
                t = max_lot.park_car(car)
                tickets[(max_lot, t)] = car
        return tickets


class SuperParkingBoy(ParkingBoy):
    def park_cars(self, cars, lots):
        tickets = {}
        for car in cars:
            lot_cn = self.count(lots)
            if not lot_cn:
                print('所有停车场都没地方了')
            else:
                rate = {}
                for k, v in lot_cn.items():
                    rate[k] = v/k.capacity
                max_rate_lot = sorted(rate.items(), key=lambda x: -x[1])[0][0]
                t = max_rate_lot.park_car(car)
                tickets[(max_rate_lot, t)] = car
        return tickets

import random
class parkingManager(SuperParkingBoy):
    def parkingboys(self, boys, cars, lots):
        tickets = {}
        for car in cars:
            tickets = boys[random.randint(0, len(boys)-1)].park_cars(car, lots)
        return tickets 
        
    def parkingself(self, cars, lots):
        return self.park_cars(cars, lots)













