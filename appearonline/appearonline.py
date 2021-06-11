"""
Main
"""
import time

import macmouse as mouse


class AppearOnline:
    """
    Appear online class
    """

    def __init__(self):
        pass

    def minute_passed(self) -> bool:
        time.sleep(60)
        return True

    def execute(self, run_time: int = 60):
        runtime_counter = 0
        while run_time > runtime_counter:
            if mouse.is_pressed(button='q'):
                break
            mouse.press(button='left')
            mouse.release(button='left')
            minute = self.minute_passed()
            if minute:
                runtime_counter += 1
