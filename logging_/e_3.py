import logging.config
import os
import tomllib

with open(os.path.join('..', 'logging.toml'), mode='rb') as f:
    config = tomllib.load(f)

logging.config.dictConfig(config)

logger = logging.getLogger('my_logger')
logger.info('Hello, world!')
logger.debug('Hello, world!')
logger.error('Hello, world!')
