from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.graphics import Color, Rectangle
from kivy.core.window import Window
import sqlite3
from kivy.uix.anchorlayout import AnchorLayout

class CustomBoxLayout(BoxLayout):
    def __init__(self, **kwargs):
        super(CustomBoxLayout, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = 10
        self.spacing = 10
        with self.canvas.before:
            Color(1, 1, 1, 1)  # Белый фон
            self.rect = Rectangle(size=self.size, pos=self.pos)
        self.bind(size=self._update_rect, pos=self._update_rect)

    def _update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size

class RegistrationScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = CustomBoxLayout()
        self.add_widget(layout)

        label = Label(text="Вход", color=(0, 0, 0, 1), font_size="20sp")
        layout.add_widget(label)

        self.name_input = TextInput(hint_text="Имя", size_hint=(None, None), size=(200, 40))
        self.name_input.pos_hint = {'center_x': 0.5}
        layout.add_widget(self.name_input)

        self.password_input = TextInput(hint_text="Пароль", password=True, size_hint=(None, None), size=(200, 40))
        self.password_input.pos_hint = {'center_x': 0.5}
        layout.add_widget(self.password_input)

        btn = Button(text="Войти", size_hint=(None, None), size=(200, 40))
        btn.pos_hint = {'center_x': 0.5}
        btn.bind(on_release=self.check_credentials)
        layout.add_widget(btn)

        self.btn = btn
        
        self.entered_name = ""

        self.bind(size=self.on_size)

    def on_size(self, instance, value):
        window_width, window_height = self.size
        self.name_input.size = (window_width * 0.4, window_height * 0.1)
        self.name_input.font_size = window_width * 0.02
        self.password_input.size = (window_width * 0.4, window_height * 0.1)
        self.password_input.font_size = window_width * 0.02
        self.btn.size = (window_width * 0.4, window_height * 0.1)
        self.btn.font_size = window_width * 0.02

    def check_credentials(self, instance):
        name = self.name_input.text
        password = self.password_input.text
        self.entered_name = name


        if name and password:
            conn = sqlite3.connect("user_data.db")
            cursor = conn.cursor()
            cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (name, password))
            conn.commit()
            conn.close()

            app = App.get_running_app()
            app.root.transition.direction = 'left'
            app.root.current = 'welcome'

class WelcomeScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = CustomBoxLayout()
        self.add_widget(layout)

        label = Label(
            text="Для того, чтобы пройти наш маршрут вам нужно:\n1. Выбрать свою возрастную категорию\n2. Выбрать категорию здоровья\n3. Выбрать маршрут",
            color=(0, 0, 0, 1),
            font_size="20sp"
        )
        layout.add_widget(label)

        btn_1 = Button(
            text="Далее",
            size_hint=(None, None),
            size=(200, 40),
            pos_hint={"center_x": 0.5, "y": 0.1}
        )
        btn_1.bind(on_release=self.go_to_third_screen)
        layout.add_widget(btn_1)

        self.btn_1 = btn_1

        self.bind(size=self.on_size_2)

    def on_size_2(self, instance, value):
        window_width, window_height = self.size
        self.btn_1.size = (window_width * 0.4, window_height * 0.1)
        self.btn_1.font_size = window_width * 0.1

    def go_to_third_screen(self, instance):
        app = App.get_running_app()
        app.root.transition.direction = "left"
        app.root.current = "third"

class ThirdScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = CustomBoxLayout()
        self.add_widget(layout)

        label = Label(
            text="Третий экран",
            color=(0, 0, 0, 1)
        )
        layout.add_widget(label)

        btn_2 = Button(
            text="Далее",
            size_hint=(None, None),
            pos_hint={"center_x": 0.5, "y": 0.1}
        )
        btn_2.bind(on_release=self.go_to_superscreen)
        layout.add_widget(btn_2)

        self.btn_2 = btn_2

        self.bind(size=self.on_size)
    
    def go_to_superscreen(self, instance):
        app = App.get_running_app()
        app.root.transition.direction = "left"
        app.root.current = "superscreen"

    def on_size(self, instance, value):
       window_width, window_height = self.size
       self.btn_2.size = (window_width * 0.4, window_height * 0.1)
       self.btn_2.font_size = window_width * 0.02
