import unittest
from TestUtils import TestCodeGen
from AST import *


class CheckCodeGenSuite(unittest.TestCase):
    def test1(self):
        input = """
                    main : function void () {}"""
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 501))
        
    def test2(self):
        input = """
                    a : integer ;
                    b : float ;
                    b1 : float ;
                    c : boolean ;
                    c1 : boolean ;
                    d : string ;
                    main : function void () {}"""
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 502))
    
    def test3(self):
        input = """ a : integer = 2 ; 
                    main : function void () {}"""
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 503))
        
    # def test4(self):
    #     input = """ a : integer = 23 ; 
    #                 b : float = a ; 
    #                 main : function integer () {}"""
    #     expect = ""
    #     self.assertTrue(TestCodeGen.test(input, expect, 504))
        
    # def test5(self):
    #     input = """x, y : integer = 1, 2 ; 
    #                a : array [2, 2] of integer = {{x, y}, {3, 4}} ;   
    #                main : function integer () {} """
    #     expect = ""
    #     self.assertTrue(TestCodeGen.test(input, expect, 505))
