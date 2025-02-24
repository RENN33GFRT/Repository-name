# decorators.py
import logging
import sys
from functools import wraps


def setup_logger(filename: object = None) -> object:
    logger = logging.getLogger('FunctionLogger')
    logger.setLevel(logging.DEBUG)

    if filename:
        handler = logging.FileHandler(filename)
    else:
        handler = logging.StreamHandler(sys.stdout)

    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    return logger


def log(filename=None):
    logger = setup_logger(filename)

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            logger.info(f'Starting function: {func.__name__} with arguments: {args}, {kwargs}')
            try:
                result = func(*args, **kwargs)
                logger.info(f'Function: {func.__name__} completed successfully with result: {result}')
                return result
            except Exception as e:
                logger.error(
                    f'Function: {func.__name__} raised an error: {type(e).__name__} - {e} with arguments: {args}, {kwargs}')
                raise  # повторно выбрасываем исключение после логирования

        return wrapper

    return decorator
'эта н существует тока потому что кое-кто нитуда закамитил'