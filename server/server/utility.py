"""
Utility helpers for the python server
"""

import time
import random

def choice(els):
    return random.SystemRandom().choice(els)

def epoch_timestamp():
    return int(time.time())
