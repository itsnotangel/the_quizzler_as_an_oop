# Importing Tkinter for GUI and TheQuizzlerApp class for launching the quiz
import tkinter as tk
from quizzler_quiz_gui import TheQuizzlerApp

if __name__ == "__main__":
    root = tk.Tk()
    app = TheQuizzlerApp(root)
    root.mainloop()