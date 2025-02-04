import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)-8s - %(name)-10s: %(message)s')

log = logging.getLogger(__name__)

# log.debug('debug message')
# log.info('info message')
# log.warning('warning message')
# log.error('error message')
# log.critical('critical message')

def add(x, y):
    log.info('Adding %d + %d', x, y)
    if not isinstance(x, int) or not isinstance(y, int):
        raise TypeError('x and y must be integers')

    return x + y

add(1, 2)
add(5, 8)
try:
    add(2, '90')
except TypeError as e:
    '???'