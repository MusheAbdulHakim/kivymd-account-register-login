from kivymd.app import MDApp
from kivy.lang import Builder



class MainApp(MDApp):
    from account import LoginScreen, RegisterAccountScreen,UserProfile

    def build(self):
        self.theme_cls.theme_style="Dark"
    
    


if __name__ == '__main__':
    MainApp().run()

