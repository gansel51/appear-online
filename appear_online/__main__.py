"""
Controller file for Appear Online
"""

import argparse

from appearonline import AppearOnline

parser = argparse.ArgumentParser()
parser.add_argument('--runtime', required=False, type=int, help='Please specify the time for AppearOnline to run.')
run_time = parser.parse_args().runtime

def main():
    """
    Method to run AppearOnline
    """
    AO = AppearOnline()
    AO.execute(run_time) if (run_time is not None) else AO.execute()
