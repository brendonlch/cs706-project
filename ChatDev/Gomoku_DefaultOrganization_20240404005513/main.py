'''
This file contains the main logic for the Pomodoro timer application.
'''
import tkinter as tk
from tkinter import messagebox
from timer import Timer
class PomodoroApp:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Pomodoro Timer")
        self.timer = Timer()
        self.label = tk.Label(self.window, text="00:00", font=("Arial", 48))
        self.label.pack(padx=50, pady=20)
        self.start_button = tk.Button(self.window, text="Start", command=self.start_timer)
        self.start_button.pack(pady=10)
        self.stop_button = tk.Button(self.window, text="Stop", command=self.stop_timer, state=tk.DISABLED)
        self.stop_button.pack(pady=10)
        self.window.protocol("WM_DELETE_WINDOW", self.on_close)
    def start_timer(self):
        self.timer.start()
        self.update_timer()
        self.start_button.config(state=tk.DISABLED)
        self.stop_button.config(state=tk.NORMAL)
    def stop_timer(self):
        self.timer.stop()
        self.start_button.config(state=tk.NORMAL)
        self.stop_button.config(state=tk.DISABLED)
    def update_timer(self):
        time_left = self.timer.get_time_left()
        self.label.config(text=time_left)
        if self.timer.is_timer_running() and self.timer.get_time_left() == "00:00":
            messagebox.showinfo("Session Ended", "Pomodoro session has ended!")
        if self.timer.is_timer_running():
            self.window.after(1000, self.update_timer)
    def on_close(self):
        if messagebox.askokcancel("Quit", "Do you want to quit the application?"):
            self.window.destroy()
if __name__ == "__main__":
    app = PomodoroApp()
    app.window.mainloop()