"""CP1404 Practical 08: Dynamic Labels exercise
Estimated Time: 20 minutes
Actual Time: 18 minutes
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label


class DynamicLabelsApp(App):
    """Main program for dynamic labels exercise"""

    def __init__(self, **kwargs):
        """Initialise the App"""
        super().__init__(**kwargs)
        self.names = ["Anna", "Bob", "Carl", "Dave", "Edna"]

    def build(self):
        """Build the Dynamic Labels GUI."""
        self.title = "Dynamic Labels"
        self.root = Builder.load_file("dynamic_labels.kv")
        self.create_widgets()
        return self.root

    def create_widgets(self):
        """Create a set of labels from names list."""
        for name in self.names:
            # Create a label for each name in the list
            temp_label = Label(text=name)
            temp_label.font_size = 36
            temp_label.color = (1, 1, 0, 1)
            # Add the label to the main BoxLayout
            self.root.ids.main.add_widget(temp_label)


DynamicLabelsApp().run()
