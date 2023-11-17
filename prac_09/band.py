"""CP1404 Practical 09 - Band Class"""


class Band:
    """Define a Band"""

    def __init__(self, band_name: str):
        """Initialise the Band object."""
        self.band_name = band_name
        self.members = []

    def add(self, member):
        """Add a new member to the Band."""
        self.members.append(member)

    def __str__(self):
        """Return a String representation of the band."""
        # I need to print the band name, and then each band members
        return f"{self.band_name} ({self.members})"

    def play(self):
        """Goes through each members, where they play"""
        return ("\n").join([member.play() for member in self.members])
