# Logging

# import logging
# logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
import logging
logging.basicConfig(filename='myProgramLog.txt', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
# logging.disable(logging.CRITICAL)
# Log Levels debug(lowest), info, warning, error, critical(highest)

logging.debug('Start of program')


def factorial(n):
    logging.debug('Start of factorial(%s)' % (n))
    total = 1
    for i in range(1, n+1):
        total *= i
        logging.debug('i is %s, total is %s' % (i,total))
    logging.debug('Return value is %s' % (total))
    return total

print(factorial(5))


logging.debug('End of Program')
# each debug function is like a print function



# 2021-04-12 14:46:57,194 - DEBUG - Start of program
# 2021-04-12 14:46:57,238 - DEBUG - Start of factorial(5)
# 2021-04-12 14:46:57,253 - DEBUG - i is 0, total is 0
# 2021-04-12 14:46:57,269 - DEBUG - i is 1, total is 0
# 2021-04-12 14:46:57,285 - DEBUG - i is 2, total is 0
# 2021-04-12 14:46:57,302 - DEBUG - i is 3, total is 0
# 2021-04-12 14:46:57,319 - DEBUG - i is 4, total is 0
# 2021-04-12 14:46:57,335 - DEBUG - i is 5, total is 0
# 2021-04-12 14:46:57,352 - DEBUG - Return value is 0
# 0
# 2021-04-12 14:46:57,402 - DEBUG - End of Program


# the logging mod lets you display logging messages
# log messages create a breadcrumb trail of what your program is doing
# after calling basicConfig() to set up logging, calling logging.debug() to create a log message
# when done, you can disable the log messages with logging.disable(logging.CRITICAL)
# dont use print() for log messages: it's hard to remove them all when you're done debugging
# the five log levels are DEBUG, INFO, WARNING, ERROR, and CRITICAL
# you can also log to a file instead of on the screen with the 'filename' keyword argument to the basicConfig() function./
