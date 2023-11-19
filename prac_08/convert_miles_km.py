"""CP1404 Practical 08
Converting Miles to Kilometers Task
Estimated Time: 30 minutes
Actual Time: 42 minutes
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.properties import StringProperty

MILES_TO_KM = 1.60934


class MilesToKmApp(App):
    """App to convert miles to kilometres."""
    miles_input = StringProperty()

    def build(self):
        """Build the app."""
        Window.size = (500, 300)
        self.title = "Convert Miles to km"
        self.root = Builder.load_file("convert_miles_km.kv")
        self.miles_input = "Type in the field and press Enter"
        return self.root

    def handle_new_value(self):
        """Handles new value and converts it to miles."""
        miles = self.get_valid_input()
        kilometres = miles * MILES_TO_KM
        self.root.ids.output_label.text = f"{kilometres}"

    def get_valid_input(self):
        """Get a valid input from a text field."""
        try:
            new_value = float(self.root.ids.miles_text_input.text)
            return new_value
        except ValueError:
            return 0.0

    def handle_increment(self, increment):
        """Handles a increment to the current value in the text field and increments it by a particular amount."""
        value = self.get_valid_input() + increment
        self.root.ids.miles_text_input.text = f"{value}"
        self.handle_new_value()


MilesToKmApp().run()
