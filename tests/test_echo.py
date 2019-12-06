#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import echo
import subprocess


# Your test case class goes here
class TestEcho(unittest.TestCase):

    def test_help(self):
        """ Running the program without arguments should show usage. """

        # Run the command `python ./echo.py -h` in a separate process, then
        # collect it's output.
        process = subprocess.Popen(
            ["python", "./echo.py", "-h"],
            stdout=subprocess.PIPE)
        stdout, _ = process.communicate()
        usage = open("./USAGE", "r").read()

        self.assertEquals(stdout, usage)

    def test_upper(self):
        result = echo.main(['-u', 'hello'])
        self.assertEquals('HELLO', result)

    def test_lower(self):
        result = echo.main(['-l', 'HELLO'])
        self.assertEquals('hello', result)

    def test_title(self):
        result = echo.main(['-t', 'hello'])
        self.assertEquals('Hello', result)

    def test_options(self):
        result = echo.main(['-tul', 'heLLo'])
        self.assertEquals('Hello', result)

    def test_text(self):
        result = echo.main(['hello'])
        self.assertEquals('hello', result)


if __name__ == '__main__':
    unittest.main()
