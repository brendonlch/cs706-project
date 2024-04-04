## main.py

from PomodoroTimer import PomodoroTimer

def main():
    root = Tk()
    root.title("Pomodoro Timer")
    # Create an instance of PomodoroTimer
    pomodoro_timer = PomodoroTimer(session_duration=25)

    # Start the session
    pomodoro_timer.start_session()

if __name__ == "__main__":
    main()
