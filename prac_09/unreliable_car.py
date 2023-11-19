"""
CP1404 Prac 09 -  Unreliable Car Class
Estimated Time: 15 minutes
Actual Time: 
"""
from prac_09.car import Car
from random import uniform


class UnreliableCar(Car):
    """A class for an Unreliable car that might breakdown."""

    def __init__(self, name: str, fuel: int, reliability: float):
        """Initialise the Unreliable Car."""
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """Drive the car a certain distance If the reliability is greater than a
        random number then it will complete the journey otherwise it will not."""
        # Generate a random number
        random_number = uniform(0, 100)  # I need a better name for this.
        # Compare the score to the reliability and drive if the reliability is greater
        if self.reliability > random_number:
            if distance > self.fuel:
                distance = self.fuel
                self.fuel = 0
            else:
                self.fuel -= distance
            self._odometer += distance
            return distance
        else:
            return 0  # The car will not travel the distance and the odometer is unchanged. Weird formatting as well.
