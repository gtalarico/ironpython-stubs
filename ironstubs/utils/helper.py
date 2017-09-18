import os
import time
from collections import defaultdict
from ConfigParser import ConfigParser
from .logger import logger

class Timer(object):
    "Time and TimeIt Decorator"
    def __init__(self):
        self.start_time = time.time()

    def stop(self):
        end_time = time.time()
        duration = end_time - self.start_time
        return duration

    @staticmethod
    def time_function(name):
        def wrapper(func):
            def wrap(*ags, **kwargs):
                logger.debug('START: {}'.format(name))
                t = Timer()
                rv = func(*ags, **kwargs)
                duration = t.stop()
                logger.debug('Done: {} sec'.format(duration))
                return rv
            return wrap
        return wrapper
