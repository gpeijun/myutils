# -*- coding: utf-8 -*-
import time
import logging
import logging.handlers
from functools import wraps


def get_logger(fn):
    """
    a rotated and formated logger 
    """
    handler = logging.handlers.TimedRotatingFileHandler(
        fn, when='D', interval=1, backupCount=1)
    fmt = "[%(levelname)1.1s %(asctime)s %(name)s %(module)s:%(lineno)d] %(message)s"
    formatter = logging.Formatter(fmt, "%y%m%d %H:%M:%S")
    handler.setFormatter(formatter)
    logger = logging.getLogger()
    logger.addHandler(handler)
    logger.setLevel(logging.INFO)
    return logger


def func_timer(function):
    """
    a decorator for counting time during performing function

    """
    @wraps(function)
    def function_timer(*args, **kwargs):
        t0 = time.time()
        result = function(*args, **kwargs)
        t1 = time.time()
        logging.info("[%s] %s %s end, cost %sms!" % (
            function.__name__, args, kwargs, 
            1000 * (t1 - t0)))
        return result
    return function_timer
