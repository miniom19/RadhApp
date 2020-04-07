# Kivy Modules
from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager
# Screen Modules
from screens.welcomescreen import WelcomeScreen

class RadhApp(MDApp):
    def __init__(self, **kwargs):
        # Basic App configuration
        self.title = "RadhApp"
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "DeepPurple"
        super().__init__(**kwargs)

    def build(self):
        # Screen Manager on main
        screen_manager = ScreenManager()

        # screens
        welcome_screen = WelcomeScreen(name="welcome")

        # adition to the Screen Manager
        screen_manager.add_widget(welcome_screen)

        return screen_manager

if __name__ == '__main__':
    RadhApp().run()