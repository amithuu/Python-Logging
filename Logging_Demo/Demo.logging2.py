import logging

logging.basicConfig(format='%(asctime)s %(message)s', filename='log2.log', filemode='w', level=logging.DEBUG, datefmt='%m/%d/%Y %H:%M:%S %p')

class loggin():
    def add(self, a, b):
        return a+b

    def multi(self, a, b):
        return a * b


lo = loggin()
add = lo.add(2, 3)

logging.debug(f" this is add message{add}")
logging.info(f" this is add message{add}")
logging.warning(f" this is add message{add}")
logging.error(f" this is add message{add}")
logging.critical(f" this is add message{add}")

mul = lo.multi(3, 5)
logging.debug(f" this is multiply message {mul}")
logging.info(f" this is multiply message {mul}")
logging.warning(f" this is multiply message {mul}")
logging.error(f" this is multiply message {mul}")
logging.critical(f" this is multiply message {mul}")

