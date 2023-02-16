## Quiero crear una aplicación para android con python
## La aplicación debe tener permitir introducir un mail y una contraseña para acceder a la aplicación.
## La aplicación debe tener un menú con 3 opciones: 
## 1. Mostrar el mail y la contraseña
## 2. Cambiar el mail y la contraseña
## 3. Salir de la aplicación
## La aplicación debe tener un botón para salir de la aplicación

import kivy
from kivy.app import App

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.popup import Popup
from kivy.uix.screenmanager import ScreenManager, Screen
 
class LoginScreen(Screen):
    def __init__(self, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)
        self.layout = BoxLayout(orientation='vertical')
        self.layout.add_widget(Label(text='Email'))
        self.email = TextInput(multiline=False)
        self.layout.add_widget(self.email)
        self.layout.add_widget(Label(text='Password'))
        self.password = TextInput(password=True, multiline=False)
        self.layout.add_widget(self.password)
        self.login = Button(text='Login')
        self.login.bind(on_press=self.login_pressed)
        self.layout.add_widget(self.login)
        self.add_widget(self.layout)
 
    def login_pressed(self, instance):
        if self.email.text == 'admin' and self.password.text == 'admin':
            self.parent.current = 'menu' # switch to menu screen from login screen 
        else:
            show_popup() # show popup if login is incorrect 
             
class MenuScreen(Screen):
    def __init__(self, **kwargs):
        super(MenuScreen, self).__init__(**kwargs)
        self.layout = BoxLayout(orientation='vertical')
        self.layout.add_widget(Label(text='Menu'))
        self.show = Button(text='Show')
        self.show.bind(on_press=self.show_pressed)
        self.layout.add_widget(self.show)
        self.change = Button(text='Change')
        self.change.bind(on_press=self.change_pressed)
        self.layout.add_widget(self.change)
        self.exit = Button(text='Exit')
        self.exit.bind(on_press=self.exit_pressed)
        self.layout.add_widget(self.exit)
        self.add_widget(self.layout)
 
    def show_pressed(self, instance):
        show_popup() # show popup with email and password
         
    def change_pressed(self, instance):
        self.parent.current = 'login' # switch to login screen from menu screen
         
    def exit_pressed(self, instance):
        self.parent.current = 'login' # switch to login screen from menu screen 
         
class MyApp(App):
    def build(self):
        self.sm = ScreenManager()
        self.sm.add_widget(LoginScreen(name='login'))
        self.sm.add_widget(MenuScreen(name='menu'))
        return self.sm 
    
def show_popup():
    show = Popup(title='Show',
        content=Label(text='Email: admin Password: admin'), size_hint=(None, None), size=(400, 400)) 
    show.open()
     
if __name__ == '__main__':
    MyApp().run() 
    
 
