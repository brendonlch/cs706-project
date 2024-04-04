from tkinter import Tk, Label, Button

class PomodoroTimer:
    def __init__(self, master, session_duration=25):
        self.master = master
        self.session_duration = session_duration * 60  # Convert minutes to seconds
        self.remaining_time = self.session_duration
        self.is_break = False
        self.is_running = False
        self.timer_label = Label(master, text=self.time_string(), font=("Helvetica", 36))
        self.timer_label.pack()
        self.status_label = Label(master, text="", font=("Helvetica", 14))
        self.status_label.pack()

    def time_string(self):
        minutes, seconds = divmod(self.remaining_time, 60)
        return f"{minutes:02d}:{seconds:02d}"

    def start_session(self):
        if not self.is_running:
            self.is_running = True
            self.is_break = False
            self.remaining_time = self.session_duration  # Reset the time
            self.update_time_display()
            self.update_status('Session started')
            self.count_down()

    def pause_session(self):
        self.is_running = False
        self.update_status('Session paused')

    def resume_session(self):
        if not self.is_running and self.remaining_time > 0:
            self.is_running = True
            self.update_time_display()
            self.update_status('Session resumed')
            self.count_down()

    def reset_session(self):
        self.is_running = False
        self.is_break = False
        self.remaining_time = self.session_duration
        self.update_time_display()
        self.update_status('Session reset')

    def update_time_display(self):
        self.timer_label.config(text=self.time_string())

    def update_status(self, status):
        self.status_label.config(text=status)

    def count_down(self):
        if self.is_running and self.remaining_time > 0:
            self.remaining_time -= 1
            self.update_time_display()
            self.master.after(1000, self.count_down)  # Wait for 1 second
        elif self.remaining_time == 0:
            self.is_break = not self.is_break  # Toggle break status
            self.is_running = False
            self.update_status('Time is up!')

if __name__ == "__main__":
    root = Tk()
    root.title("Pomodoro Timer")

    timer = PomodoroTimer(root, session_duration=25)

    start_button = Button(root, text="Start", command=timer.start_session)
    start_button.pack()

    pause_button = Button(root, text="Pause", command=timer.pause_session)
    pause_button.pack()

    resume_button = Button(root, text="Resume", command=timer.resume_session)
    resume_button.pack()

    reset_button = Button(root, text="Reset", command=timer.reset_session)
    reset_button.pack()

    root.mainloop()