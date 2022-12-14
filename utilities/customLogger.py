import logging
import logging.handlers

class LogGen:
    @staticmethod
    def loggen():
        logging.basicConfig(filename=".\\logs\\automation.log",
                            format='%(asctime)s: %(levelname)s: %(message)s',datefmt='%m/%d/%y %I:%M:%S %P')
        logger=logging.getLogger()

        logger.setLevel(logging.INFO)
        return logger

