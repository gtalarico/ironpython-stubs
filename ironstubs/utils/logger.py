import os
import logging
from logging.config import dictConfig
LOG_LEVEL = 'INFO'

LOGGER_CONFIG = {
      "version": 1,
      "disable_existing_loggers": True,
      "handlers": {
          "console": {
              "class": "logging.StreamHandler",
              "formatter": "simple",
              },
          "file_handler": {
              "class": "logging.FileHandler",
              "formatter": "simple",
              "filename": "logs\\log.log"
              },
          },
      "formatters": {
          "simple": {
              "format": "[%(levelname)s] %(message)s [%(asctime)s]",
              "datefmt": "%Y:%m:%d - %I:%M:%S"
              }
      },

      "loggers": {
          "": {
              "handlers": ["console", "file_handler"],
              "level": LOG_LEVEL
              }
      }
}

log_levels = {50: 'CRITICAL',
              40: 'ERROR',
              30: 'WARNING',
              20: 'INFO',
              10: 'DEBUG',
              0: 'NOTSET'}

dictConfig(LOGGER_CONFIG)
logger = logging.getLogger()
logger.debug('** LOG LEVEL: {}'.format(log_levels[logger.getEffectiveLevel()]))

def enable_debug():
  logger.setLevel(logging.DEBUG)
logger.enable_debug = enable_debug
