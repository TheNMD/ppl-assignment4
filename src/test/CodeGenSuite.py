import unittest
from TestUtils import TestCodeGen
from AST import *


class CheckCodeGenSuite(unittest.TestCase):
    def test1(self):
        input = """a : integer ; b : float ; c : boolean ; d : string ;"""
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 501))
