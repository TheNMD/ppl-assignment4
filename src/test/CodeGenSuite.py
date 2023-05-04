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
                    b : float = 3.3 ;
                    b1 : float = 3 ;
                    c : boolean = true ;
                    c1 : boolean = false ;
                    d : string = "123" ;
                    main : function void () {}"""
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 503))
        
    def test4(self):
        input = """ a : integer = 23 ; 
                    b : integer = a ; 
                    main : function void () {}"""
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 504))
        
    def test5(self):
        input = """a : array [2] of string ;   
                   main : function void () {} """
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 505))
        
    def test6(self):
        input = """a : array [3, 2] of integer ;   
                   main : function void () {} """
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 506))

    def test7(self):
        input = """a : array [3, 2, 2] of integer ;   
                   main : function void () {} """
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 507))
        
    def test8(self):
        input = """a : array [3, 2, 2, 2] of string ;   
                   main : function void () {} """
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 508))
    
    def test9(self):
        input = """a : array [3] of float = {1.0, 2.0, 3.0} ;   
                   main : function void () {} """
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 509))
        
    def test10(self):
        input = """a : array [3, 2] of float = {{1.1, 2.0}, {3.0, 4.0}, {5.0, 6.0}} ;   
                   main : function void () {} """
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 510))
        
    def test11(self):
        input = """a : array [3, 2, 2] of string = {{{"1.0", "2.0"}, {"3.0", "4.0"}}, {{"5.0", "6.0"}, {"7.0", "8.0"}}, {{"9.0", "10.0"}, {"11.0", "12.0"}}} ;   
                   main : function void () {} """
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 511))