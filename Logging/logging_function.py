"""
This function allows for the creation of a Logging Handler, setting the logging level,
and formatting the output in a very descriptive and structured way.  Logging levels can
be selected by their integer levels:

NOTSET: 0
DEBUG: 10
INFO: 20
WARNING: 30
ERROR: 40
CRITICAL: 50

The output format is configured as such:

   Date    Timezone+-  Time + 3   Log   Script   Func.     Code    Log message
           GMT offset  Millisec.  Lvl   name     name    line num     text
---------- -------- ------------- ---- --------------------------  -----------
YYYY-MM-DD CDT-0500 HH:MM:SS.msec INFO (module, function, lineNo): Log Message

**Note: The timezone and GMT offset is placed BEFORE the time due to formatting limitations, which interfere with 
        the ability to display milliseconds at the end of the time stamp.  Much troubleshooting and gnashing of
        teeth was required to figure this out :).
"""
import logging

def config_logging(level):
    """
    Configures logging handler for the script

    param level: Numeric logging level to set (0, 10, 20, 30, 40, 50), default=20 (INFO)

    Example output: 2025-06-25 CDT-0500 16:12:52.154 INFO (myscript, myfunction, 123): testing
    Format: YYYY-MM-DD [timezone][+,-][GMT offset] HH:mm:ss.msec [logging level] (module, function, lineNo): [message]
    """
    logger = logging.getLogger(__name__)
    logger.setLevel(level)
    logging.basicConfig(format='%(asctime)s.%(msecs)03d %(levelname)s (%(module)s, %(funcName)s, %(lineno)d): %(message)s', datefmt='%Y-%m-%d %Z%z %H:%M:%S')
    return logger
