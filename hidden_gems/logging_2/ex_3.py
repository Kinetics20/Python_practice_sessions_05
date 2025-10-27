import logging.config
import logging
import os
import tomllib

with open(os.path.join('..', '..', 'logging.toml'), mode='rb') as f:
    config = tomllib.load(f)

logging.config.dictConfig(config)

logger = logging.getLogger('my_logger')

logger.info('hello world')
logger.debug('hello world')
logger.error('hello world')