import datetime
import random


def get_random_seconds():
    current_time = datetime.datetime.now()

    current_seconds = (current_time.minute % 10) * 60

    return random.randint(current_seconds, 600)

