"""CP1404 Practical 08 Box Layout example
Time Estimate: 10 minutes
Time Actual: 8 minutes
"""

from kivy.app import App
from kivy.lang import Builder


class BoxLayoutDemo(App):
    """Program that greets the user based on a name inputted by the user."""
    def build(self):
        """Builds the box layout demo app."""
        self.title = "Box Layout Demo"
        self.root = Builder.load_file('box_layout.kv')
        return self.root

    def handle_greet(self):
        """Greets the user."""
        self.root.ids.output_label.text = f"Hello {self.root.ids.input_name.text}"

    def handle_clear(self):
        """Clears the output label"""
        self.root.ids.output_label.text = ""


BoxLayoutDemo().run()
