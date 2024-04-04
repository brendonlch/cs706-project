import unittest
from unittest.mock import patch
from tkinter import Tk, Label, Button
from data.pomodoro_timer.PomodoroTimer import PomodoroTimer

class TestPomodoroTimer(unittest.TestCase):

    def setUp(self):
        self.timer = PomodoroTimer()

    def test_initial_state(self):
        self.assertEqual(self.timer.session_duration, 25)
        self.assertFalse(self.timer.is_break)
        self.assertFalse(self.timer.is_running)

    def test_start_session(self):
        self.timer.start_session()
        self.assertTrue(self.timer.is_running)

    def test_pause_session(self):
        self.timer.pause_session()
        self.assertFalse(self.timer.is_running)

    def test_resume_session(self):
        self.timer.resume_session()
        self.assertTrue(self.timer.is_running)

    def test_reset_session(self):
        self.timer.reset_session()
        self.assertFalse(self.timer.is_running)
        self.assertFalse(self.timer.is_break)

    @patch('data.pomodoro_timer.PomodoroTimer.notification.notify')
    def test_send_notification(self, mock_notify):
        message = 'Test message'
        self.timer.send_notification(message)
        mock_notify.assert_called_once_with(title='Pomodoro Timer', message=message)

if __name__ == '__main__':
    unittest.main()
