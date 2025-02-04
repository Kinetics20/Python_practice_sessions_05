import logging

console_handler = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s - %(levelname)-8s - %(name)-10s: %(message)s')
console_handler.setFormatter(formatter)

log = logging.getLogger(__name__)
log.setLevel(logging.DEBUG)
log.addHandler(console_handler)

log.debug('debug message')
log.info('info message')
log.warning('warning message')
log.error('error message')
log.critical('critical message')