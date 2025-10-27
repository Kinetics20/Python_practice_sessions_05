import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(levelname)-8s %(name)-10s: %(message)s')

log = logging.getLogger(__name__)

# log.debug('Debug message')
# log.info('Info message')
# log.warning('Warning message')
# log.error('Error message')
# log.critical('Critical message')

def add(x, y):
    log.info('Adding %d + %d, x, y')
    if not isinstance(x, int) or not isinstance(y, int):
        log.error('Only integers are accepted')
        raise TypeError('Only integers are accepted')
    return x + y


add(1, 2)
add(3, 4)
try:
    add(1, '2')
except TypeError as e:
    '??'

try:
    add('1', 0)
except TypeError as e:
    '??'


