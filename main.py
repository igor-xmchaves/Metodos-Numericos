from tkinter import *
from user.app import Application

def main():
    root = Tk()
    app = Application(root)
    app.mainloop()

if __name__ == "__main__":
    main()