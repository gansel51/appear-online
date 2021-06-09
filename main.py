"""
Main
"""
import sys
import time

import pyautogui as pya

class AppearOnline:
    """
    Appear online class
    """

    def __init__(self):
        pass

    def minute_passed(self) -> bool:
        time.sleep(60)
        return True

    def execute(self, run_time: int = 300):
        runtime_counter = 0
        while run_time > runtime_counter:
            pya.press("shift")
            minute = self.minute_passed()
            if minute:
                runtime_counter += 1



