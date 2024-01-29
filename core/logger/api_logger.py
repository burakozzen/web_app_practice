import logging
import logging.handlers


class ApiLogger(object):
    __instance = None

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, 'instance'):
            cls.__instance = super(ApiLogger, cls).__new__(cls)
        return cls.__instance

    def __init__(self, name: str = "api"):
        self.name = name
        self.logger = logging.getLogger(name=name)
        self.log_format = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        self.setup_logging()

    def setup_logging(self):
        # add log format
        logging.basicConfig(level=logging.INFO, format=self.log_format)

        # configure formatter for logger
        formatter = logging.Formatter(self.log_format)

        # configure console handler
        console = logging.StreamHandler()
        console.setFormatter(formatter)
        self.logger.addHandler(console)

        # configure TimeRotatingFileHandler
        log_file = f"logs/{self.name}.log"
        file = logging.handlers.TimedRotatingFileHandler(filename=log_file, when="midnight", backupCount=5)
        file.setFormatter(formatter)
        self.logger.addHandler(file)
