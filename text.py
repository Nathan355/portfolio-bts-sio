from pynput.keyboard import Controller
import time

time.sleep(5)


keyboard = Controller()


texte = "Bonjour, ceci est un test de frappe automatique."


for char in texte:
    keyboard.type(char)  # Tape chaque caractère
    time.sleep(0.1)  # Pause entre chaque frappe pour simuler une frappe humaine