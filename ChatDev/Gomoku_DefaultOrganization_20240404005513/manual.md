# Pomodoro Timer User Manual

## Introduction

The Pomodoro Timer is a simple application that helps you implement the Pomodoro technique, a time management method developed by Francesco Cirillo. This technique uses a timer to break work into intervals, traditionally 25 minutes in length, separated by short breaks. The Pomodoro Timer application provides a user-friendly interface to track your work sessions and receive notifications when a session ends.

## Installation

To use the Pomodoro Timer, you need to have Python installed on your machine. You can download Python from the official website: [https://www.python.org/downloads/](https://www.python.org/downloads/)

Once you have Python installed, you can follow these steps to install the required dependencies and run the application:

1. Open a terminal or command prompt.
2. Navigate to the directory where you have saved the `main.py` and `timer.py` files.
3. Install the required dependencies by running the following command:

   ```
   pip install tkinter
   ```

   This will install the `tkinter` library, which is used for creating the user interface.

## Usage

To start using the Pomodoro Timer, follow these steps:

1. Open a terminal or command prompt.
2. Navigate to the directory where you have saved the `main.py` and `timer.py` files.
3. Run the following command to start the application:

   ```
   python main.py
   ```

4. The Pomodoro Timer window will open.
5. Click the "Start" button to start a work session. The timer will start counting down from 25 minutes.
6. Work on your task until the timer reaches 0.
7. When the session ends, a notification will be displayed, indicating that the Pomodoro session has ended.
8. You can click the "Stop" button to stop the timer before the session ends.
9. To quit the application, click the close button (X) on the window or use the keyboard shortcut Alt+F4.

## Customization

If you want to customize the duration of the work sessions or the notification message, you can modify the `timer.py` file.

1. Open the `timer.py` file in a text editor.
2. Locate the line that defines the duration of the work sessions:

   ```python
   self.duration = 25 * 60  # 25 minutes in seconds
   ```

   You can change the value `25` to the desired number of minutes.

3. To customize the notification message, locate the following lines in the `main.py` file:

   ```python
   if self.timer.is_timer_running() and self.timer.get_time_left() <= 0:
       messagebox.showinfo("Session Ended", "Pomodoro session has ended!")
   ```

   You can modify the strings `"Session Ended"` and `"Pomodoro session has ended!"` to your preferred notification message.

4. Save the changes to the file.

## Conclusion

The Pomodoro Timer is a useful tool for implementing the Pomodoro technique and improving your productivity. By following the installation instructions and using the application as described in this manual, you can effectively manage your work sessions and stay focused on your tasks.