"""CP1404 Practical 07: Project Mangement Task"""


class Project:
    """A Project object."""

    def __init__(self, name="", start_date="", priority=1, cost_estimate=0.00, completion_percentage=0):
        self.name = name
        self.start_date = start_date  # May want this to be with datetime object
        self.priority = priority
        self.cost_estimate = cost_estimate
        self.completion_percentage = completion_percentage

    def __str__(self):
        return f"{self.name}, start: {self.start_date}, priority: {self.priority}, estimate: ${self.cost_estimate:,.2f}, completion: {self.completion_percentage}%"

    def __lt__(self, other):
        return self.priority < other.priority

    def format_for_storage(self):
        return f"{self.name}\t{self.start_date}\t{self.priority}\t{self.cost_estimate:.1f}\t{self.completion_percentage}"
