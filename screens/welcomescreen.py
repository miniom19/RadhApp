from kivy.uix.screenmanager import Screen
from kivy.uix.floatlayout import FloatLayout
from kivymd.button import MDFlatButton

class WelcomeScreen(Screen):
    def __init__(self, *args, **kwargs):
        super(WelcomeScreen, self).__init__()

        # Layouts

        self.root = FloatLayout()
        self.add_widget(self.root)

        # Widgets
        self.test_button = MDFlatButton(
            text= "Hello World",
            pos_hint={"center_x": 0.5, "center_y": 0.5},
        )

        # Widget to Layout

        self.root.add_widget(self.test_button)
