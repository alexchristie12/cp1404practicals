"""CP1404 Programming Language Example"""


class ProgrammingLanguage:
    """Represents a Programming Language Object."""

    def __init__(self, name="", typing="", reflection=True, year=0):
        """Initialises ProgrammingLanguage object."""
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def __str__(self):
        return f"{self.name}, {self.typing} Typing, Reflection={self.reflection}, First appeared in {self.year}"

    def is_dynamic(self):
        """Determines whether a language is dynamic."""
        return self.typing == "Dynamic"
