# Level           When it’s used

# DEBUG           Detailed information, typically of interest only when diagnosing problems.

# INFO            Confirmation that things are working as expected.

# WARNING         An indication that something unexpected happened, or indicative of some problem in the near future (e.g. ‘disk space low’). The software is still working as expected.

# ERROR           Due to a more serious problem, the software has not been able to perform some function.

# CRITICAL        A serious error, indicating that the program itself may be unable to continue running.

# logging id mainly used to get the errors as we use in pytest @ xfail, so that we don't get message as error, in the same way we use these logging's, which keeps out data more securely and the messages which we want to pass as well.
import logging

logging.basicConfig(level=logging.DEBUG, filename=".....\logs\demologs.log", filemode='w')

# By default, level will be "Warning"


class DemoLogging1:
    def add_numbers(self, a, b):
        return a + b

    def multiply_numbers(self, a, b):
        return a * b


dl = DemoLogging1()
sum = dl.add_numbers(3, 5)
print(f"the addition is :{sum}")

# this is how we can use logging and their types.
logging.debug(f"the addition is :{sum}")
logging.info(f"the addition is :{sum}")
logging.warning(f"the addition is :{sum}")
logging.error(f"the addition is :{sum}")
logging.critical(f"the addition is :{sum}")

multi = dl.multiply_numbers(3, 5)
print(f"the multiply is :{multi}")
