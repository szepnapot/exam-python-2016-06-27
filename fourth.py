#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Rocket(object):
    """basic rocket class with two possible types"""

    def __init__(self, rocket_type='', starting_fuel=0, launches=0):
        self.rocket_type = rocket_type
        self.fuel = starting_fuel
        self.launches = launches
        self.setDefaultsForRocket()

    def setDefaultsForRocket(self):
        if self.rocket_type == 'falcon1':
            self.fuel_per_launch = 1
            self.refillTop = 5
        elif self.rocket_type == 'falcon9':
            self.fuel_per_launch = 9
            self.refillTop = 20

    def launch(self):
        self.fuel -= self.fuel_per_launch
        self.launches += 1

    def refill(self):
        used_fuel = self.refillTop - self.fuel
        self.fuel = self.refillTop
        return used_fuel

    def getStats(self):
        return "name: {}, fuel: {}".format(self.rocket_type, self.fuel)


class SpaceX(Rocket):
    """Rocket carrier spaceship, control rockets added to it"""

    def __init__(self, storedFuel):
        super().__init__()
        self.storedFuel = storedFuel
        self.rockets = []
        self.rockets_launched = 0

    def getLaunches(self):
        self.rockets_launched = sum([rocket.launches for rocket in self.rockets])

    def addRocket(self, rocket):
        self.rockets.append(rocket)
        self.getLaunches()

    def refill_all(self):
        fuelFromSTorage = sum([rocket.refill() for rocket in self.rockets])
        self.storedFuel -= fuelFromSTorage

    def launch_all(self):
        [rocket.launch() for rocket in self.rockets]
        self.getLaunches()

    def buy_fuel(self, amount):
        self.storedFuel += amount

    def getStats(self):
        return "rockets: {}, fuel: {}, launches: {}".format(len(self.rockets), self.storedFuel, self.rockets_launched)


space_x = SpaceX(100)
falcon1 = Rocket('falcon1', 0, 0)
falcon9 = Rocket('falcon9', 0, 0)
returned_falcon9 = Rocket('falcon9', 11, 1)
print(returned_falcon9.getStats()) # name: falcon9, fuel: 11

space_x.addRocket(falcon1)
space_x.addRocket(falcon9)
space_x.addRocket(returned_falcon9)

print(space_x.getStats()) # rockets: 3, fuel: 100, launches: 1
space_x.refill_all()
print(space_x.getStats()) # rockets: 3, fuel: 66, launches: 1
space_x.launch_all()
print(space_x.getStats()) # rockets: 3, fuel: 66, launches: 4
space_x.buy_fuel(50)
print(space_x.getStats()) # rockets: 3, fuel: 116, launches: 4
