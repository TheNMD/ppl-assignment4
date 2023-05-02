import unittest
from TestUtils import TestCodeGen
from AST import *


class CheckCodeGenSuite(unittest.TestCase):
    def test1(self):
        input = """a : integer = 32768 ; 
                   b : float = 13.2 ; 
                   b1 : float = 13 ;
                   c : boolean = true ; 
                   c1 : boolean = false ;
                   d : string = "abc" ;"""
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 501))
