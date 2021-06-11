"""
Main
"""
import time

import macmouse as mouse


class AppearOn:
    """
    Appear online class
    """

    def __init__(self):
        pass

    def minute_passed(self) -> bool:
        """
        Helper function to wait one minute.

        Returns:
            bool: Returns True after one minute
        """
        time.sleep(60)
        return True

    def execute(self, run_time: int = 60):
        """
        Execute method for Appear Online

        Args:
            run_time (int, optional): Minutes to run the package. Defaults to 60.
        """
        print(f"You will appear online for {run_time} minutes!")
        runtime_counter = 0
        while run_time > runtime_counter:
            if mouse.is_pressed(button='q'):
                break
            mouse.press(button='left')
            mouse.release(button='left')
            minute = self.minute_passed()
            if minute:
                runtime_counter += 1