#
 #   def go_to_profile_screen(self, instance):
  #      app = App.get_running_app()
  #      profile_screen = app.root.get_screen("profile")
  #      conn = sqlite3.connect("user_data.db")
  #      cursor = conn.cursor()
  #      cursor.execute("SELECT username FROM users")
  #      result = cursor.fetchone()
  #      conn.close()

 #       if result:
  #          username = result[0]
   #         profile_screen.label.text = f" {username}"
#
 #       app.root.current = "profile"

class ThirdScreen_1(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = CustomBoxLayout()
        self.add_widget(layout)

        label = Label(
            text="xjjnsdf",
            color=(0, 0, 0, 1),
            font_size="20sp"
        )
        layout.add_widget(label)

        btn_3 = Button(
            text="Завершить",
            size_hint=(None, None),
            size=(200, 40)
        )
        btn_3.pos_hint = {"center_x": 0.5}
        btn_3.bind(on_release=self.go_to_welcome)
        layout.add_widget(btn_3)

        self.btn_3 = btn_3

        self.bind(size=self.on_size_4)

    def on_size_4(self, instance, value):
        window_width, window_height = self.size
        self.btn_3.size = (window_width * 0.4, window_height * 0.1)
        self.btn_3.font_size = window_width * 0.02

    def go_to_welcome(self, instance):
        app = App.get_running_app()
        app.root.transition.direction = "left"
        app.root.current = "welcome"

class SuperScreen(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        layout = CustomBoxLayout()
        self.add_widget(layout)

        self.label = Label(
             text = "Главный экран",
             color = (0, 0, 0, 1)
        )
        layout.add_widget(self.label)
        
        anchor_layout = AnchorLayout(
            anchor_x ="right",
            anchor_y = "bottom")

        btn_4 = Button(
            text="text",
            size_hint = (None, None),
            pos_hint= {"center_x": 0.5, "y": 0.1}
        )
        btn_4.bind(on_release=self.go_to_profile_screen)
        layout.add_widget(btn_4)

        self.btn_4 = btn_4

        #self.bind(size=self.on_size)

       # Создайте новый BoxLayout для btn_6
        box_layout_for_btn_6 = BoxLayout(
            orientation="vertical", 
            size_hint=(None, None))

        btn_6 = Button(
            text="Упражнения",
            size_hint=(None, None),
        )
        btn_6.bind(on_release=self.go_to_exesex_screen)  # Исправлено название метода
        box_layout_for_btn_6.add_widget(btn_6)  # Добавьте кнопку btn_6 в новый BoxLayout

        anchor_layout.add_widget(box_layout_for_btn_6)  # Добавьте новый BoxLayout в anchor_layout
        layout.add_widget(anchor_layout)  # Добавьте anchor_layout в layout

        self.btn_6 = btn_6

        self.bind(size=self.on_size)

    def on_size(self, instance, value):
        window_width, window_height = self.size
        self.btn_4.size = (window_width * 0.4, window_height * 0.1)
        self.btn_4.font_size = window_width * 0.02
        self.btn_6.size = (window_width * 0.4, window_height * 0.1)
        self.btn_6.font_size = window_width * 0.02

    def go_to_profile_screen(self, instance):
        app = App.get_running_app()
        profile_screen = app.root.get_screen("profile")
        conn = sqlite3.connect("user_data.db")
        cursor = conn.cursor()
        cursor.execute("SELECT username FROM users")
        result = cursor.fetchone()
        conn.close()

        if result:
            username = result[0]
            profile_screen.set_username(username)
            profile_screen.label.text = f" {username}"

        app.root.current = "profile"
    
    def go_to_profile_screen(self, instance):
        app = App.get_running_app()
        registration_screen = app.root.get_screen("registration")
        new_username = registration_screen.entered_name  # Получите новое имя из RegistrationScreen

        conn = sqlite3.connect("user_data.db")
        cursor = conn.cursor()
        cursor.execute("UPDATE users SET username = ?", (new_username,))
        conn.commit()
        conn.close()

        profile_screen = app.root.get_screen("profile")
        profile_screen.set_username(new_username)  # Обновите имя пользователя на экране профиля
        app.root.current = "profile"
      
        anchor_layout = AnchorLayout(
            anchor_x ="left",
            anchor_y = "bottom")
        
    def go_to_exesex_screen(self, instance):
        print("button click")
        app = App.get_running_app()
        app.root.current = "third_1"


class ProfileScreen(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        layout = CustomBoxLayout()
        self.add_widget(layout)

        self.label = Label(
            text="имя пользователя: ",
            color=(0, 0, 0, 1)
        )
        layout.add_widget(self.label)

        anchor_layout = AnchorLayout(
            anchor_x ="left",
            anchor_y = "top")
          
        btn_5 = Button(
            text="Назад", 
            size_hint = (None, None),
        )
        btn_5.bind(on_release=self.go_to_profile_screen_1)
        layout.add_widget(btn_5)

        self.btn_5 = btn_5

        self.bind(size=self.on_size)

    def on_size(self, instance, value):
        window_width, window_height = self.size
        self.btn_5.size = (window_width * 0.4, window_height * 0.1)
        self.btn_5.font_size = window_width * 0.02

    def go_to_profile_screen_1(self, instance):
        print("button click")
        app = App.get_running_app()
        app.root.current = "superscreen"

        #self.load_username()

    def set_username(self, username):
        self.label.text = f"имя пользователя: {username}"

    def update_username(self, new_username):
        conn = sqlite3.connect("user_data.db")
        cursor = conn.cursor()
        cursor.execute("UPDATE users SET username = ?", (new_username,))
        conn.commit()
        conn.close()
        self.set_username(new_username)

    def load_username(self):
        conn = sqlite3.connect("user_data.db")
        cursor = conn.cursor()
        cursor.execute("SELECT username FROM users")
        result = cursor.fetchone()
        conn.close()

        if result:
            username = result[0]
            self.set_username(username)

    def on_enter(self):
        conn = sqlite3.connect("user_data.db")
        cursor = conn.cursor()
        cursor.execute("SELECT username FROM users")
        result = cursor.fetchone()
        conn.close()

        if result:
            username = result[0]
            self.set_username(username)
            #self.label.text = f"имя пользователя: {username}"
            print("Имя в профиле обновлено:", username)
    
    def set_username(self, username):
        self.label.text = f"имя пользователя: {username}"

    def load_username(self):
        conn = sqlite3.connect("user_data.db")
        cursor = conn.cursor()
        cursor.execute("SELECT username FROM users")
        result = cursor.fetchone()
        conn.close()

        if result:
            username = result[0]
            self.set_username(username)

    def check_profile(self, instance):
        conn = sqlite3.connect("user_data.db")
        cursor = conn.cursor()
        cursor.execute("SELECT username FROM users")
        result = cursor.fetchone()
        conn.close()

        if result:
            username = result[0]
        else:
            username = "пользователь"

        self.label.text = f"имя пользователя: {username}"



class RegistrationApp(App):
    def build(self):
        Window.size = (720, 1280)  # Установите размер окна приложения при его запуске
        sm = ScreenManager()
        sm.add_widget(RegistrationScreen(name="registration"))
        sm.add_widget(SuperScreen(name="superscreen"))
        sm.add_widget(WelcomeScreen(name="welcome"))
        sm.add_widget(ThirdScreen(name="third"))
        sm.add_widget(ThirdScreen_1(name="third_1"))
        profile_screen = ProfileScreen(name="profile")
        sm.add_widget(profile_screen)
        profile_screen.load_username()  # Загрузите имя пользователя при запуске приложения
        return sm

if __name__ == '__main__':
    RegistrationApp().run()


