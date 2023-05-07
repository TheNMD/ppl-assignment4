import unittest
from TestUtils import TestCodeGen
from AST import *


class CheckCodeGenSuite(unittest.TestCase):
    # def test1(self):
    #     input = """
    #                 main : function void () { return ; }"""
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
    #                 main : function void () { return ; }"""
    #     expect = ""
    #     self.assertTrue(TestCodeGen.test(input, expect, 502))
    
    # def test3(self):
    #     input = """ a : integer = 2 ;
    #                 b : float = 3.3 ;
    #                 b1 : float = 3 ;
    #                 c : boolean = true ;
    #                 c1 : boolean = false ;
    #                 d : string = "123" ;
    #                 main : function void () { return ; }"""
    #     expect = ""
    #     self.assertTrue(TestCodeGen.test(input, expect, 503))
        
    # def test4(self):
    #     input = """ a : integer = 23 ; 
    #                 b : integer = a ; 
    #                 main : function void () { return ; }"""
    #     expect = ""
    #     self.assertTrue(TestCodeGen.test(input, expect, 504))
        
    # def test5(self):
    #     input = """a : array [2] of string ;   
    #                main : function void () { return ; } """
    #     expect = ""
    #     self.assertTrue(TestCodeGen.test(input, expect, 505))
        
    # def test6(self):
    #     input = """a : array [3, 2] of integer ;   
    #                main : function void () { return ; } """
    #     expect = ""
    #     self.assertTrue(TestCodeGen.test(input, expect, 506))

    # def test7(self):
    #     input = """a : array [3, 2, 2] of integer ;   
    #                main : function void () { return ; } """
    #     expect = ""
    #     self.assertTrue(TestCodeGen.test(input, expect, 507))
        
    # def test8(self):
    #     input = """a : array [3, 2, 2, 2] of string ;   
    #                main : function void () { return ; } """
    #     expect = ""
    #     self.assertTrue(TestCodeGen.test(input, expect, 508))
    
    # def test9(self):
    #     input = """a : array [3] of float = {1.0, 2.0, 3.0} ;   
    #                main : function void () { return ; } """
    #     expect = ""
    #     self.assertTrue(TestCodeGen.test(input, expect, 509))
        
    # def test10(self):
    #     input = """a : array [3, 2] of float = {{1.1, 2.0}, {3.0, 4.0}, {5.0, 6.0}} ;   
    #                main : function void () { return ; } """
    #     expect = ""
    #     self.assertTrue(TestCodeGen.test(input, expect, 510))
        
    # def test11(self):
    #     input = """a : array [3, 2, 2] of string = {{{"1.0", "2.0"}, {"3.0", "4.0"}}, {{"5.0", "6.0"}, {"7.0", "8.0"}}, {{"9.0", "10.0"}, {"11.0", "12.0"}}} ;   
    #                main : function void () { return ; } """
    #     expect = ""
    #     self.assertTrue(TestCodeGen.test(input, expect, 511))
        
    # def test12(self):
    #     input = """a : array [2] of integer = {1, 2} ; b : float = a[1] ;   
    #                main : function void () { return ; } """
    #     expect = ""
    #     self.assertTrue(TestCodeGen.test(input, expect, 512))
        
    # def test13(self):
    #     input = """a : array [2, 2] of boolean = {{true, false}, {false, true}} ; b : boolean = a[0, 1] ;   
    #                main : function void () { return ; } """
    #     expect = ""
    #     self.assertTrue(TestCodeGen.test(input, expect, 513))
        
    # def test14(self):
    #     input = """a : array [2, 2, 2] of string = {{{"true", "false"}, {"false", "true"}}, {{"false", "true"}, {"true", "false"}}} ; b : string = a[0, 0, 0] ;   
    #                main : function void () { return ; } """
    #     expect = ""
    #     self.assertTrue(TestCodeGen.test(input, expect, 514))
    
    # def test15(self):
    #     input = """a : integer = 1 - (4 - (2 + 3)) ;   
    #                main : function void () { return ; } """
    #     expect = ""
    #     self.assertTrue(TestCodeGen.test(input, expect, 515))
        
    # def test16(self):
    #     input = """a : float = 1.1 + 2 ;   
    #                main : function void () { return ; } """
    #     expect = ""
    #     self.assertTrue(TestCodeGen.test(input, expect, 516))
        
    # def test17(self):
    #     input = """a : float = 1 + 2.2 ;   
    #                main : function void () { return ; } """
    #     expect = ""
    #     self.assertTrue(TestCodeGen.test(input, expect, 517))
        
    # def test18(self):
    #     input = """a : float = 1 + (2.2 - 3 + 4 * 6) / 12 ;   
    #                main : function void () { return ; } """
    #     expect = ""
    #     self.assertTrue(TestCodeGen.test(input, expect, 518))
        
    # def test19(self):
    #     input = """a : float = 2.1 ;
    #                b : integer = 3 ;
    #                c : float = a - (b * a) / (a + b) ;  
    #                main : function void () { return ; } """
    #     expect = ""
    #     self.assertTrue(TestCodeGen.test(input, expect, 519))
        
    # def test20(self):
    #     input = """a : integer = 8 ;
    #                b : integer = 3 ;
    #                c : float = a % b ;  
    #                main : function void () { return ; } """
    #     expect = ""
    #     self.assertTrue(TestCodeGen.test(input, expect, 520))
        
    # def test21(self):
    #     input = """a : float = 8.3 ;
    #                b : integer = 3 ;
    #                c : float = a / b ;  
    #                main : function void () { return ; } """
    #     expect = ""
    #     self.assertTrue(TestCodeGen.test(input, expect, 521))
        
    # def test22(self):
    #     input = """a : boolean = true ;
    #                b : boolean = false ;
    #                c : boolean = (a && b || true ) && (true || b) ;
    #                main : function void () { return ; } """
    #     expect = ""
    #     self.assertTrue(TestCodeGen.test(input, expect, 522))
        
    # def test23(self):
    #     input = """a : boolean = false ;
    #                b : boolean = true ;
    #                c : boolean = (a != b) == (a == b) ;
    #                main : function void () { return ; } """
    #     expect = ""
    #     self.assertTrue(TestCodeGen.test(input, expect, 523))
        
    # def test24(self):
    #     input = """a : integer = 2 ;
    #                b : integer = 3 ;
    #                c : boolean = a != b ;
    #                main : function void () { return ; } """
    #     expect = ""
    #     self.assertTrue(TestCodeGen.test(input, expect, 524))
        
    # def test25(self):
    #     input = """a : float = 2 ;
    #                b : integer = 3 ;
    #                c : array [3, 2] of integer = {{1, 2}, {3, 4}, {5, 6}} ;
    #                d : boolean = a > c[0, 0] ;
    #                main : function void () { return ; } """
    #     expect = ""
    #     self.assertTrue(TestCodeGen.test(input, expect, 525))
        
    # def test26(self):
    #     input = """func : function void (a : integer, b : float) 
    #                 {
    #                     c : array [2, 5] of integer ;
    #                     d : array [3, 10] of float ;
    #                     return ;
    #                 }
    #                main : function void () { return ; } """
    #     expect = ""
    #     self.assertTrue(TestCodeGen.test(input, expect, 526))
    
    # def test27(self):
    #     input = """func : function void (a : integer, b : float) 
    #                 {
    #                     c : array [2, 2, 2] of string = {{{"10", "20"}, {"30", "40"}}, {{"50", "60"}, {"70", "90"}}} ;
    #                     return ;
    #                 }
    #                main : function void () { return ; } """
    #     expect = ""
    #     self.assertTrue(TestCodeGen.test(input, expect, 527))
        
    # def test28(self):
    #     input = """ func : function void (a : integer, b : float) 
    #                 {
    #                     c : array [3, 1, 2] of string = {{{"6", "5"}}, {{"4", "3"}}, {{"2", "1"}}} ;
    #                     return ;
    #                 }
    #                main : function void () { return ; } """
    #     expect = ""
    #     self.assertTrue(TestCodeGen.test(input, expect, 528))
        
    # def test29(self):
    #     input = """ func : function void (a : integer, b : float) 
    #                 {
    #                     c : array [3] of string = {"1", "2", "3"} ;
    #                     d : string = c[2] ;
    #                     return ;
    #                 }
    #                main : function void () { return ; } """
    #     expect = ""
    #     self.assertTrue(TestCodeGen.test(input, expect, 529))
    
    
    # def test30(self):
    #     input = """ func : function void (a : integer, b : float) 
    #                 {
    #                     c : array [3, 2] of string = {{"1", "2"}, {"3", "4"}, {"5", "6"}} ;
    #                     e : integer ;
    #                     d : string = c[2, 1] ;
    #                     return ;
    #                 }
    #                main : function void () { return ; } """
    #     expect = ""
    #     self.assertTrue(TestCodeGen.test(input, expect, 530))
        
    # def test31(self):
    #     input = """ x : array [2] of integer = {1, 2} ;
    #                 func : function void (a : integer, b : float) 
    #                 {   
    #                     z : array [3] of float = {1.0, 2.0, 3.0} ;
    #                     y : float = x[0] ;
    #                     return ;
    #                 }
    #                main : function void () { return ; } """
    #     expect = ""
    #     self.assertTrue(TestCodeGen.test(input, expect, 531))
        
    def test32(self):
        input = """ 
                    c : string = "true" ;
                    func : function void (a : integer, b : float) 
                    {   
                        c : boolean = false ;
                        d : boolean = true ;
                        x : string ;
                        y : string ;
                        z : string ;
                        {
                            a : integer = 2 ;
                            b : float = 3.5 ;
                            {
                                x : boolean = c ;
                                d : boolean = true ;
                            }
                        }
                        return ;
                    }
                   main : function void () { return ; } """
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 532))
        
    
    # def test26(self):
    #     input = """a : string = "abc" ;
    #                b : string = "def" ;
    #                c : string = "123" :: "abc" ;
    #                main : function void () { return ; } """
    #     expect = ""
    #     self.assertTrue(TestCodeGen.test(input, expect, 526))