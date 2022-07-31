from tkinter.constants import CENTER
import requests
import tkinter as tk
import time
from threading import Thread
import pyautogui
import random

class Main():

    URL = "https://cleeryy.com/Pyrental/password.txt"

    def __init__(self) -> None:
        print("Initing the script.")
        self.password = self.fetchPassword()
        print(f"App password: {self.password}")
        self.createGui()
        self.root.update()
        self.mouseFreezing.start()
        self.root.mainloop()
        
    def fetchPassword(self) -> str:
        print("Getting the app password.")
        res = requests.get(self.URL)
        return res.text

    def blockingMouse(self) -> None:
        while True:
            self.moveMouse(random.randint(1, 1800), random.randint(1, 1920))

    def moveMouse(self, x, y) -> None:
        pyautogui.moveTo(x, y)

    def verifyingPassword(self, event) -> bool:
        print(repr(self.password))
        print(repr(f"{self.entryField.get()}\n"))
        if str(f"{self.entryField.get()}\n") in str(self.password):
            print("password's the one.")
        else:
            print("password's not the one.")
        
    def createGui(self) -> None:
        self.mouseFreezing = Thread(target=self.blockingMouse)
        print("Opening the GUI.")
        self.root = tk.Tk()
        self.root.title("Pyrental")
        self.root.attributes('-topmost', True)
        self.root.update()
        label = tk.Label(self.root, text="Entrer le mot de passe.").grid(row=0, column=0)
        self.entryField = tk.Entry(self.root, justify=CENTER)
        self.entryField.focus_set()
        self.entryField.bind("<Return>", self.verifyingPassword)
        self.entryField.grid(row=1, column=0)

if __name__ == "__main__":
    main = Main()
