from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton
from kivy.properties import ObjectProperty
from database import MySQLdb



account_kv = Builder.load_file('account.kv')

class RegisterAccountScreen(Screen):
    dialog = None

    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.db  = MySQLdb()
    
    
    def register_btn_click(self):
        self.ids.register_btn.text = 'account created'
        fullname = self.ids.fullname.text
        username = self.ids.username.text
        email = self.ids.email.text
        password = self.ids.password.text
        create_user = self.db.create_user(fullname, username, email, password)
        


    def show_alert_dialog(self):
        if not self.dialog:
            self.dialog = MDDialog(
                text="User has registered successfully",
                buttons=[
                    MDFlatButton(
                        text="Login",
                    ),
                    MDFlatButton(
                        text="CANCEL",
                        on_press= self.close_dialog()
                    ),
                ],
            )
        self.dialog.open()

    def close_dialog(self,obj):
        self.dialog.dismiss()

    



class LoginScreen(Screen):
    dialog = None

    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.db  = MySQLdb()

    def user_login(self):
        username = self.ids.login_username.text
        password = self.ids.login_password.text
        self.db.login(username, password)


        

    def show_alert_dialog(self):
        if not self.dialog:
            self.dialog = MDDialog(
                text="User has logged in"
            )
        self.dialog.open()

    def close_dialog(self):
        self.dialog.dismiss()

    


class UserProfile(Screen):
    pass


