from tkinter.constants import CENTER
from datetime import date
import requests
import tkinter as tk
import time
from threading import Thread
import pyautogui
import os
import random

class Main():

    URL = "https://cleeryy.com/Pyrental/"

    def timer(self) -> None:
        res = int(requests.get(f"{self.URL}timer.txt").text)
        timeAlreadySpent = 0
        with open("timeSpent.log", "r") as f:
            timeAlreadySpent = int(f.read())
            f.close()

        with open("todaysDate.log", "r") as f:
            if str(date.today().day) not in f.read():
                with open("todaysDate.log", "w") as fw:
                    timeAlreadySpent = 0
                    fw.write(str(date.today().day))
                    fw.close()
            f.close()


        for i in range(timeAlreadySpent, res):
            with open("timeSpent.log", "w") as logFile:
                logFile.write(f"{i}")
                logFile.close()
            time.sleep(1)

    def initLocking(self) -> None:
        print("Initing the script.")
        self.password = self.fetchPassword()
        print(f"App password: {self.password}")
        print("Getting the screen size...")
        try:
            self.width, self.height = pyautogui.size()
            print(f"Screen size detected: {self.width}x{self.height}.")
        except:
            print("Unable to get the screen size.")
        self.createGui()
        self.root.update()
        self.root.after(2000, self.mouseFreezing.start())
        self.root.mainloop()

        
    def fetchPassword(self) -> str:
        print("Getting the app password.")
        res = requests.get(f"{self.URL}password.txt")
        return res.text


    def blockingMouse(self) -> None:
        print("Getting the screen size...")
        try: 
            self.width, self.height = pyautogui.size()
            print(f"Screen size detected: {self.width}x{self.height}.")
        except:
            print("Unable to get the screen size.")

        while True:
            if type(self.width) != int:
                self.moveMouse(random.randint(1, 1800), random.randint(1, 1920))
            else:
                self.moveMouse(self.width / 2, self.height / 2)


    def moveMouse(self, x, y) -> None:
        pyautogui.moveTo(x, y)


    def verifyingPassword(self, event) -> bool:
        print(repr(self.password))
        print(repr(f"{self.entryField.get()}\n"))
        if str(f"{self.entryField.get()}\n") in str(self.password):
            print("Password's the one.")
            os.system("shutdown -a")
            os._exit(0)
        else:
            print("Password's not the one.")
            os.system("shutdown -s -t 30")

        
    def createGui(self) -> None:
        self.mouseFreezing = Thread(target=self.blockingMouse)
        print("Opening the GUI.")
        self.root = tk.Tk()
        self.root.title("Pyrental")
        self.root.geometry(f"300x200+{int(self.width / 2 - 150)}+{int(self.height / 2 - 100)}")
        self.root.attributes('-topmost', True)
        self.root.focus_force()
        self.root.update()
        label = tk.Label(self.root, text="Entrer le mot de passe pour continuer à utiliser.").grid(row=0, column=0)
        self.entryField = tk.Entry(self.root, justify=CENTER)
        self.entryField.focus_set()
        self.entryField.bind("<Return>", self.verifyingPassword)
        self.entryField.grid(row=1, column=0)



if __name__ == "__main__":
    main = Main()
    main.timer()
    main.initLocking()
