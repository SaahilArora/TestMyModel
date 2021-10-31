import logging


class Logger:

    @staticmethod
    def __initLoggerFactory__(className):
        logging.info('Init Logger ', className)

    @staticmethod
    def __infoLogging__(msg):
        logging.info('Init ', msg)

