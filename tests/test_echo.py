#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import echo
import subprocess


class EchoTest(unittest.TestCase):

    def setUp(self):
        self.parser = echo.create_parser()

    def test_help(self):
        """ when running program with no args, USAGE should be displayed """
        process = subprocess.Popen(
            ["python", "./echo.py", "-h"], stdout=subprocess.PIPE
            )
        stdout, _ = process.communicate()
        usage = open("./USAGE", "r").read()
        self.assertEquals(stdout, usage)

    def test_lower(self):
        """ tests for lowercase """
        arg_list = ["-l", "HELLO"]
        result = echo.main(arg_list)
        self.assertEqual(result, "hello")

    def test_upper(self):
        """ tests for uppercase """
        arg_list = ["-u", "hello"]
        result = echo.main(arg_list)
        self.assertEqual(result, "HELLO")

    def test_title(self):
        """ tests for titlecase """
        arg_list = ["-t", "hello"]
        result = echo.main(arg_list)
        self.assertEqual(result, "Hello")

    def test_all_arg(self):
        """ tests for all """
        arg_list = ["-l", "-u", "-t", "hello"]
        result = echo.main(arg_list)
        self.assertTrue(result, "Hello")

    def test_no_arg(self):
        """ tests for none """
        process = subprocess.Popen(
            ["python", "./echo.py"], stdout=subprocess.PIPE
            )
        stdout, _ = process.communicate()
        helper_message = "usage: echo.py [-h] [-u] [-l] [-t] text\n"
        self.assertEquals(stdout, helper_message)


if __name__ == '__main__':
    unittest.main()
