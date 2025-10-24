from datetime import datetime


class Singleton:
    _instances = {}

    def __new__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__new__(cls)
            cls._instances[cls] = instance
        return cls._instances[cls]

class Logger(Singleton):
    log_file = None

    def __init__(self, path='_data.log'):
        if self.log_file is None:
            self.log_file = open(path, mode='w')

    def write_log(self, log_record):
        now = str(datetime.now())
        record = f'{now}: {log_record}\n'
        self.log_file.write(record)

    def close_log(self):
        self.log_file.close()
        self.log_file = None

l1 = Logger()
l2 = Logger('/usr/bin/')

l1.write_log('STH')
l1.write_log('STH_2')
l2.write_log('Home')
l2.write_log('Home_2')
l1.write_log('Mike')

l2.close_log()