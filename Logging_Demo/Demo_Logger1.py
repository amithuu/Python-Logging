import logging


class filelogger:

    def filelog(self):

        # create logger
        logger = logging.getLogger("file_loger")
        logger.setLevel(logging.DEBUG)

        # adding the logger to file.
        file = logging.FileHandler("file_log_handler")

        # create formatter
        formatter = logging.Formatter('%(asctime)s - %(levelname)s : %(message)s', datefmt='%m/%d/%Y %I:%H:%S %p')

        # add formatter to file
        file.setFormatter(formatter)

        # add file handler to logger
        logger.addHandler(file)

        # log message
        logger.debug(" this is the debug message")
        logger.info(" this is the info message")
        logger.warning("this is the warning message")
        logger.error("this is the error message")
        logger.critical("this is the critical message")


lo = filelogger()
lo.filelog()
