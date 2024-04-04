'''
This file contains the Timer class for managing the Pomodoro timer.
'''
import time
class Timer:
    def __init__(self):
        self.is_running = False
        self.start_time = 0
        self.duration = 25 * 60  # 25 minutes in seconds
    def start(self):
        if not self.is_running:
            self.start_time = time.time()
            self.is_running = True
    def stop(self):
        if self.is_running:
            self.is_running = False
    def get_time_left(self):
        if self.is_running:
            elapsed_time = time.time() - self.start_time
            time_left = self.duration - int(elapsed_time)
            minutes = time_left // 60
            seconds = time_left % 60
            return f"{minutes:02d}:{seconds:02d}"
        else:
            return "00:00"
    def is_timer_running(self):
        return self.is_running