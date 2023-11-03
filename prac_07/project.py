"""CP1404 Practical 07: Project Mangement Task"""
import datetime


class Project:
    """A Project object."""

    def __init__(self, name="", start_date="01/01/2000", priority=1, cost_estimate=0.00, completion_percentage=0):
        """Instantiate a Project object."""
        self.name = name
        # self.start_date = start_date
        try:
            full_date = datetime.datetime.strptime(start_date, "%d/%m/%Y")
            self.start_date = full_date.date()
        except ValueError:
            # If the formatting fails, just use the current date
            self.start_date = datetime.date.today()
        self.priority = priority
        self.cost_estimate = cost_estimate
        self.completion_percentage = completion_percentage

    def __str__(self):
        """String formatting for use in print statements, etc."""
        date_string = self.start_date.strftime("%d/%m/%Y")
        return f"{self.name}, start: {date_string}, priority: {self.priority}, estimate: ${self.cost_estimate:,.2f}, completion: {self.completion_percentage}%"

    def __lt__(self, other):
        return self.priority < other.priority

    def storage_format(self):
        """Returns a string in correct format for storage in .txt file."""
        date_string = self.start_date.strftime("%d/%m/%Y")
        return f"{self.name}\t{date_string}\t{self.priority}\t{self.cost_estimate:.1f}\t{self.completion_percentage}\n"
