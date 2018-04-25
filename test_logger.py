# -*- coding: utf-8 -*-

"""
This is a unittest for pylogger.
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
import unittest
from logger import Logger

class PyloggerTest(unittest.TestCase):

    def test_1_initialize_logger(self):
        self.log = Logger(__file__)
        self.assertTrue(expr=self.log)

    def test_2_initialize_console_logger(self):
        self.log = Logger(__file__).console_logger()

        self.log.debug("This is a debug message in test 1")
        self.log.info("This is a info message in test 1")
        self.log.warning("This is a warning message in test 1")
        self.log.error("This is a error message in test 1")
        self.log.critical("This is a critical message in test 1")

        # Find if we have any instance of stream handler
        for each in list(self.log.root.handlers):
            each = str(each)
            if each.split(" ")[0].split("<")[1] == "StreamHandler":
                self.assertEqual(1, 1)

    def test_3_initialize_file_logger(self):
        self.log = Logger(__file__).file_logger()

        self.log.debug("This is a debug message in test 1")
        self.log.info("This is a info message in test 1")
        self.log.warning("This is a warning message in test 1")
        self.log.error("This is a error message in test 1")
        self.log.critical("This is a critical message in test 1")

        # Find if we have any instance of stream handler
        for each in list(self.log.root.handlers):
            each = str(each)
            if each.split(" ")[0].split("<")[1] == "FileHandler":
                self.assertEqual(1, 1)

    def test_4_check_file_logger(self):
        self.log = Logger(__file__).file_logger()

        self.log.debug("This is a debug message in test 1")
        self.log.info("This is a info message in test 1")
        self.log.warning("This is a warning message in test 1")
        self.log.error("This is a error message in test 1")
        self.log.critical("This is a critical message in test 1")

        # Find if we have any instance of stream handler
        for each in list(self.log.root.handlers):
            each = str(each)
            if each.split(" ")[0].split("<")[1] == "FileHandler":
                self.assertTrue(self.log.file_handle)


if __name__ == "__main__":
    unittest.main()
