# pylogger

This is a simple logging module which helps you either log to the console for all generic modules else will help you log to a file.

# How to use
```
git clone https://github.com/mokbat/pylogger.git
```

# For console logging
```
>>> from logger import Logger
>>> log = Logger(__file__).console_logger()
>>> log.debug("This is a debug message")
>>> log.info("This is a info message")
>>> log.warning("This is a warning message")
>>> log.error("This is a error message")
>>> log.critical("This is a critical message")
```
# For file logging
```
>>> from logger import Logger
>>> log = Logger(__file__).file_logger()
>>> log.debug("This is a debug message")
>>> log.info("This is a info message")
>>> log.warning("This is a warning message")
>>> log.error("This is a error message")
>>> log.critical("This is a critical message")
```
