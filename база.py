import sqlite3
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.graphics import Color, Rectangle
from kivy.uix.anchorlayout import AnchorLayout
from passlib.hash import pbkdf2_sha256

class RegistrationApp(App):
    def build(self):
        # создаем подключение к базе данных
        conn = sqlite3.connect("user_data.db")

        # создаем курсор для выполнения SQL-запросов

        cursor = conn.cursor()

        # Создаем таблицу для хранения имени и пароля

        cursor.execute (""" 
                   CREATE TABLE IF NOT EXISTS users (
                        id INTENGER PRIMARY KEY AUTOINCREMENT,
                        username TEXT NOT NULL,
                        password TEXT NOT NULL
                   )
                   """

        )
        # Сохраняем изменения и закрываем соединение с базой данных
        conn.commit()
        conn.close()
        # Добавить другие экраны и настройки приложения как обычно

        def check_credentials(self, instsnce):
            name = self.name_input.text
            password = self.password_input.text

            if name and password:
                # Создаем подключение к базе данных
                conn = sqlite3.connect("user_data.db")
                cursor = conn.cursor()

                # Вставляем имя и пароль в таблицу
                cursor.execute('INSERT INTO users (username, password) VALUES (?, ?)', (name, password))

                # Сохраняем изменения и закрываем соединение
                conn.commit()
                conn.close()

                # Переходите на другой экран и т. д.