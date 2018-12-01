"""
Base class all demo classes should inherit
Totally stolen from tgt_grease
"""
#import tgt_mage
from abc import ABCMeta
import logging

LOGGER_NAME: str = 'api-demo.mather'

class CLASS(object):
    """Core class object that all demo classes come from

    Attributes:
        log (logging.Logger): instance of log

    """

    __log: logging.Logger

    def __init__(self):
        super(CLASS, self).__init__()
        self.__metadata__ = ABCMeta
        self.log = logging.getLogger(LOGGER_NAME)

    @property
    def log(self) -> logging.Logger:  # pylint: disable=C0111
        return self.__log

    @log.setter
    def log(self, l: logging.Logger):
        self.__log = l
