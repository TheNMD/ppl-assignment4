import unittest
from TestUtils import TestCodeGen
from AST import *


class CheckCodeGenSuite(unittest.TestCase):
    # def test1(self):
    #     input = """
    #                 main : function void () {}"""
    #     expect = ""
    #     self.assertTrue(TestCodeGen.test(input, expect, 501))
        
    # def test2(self):
    #     input = """
    #                 a : integer ;
    #                 b : float ;
    #                 b1 : float ;
    #                 c : boolean ;
    #                 c1 : boolean ;
    #                 d : string ;
    #                 main : function void () {}"""
    #     expect = ""
    #     self.assertTrue(TestCodeGen.test(input, expect, 502))
    
    # def test3(self):
    #     input = """ a : integer = 2 ;
    #                 b : float = 3.3 ;
    #                 b1 : float = 3 ;
    #                 c : boolean = true ;
    #                 c1 : boolean = false ;
    #                 d : string = "123" ;
    #                 main : function void () {}"""
    #     expect = ""
    #     self.assertTrue(TestCodeGen.test(input, expect, 503))
        
    # def test4(self):
    #     input = """ a : integer = 23 ; 
    #                 b : integer = a ; 
    #                 main : function void () {}"""
    #     expect = ""
    #     self.assertTrue(TestCodeGen.test(input, expect, 504))
        
    # def test5(self):
    #     input = """a : array [2] of integer ;   
    #                main : function void () {} """
    #     expect = ""
    #     self.assertTrue(TestCodeGen.test(input, expect, 505))
        
    def test6(self):
        input = """a : array [3, 2] of integer ;   
                   main : function void () {} """
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 506))
