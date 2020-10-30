from copy import copy
from logging import Formatter

# Log coloring start
MAPPING = {
    'DEBUG'     : 36,  # Cyan
    'INFO'      : 37,  # White
    'WARNING'   : 33,  # Yellow
    'ERROR'     : 31,  # Red
    'CRITICAL'  : 41   # White on red bg
}

PREFIX = '\u001b['
SUFFIX = '\u001b[0m'


class ColoredFormatter(Formatter):
    def __init__(self, pattern):
        Formatter.__init__(self, pattern)

    def format(self, record):
        colored_record = copy(record)
        levelname = colored_record.levelname
        seq = MAPPING.get(levelname, 37)  # Default white
        colored_levelname = ('{0}{1}m{2}{3}') \
            .format(PREFIX, seq, levelname, SUFFIX)
        colored_record.levelname = colored_levelname
        return Formatter.format(self, colored_record)
