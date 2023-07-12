import logging

# Create logger
# create console handler or file handler and set the log level
# create formatter: how you want your logs to perform
# add formatter to condole or file handler
# add console handler to logger
# application code- log messages


class Logger:
    def loger(self):
        # create
        logger = logging.getLogger("logdemo")
        logger.setLevel(logging.DEBUG)
        # we have crated a logger and given name for the logger using get.logger() function
        # And we are setting the level for the logger.

        # create console handler
        ch = logging.StreamHandler()

        # to add the message or to display the message in the console we use StreamHandler() function.

        # create formatter
        formatter = logging.Formatter('%(asctime)s - %(levelname)s : %(message)s', datefmt='%m/%d/%Y %H:%M:%S %p')

        # here we are formatting the message how we need to display on the console.

        # Add Formatter console to logger
        ch.setFormatter(formatter)

        # here we are adding the formatter to console using the function setFormatter() using console handler variable.

        # add consoler handler to logger
        logger.addHandler(ch)

        # here we are adding the console to the logger, so that is sends the message to console.

        # application code or the log messages.
        logger.debug(" this is the debug message")
        logger.info(" this is the info message")
        logger.warning("this is the warning message")
        logger.error("this is the error message")
        logger.critical("this is the critical message")



lo = Logger()
lo.loger()

