# Importing Tkinter for GUI and TheQuizzler class for launching the quiz
import tkinter as tk
from quizzler_creator_gui import TheQuizzler

# Initializes the main Tkinter window and runs the event loop to start the GUI application
if __name__ == "__main__":
    root = tk.Tk()
    app = TheQuizzler(root)
    root.mainloop()