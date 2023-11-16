"""
CP1404 Practical 09 - Silver Service Taxi
Estimated Time: 20 minutes
Actual Time:
"""
from prac_09.taxi import Taxi


class SilverServiceTaxi(Taxi):
    """A Silver Service Taxi Class derivative of a Taxi class."""

    flagfall = 4.50

    def __init__(self, name, fuel, fanciness: float):
        super().__init__(name, fuel)
        self.price_per_km = Taxi.price_per_km * fanciness

    def get_fare(self):
        """Return the price for the current fare."""
        return self.price_per_km * self.current_fare_distance + self.flagfall
