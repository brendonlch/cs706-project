## test_main.py

import unittest
from PomodoroTimer import PomodoroTimer

class TestPomodoroTimer(unittest.TestCase):

    def test_session_duration_default(self):
        pomodoro_timer = PomodoroTimer()
        self.assertEqual(pomodoro_timer.session_duration, 25)

    def test_start_session(self):
        pomodoro_timer = PomodoroTimer(session_duration=25)
        self.assertIsNone(pomodoro_timer.start_session())

if __name__ == '__main__':
    unittest.main()
