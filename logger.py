# -*- coding: utf-8 -*-

"""
This module helps you perform logging in all your modules, test cases and scripts.
There are two types of logging methods, console logger and file logger.
Console logger is used for modules in python.
File logger is used for test cases in python.
"""

# File ownership in Python
__author__ = "Sundar Ramakrishnan"
__copyright__ = "Copyright 2018, The Python Project"
__credits__ = ["Vinay Sajip", "Kenneth Reitz ", "Ashwin Ramakrishnan"]
__license__ = "GPL"
__version__ = "1.0.0"
__maintainer__ = "Sundar Ramakrishnan"
__email__ = "mokbat@gmail.com"

# Standard Python Libraries
import os
import logging
from datetime import datetime

class Logger():
    """ Custom logger for your repository"""

    def __init__(self, filename, propagate=True, loglevel=20):
        """
        Descriptions -
            Constructor for Logger which initializes all variables.

        Mandatory Args -
            filename (str) : Module name

        Optional Args -
            propagate (bool) : True (default) - Propagate log level across
                               False - Don't propagate log level
            loglevel (int)   : 10 - DEBUG
                               20 - INFO (default)
                               30 - WARNING
                               40 - ERROR
                               50 - CRITICAL

        Usage -
            >>> import Logger ; log = Logger(__file__)
        """
        # Default log msg format
        self.msg_format = '%(asctime)s | %(levelname)-10s | %(module)-20s | %(lineno)-6d | %(message)s'

        # Default log date format
        self.date_format = '%b/%d/%y | %H:%M:%S'

        # Default log directory
        self.log_dir = "/var/repo/logs"

        # Create the log directory if it does not exists
        if not os.path.exists(self.log_dir):
            os.makedirs(self.log_dir)

        # Log level
        self.loglevel = loglevel

        # Enable / Disable Propagation
        self.propagate = propagate

        # Enable formatter
        self.formatter = logging.Formatter(fmt=self.msg_format, datefmt=self.date_format)

        # Define log instance
        self.log = logging.getLogger('root')

        # Filename
        self.filename = filename

        # Invoke Console Logging
        self.console_logger(self.filename)

    def console_logger(self, propagate=True):
        """
        Descriptions -
            Create a console logger which enables console logging

        Mandatory Args -
                None

        Optional Args -
            propagate (bool) : True (default) - Propagate log level across
                               False - Don't propagate log level
        Usage -
            >>> import Logger ; log = Logger(__file__).module()
        """
        # Get an individual logger for the module
        self.log = logging.getLogger(self.filename).getChild("root.console")

        # Set the logging to required level
        self.log.setLevel(self.loglevel)

        # Enable or Disable Propagation
        self.propagate = propagate

        # Assume we have no stream handlers
        found = False

        # Find if we have any instance of stream handler
        for each in list(logging.root.handlers):
            each = str(each)

            if each.split(" ")[0].split(".")[1] == "StreamHandler":
                found = True
                break

        # If not found create one
        if not found:
            console_handler = logging.StreamHandler()
            console_handler.setFormatter(self.formatter)
            self.log.root.addHandler(console_handler)

        # Fetch the name of logger
        name = name.split('.')[-1]

        return self.log

    def file_logger(self, propagate=True):
        """
        Descriptions -
            Create a file logger which enables file logging

        Mandatory Args -
            None

        Optional Args -
            propagate (bool) : True (default) - Propagate log level across
                               False - Don't propagate log level
        Usage -
            >>> import Logger ; log = Logger(__file__).testcase()
        """
        # Fetch the name of logger
        name = os.path.basename(self.filename).split('.')[-1]

        # Get a child logger from root for testcase
        self.log = logging.getLogger(self.filename).getChild("root.file")

        # Set the logging to required level
        self.log.setLevel(self.loglevel)

        # Enable or Disable Propagation
        self.propagate = propagate

        # Assume we have no file handlers
        found = False

        # Find if there is already a file logger
        for each in list(logging.root.handlers):
            each = str(each)

            if each.split(" ")[0].split(".")[1] == "FileHandler":
                found = True
                break

        # If not found create one
        if not found:
            file_suffix = datetime.now().strftime('%b_%d_%y_%H_%M_%S')
            file_handle = logging.FileHandler(self.log_dir + '/' + self.filename + '_' + file_suffix + '.log')
            file_handle.setFormatter(self.formatter)
            self.log.root.addHandler(file_handle)

        return self.log
