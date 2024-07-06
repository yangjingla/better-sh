import os
import sys
from loguru import logger


# logger.add("logs/{time}.log")

logger_fmt = "[{time}]-[{level}]-[{thread}]-[{process}] | [{elapsed}]- [{function}:{module}:{line}]|\n>{message}"
logger.add(sys.stdout, format=logger_fmt)


@logger.catch
def func(x, y):
    return x / y


def filter_rule(record):
    """
    如果返回False那么就不会记录
    """

    return "1" in record["message"]


# logger.add("log_{time}.log", filter=filter_rule)


def main():

    fmt = "hello [pid/ppid]={}/{}".format(os.getpid(), os.getppid())

    logger.info(fmt)


if __name__ == "__main__":
    main()
