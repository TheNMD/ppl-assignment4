from Emitter import Emitter
from functools import reduce

from Frame import Frame
from abc import ABC

from Visitor import *
from AST import *


class MType:
    def __init__(self, partype, rettype):
        self.partype = partype
        self.rettype = rettype


class Symbol:
    def __init__(self, name, mtype, value=None):
        self.name = name
        self.mtype = mtype
        self.value = value

    def __str__(self):
        return "Symbol(" + self.name + "," + str(self.mtype) + ")"


class CodeGenerator:
    def __init__(self):
        self.libName = "io"
    
    # TODO super va preventDefault
    def init(self):
        return [Symbol("readInteger", MType(list(), IntegerType()), CName(self.libName)),
                Symbol("printInteger", MType([IntegerType()], VoidType()), CName(self.libName)),
                Symbol("readFloat", MType(list(), FloatType()), CName(self.libName)),
                Symbol("writeFloat", MType([FloatType()], VoidType()), CName(self.libName)),
                Symbol("readBoolean", MType(list(), BooleanType()), CName(self.libName)),
                Symbol("printBoolean", MType([BooleanType()], VoidType()), CName(self.libName)),
                Symbol("readString", MType(list(), StringType()), CName(self.libName)),
                Symbol("printString", MType([StringType()], VoidType()), CName(self.libName))]

    def gen(self, ast, path):
        # ast: AST
        # dir_: String

        gl = self.init()
        gc = CodeGenVisitor(ast, gl, path)
        gc.visit(ast, None)


class SubBody():
    def __init__(self, frame, sym):
        self.frame = frame
        self.sym = sym


class Access():
    def __init__(self, frame, sym, isLeft, isFirst=False):
        self.frame = frame
        self.sym = sym
        self.isLeft = isLeft
        self.isFirst = isFirst


class Val(ABC):
    pass


class Index(Val):
    def __init__(self, value):
        self.value = value


class CName(Val):
    def __init__(self, value):
        self.value = value


class CodeGenVisitor(Visitor):
    def __init__(self, ast, env, path):
        self.ast = ast
        self.env = env
        self.path = path
    
    # Types
    def visitIntegerType(self, ast, o): pass
    
    def visitFloatType(self, ast, o): pass
    
    def visitBooleanType(self, ast, o): pass
    
    def visitStringType(self, ast, o): pass
    
    def visitArrayType(self, ast, o): pass
    
    def visitAutoType(self, ast, o): pass
    
    def visitVoidType(self, ast, o): pass
    
    # Literals
    def visitBinExpr(self, ast, o):
        op = str(ast.op)
        left = ast.left
        right = ast.right
        frame = o.frame
        
        leftValue, leftType = self.visit(left, o)
        rightValue, rightType = self.visit(right, o)
        
        if type(leftType) == FloatType and type(rightType) == IntegerType:
            typ = FloatType()
            self.emit.printout(self.emit.emitI2F(frame))
        elif type(leftType) == IntegerType and type(rightType) == FloatType:
            typ = FloatType()
            self.emit.printout(self.emit.emitPOP(frame))
            self.emit.printout(self.emit.emitI2F(frame))
            self.visit(right, o)
        elif op == "/":
            typ = FloatType()
            if type(leftType) == IntegerType:
                self.emit.printout(self.emit.emitPOP(frame))
                self.emit.printout(self.emit.emitI2F(frame))
                self.visit(right, o)
            if type(rightType) == IntegerType:
                self.emit.printout(self.emit.emitI2F(frame))
        else:
            typ = leftType
            
        if op == "+" or op == "-":
            return self.emit.printout(self.emit.emitADDOP(op, typ, frame)), typ
        elif op == "*" or op == "/":
            return self.emit.printout(self.emit.emitMULOP(op, typ, frame)), typ
        elif op == "%":
            return self.emit.printout(self.emit.emitMOD(frame)), typ
        elif op == "&&":
            return self.emit.printout(self.emit.emitANDOP(frame)), typ
        elif op == "||":
            return self.emit.printout(self.emit.emitOROP(frame)), typ
        elif op == "==" or op == "!=" or op == "<" or op == ">" or op == "<=" or op == ">=":
            return self.emit.printout(self.emit.emitREOP(op, typ, frame)), typ
        elif op == "::":
            pass
    
    def visitUnExpr(self, ast, o): pass
    
    def visitId(self, ast, o):
        name = ast.name
        frame = o.frame
        sym = o.sym
        
        for i in range(len(sym)):
            for j in range(len(sym[i])):
                if i == 0:
                    if sym[i][j].name == name:
                        self.emit.printout(self.emit.emitGETSTATIC(f"MT22Class/{sym[i][j].name}", sym[i][j].typ, frame))
                        return sym[i][j].name, sym[i][j].typ
                else: 
                    pass
                    # TODO khi o trong function
                    # if sym[i][j].name == name:
                    #     self.emit.printout(self.emit.emitREADVAR(sym[i][j].name, sym[i][j].typ, frame.getNewIndex(), frame))
                    #     return sym[i][j].name, sym[i][j].typ
    
    def visitArrayCell(self, ast, o):
        name = ast.name
        cell = ast.cell
        frame = o.frame
        sym = o.sym
        
        for i in range(len(sym)):
            for j in range(len(sym[i])):
                if i == 0:
                    if sym[i][j].name == name:
                        self.emit.printout(self.emit.emitGETSTATIC(f"MT22Class/{sym[i][j].name}", sym[i][j].typ, frame))
                        for k in range(len(cell)):
                            cellValue, cellType = self.visit(cell[k], o)
                            # TODO So sanh xem cellValue co phai la integer va co vuot upper bound hay lower bound ko
                            if k == len(cell) - 1:
                                self.emit.printout(self.emit.emitALOAD(sym[i][j].typ.typ, frame))
                            else:
                                self.emit.printout(self.emit.emitALOAD(sym[i][j].typ, frame))
                        return sym[i][j].name, sym[i][j].typ.typ
                else: 
                    pass
                    # TODO khi o trong function
    
    def visitIntegerLit(self, ast, o):
        frame = o.frame
        self.emit.printout(self.emit.emitPUSHICONST(ast.val, frame))
        return ast.val, IntegerType()
        
    def visitFloatLit(self, ast, o):
        frame = o.frame
        self.emit.printout(self.emit.emitPUSHFCONST(str(ast.val), frame))
        return str(ast.val), FloatType()
    
    def visitBooleanLit(self, ast, o):
        frame = o.frame
        self.emit.printout(self.emit.emitPUSHICONST(str(ast.val), frame))
        return str(ast.val), BooleanType()
    
    def visitStringLit(self, ast, o):
        frame = o.frame
        self.emit.printout(self.emit.emitPUSHICONST(str(ast.val), frame))
        return str(ast.val), StringType()
    
    def visitArrayLit(self, ast, o):
        explist = ast.explist
        temp = []
        for exp in explist:
            if type(exp) == ArrayLit:
                temp += self.visit(exp, o)
            else:
                temp += [exp]
        return temp
        
    def visitFuncCall(self, ast, o): pass

    # Statements
    def visitAssignStmt(self, ast, o): pass
        
    def visitBlockStmt(self, ast, o): pass
    
    def visitIfStmt(self, ast, o): pass
    
    def visitForStmt(self, ast, o): pass
    
    def visitWhileStmt(self, ast, o): pass
    
    def visitDoWhileStmt(self, ast, o): pass
    
    def visitBreakStmt(self, ast, o): pass
    
    def visitContinueStmt(self, ast, o): pass
    
    def visitReturnStmt(self, ast, o): pass
    
    def visitCallStmt(self, ast, o): pass
    
    # Declarations
    def visitVarDecl(self, ast, o): pass # TODO emitVAR khi visit local variable trong function

    def visitParamDecl(self, ast, o): pass
    
    def visitFuncDecl(self, ast, o):
        name = ast.name
        return_type = ast.return_type
        params = ast.params
        inherit = ast.inherit
        body = ast.body
        frame =  Frame(name, return_type)
        
        if name == "main" and type(return_type) == VoidType and len(params) == 0:
            self.emit.printout(self.emit.emitMETHOD("main", MType([ArrayType(0, StringType())], VoidType()), True, frame))
            frame.enterScope(True)
            self.emit.printout(self.emit.emitVAR(frame.getNewIndex(), "args", ArrayType(0, StringType()), frame.getStartLabel(), frame.getEndLabel(), frame))
            self.emit.printout(self.emit.emitLABEL(frame.getStartLabel(), frame))
            self.emit.printout(self.emit.emitLABEL(frame.getEndLabel(), frame))
            self.emit.printout(self.emit.emitRETURN(VoidType(), frame))
            self.emit.printout(self.emit.emitENDMETHOD(frame))
            frame.exitScope()

    # Program
    def visitProgram(self, ast, o):
        def arrayTraversalBare(name, typ, dim, frame):
            if len(dim) == 1:
                for i in range(int(dim[0])):
                    self.emit.printout(self.emit.emitDUP(frame))
                    
                    self.emit.printout(self.emit.emitPUSHICONST(i, frame))
                    self.emit.printout(self.emit.emitPUSHICONST(int(dim[0]), frame))
                    self.emit.printout(self.emit.emitANEWARRAY(typ, len(dim)))
                    self.emit.printout(self.emit.emitASTORE(typ, frame))
                    
                    if i == int(dim[0]) - 1:
                        self.emit.printout(self.emit.emitPOP(frame))
            else:
                for i in range(int(dim[0])):
                    self.emit.printout(self.emit.emitDUP(frame))

                    self.emit.printout(self.emit.emitPUSHICONST(i, frame))
                    self.emit.printout(self.emit.emitPUSHICONST(int(dim[0]), frame))
                    self.emit.printout(self.emit.emitANEWARRAY(typ, len(dim)))
                    self.emit.printout(self.emit.emitASTORE(typ, frame))

                    self.emit.printout(self.emit.emitDUP(frame))
                    self.emit.printout(self.emit.emitPUSHICONST(i, frame))
                    self.emit.printout(self.emit.emitALOAD(typ, frame))
                    arrayTraversalBare(name, typ, dim[1:], frame)
                    
                    if i == int(dim[0]) - 1:
                        self.emit.printout(self.emit.emitPOP(frame))
        
        def arrayTraversalInit(name, typ, dim, frame, init):
            if len(dim) == 1:
                for i in range(int(dim[0])):
                    self.emit.printout(self.emit.emitDUP(frame))
                    
                    self.emit.printout(self.emit.emitPUSHICONST(i, frame))
                    eleValue, eleType = self.visit(init[0], evnList_clinit)
                    self.emit.printout(self.emit.emitASTORE(eleType, frame))
                    
                    init.pop(0) 
                    if i == int(dim[0]) - 1:
                        self.emit.printout(self.emit.emitPOP(frame))
            else:
                for i in range(int(dim[0])):
                    self.emit.printout(self.emit.emitDUP(frame))
                    
                    self.emit.printout(self.emit.emitPUSHICONST(i, frame))
                    self.emit.printout(self.emit.emitALOAD(typ, frame))
                    arrayTraversalInit(name, typ, dim[1:], frame, init)
                    
                    if i == int(dim[0]) - 1:
                        self.emit.printout(self.emit.emitPOP(frame))
        # Emitter
        self.emit = Emitter(self.path + "/" + "MT22Class" +  ".j")
         
        # Frame
        frame_clinit = Frame("<clinit>", VoidType)
        frame_init = Frame("<init>", VoidType())
        frame_func = Frame("func", VoidType)
        
        # Environment list
        ## evnList in global : [[global_env]]
        ## evnList in function : [[global_env], [local_env1], [local_env2], ...]
        evnList_clinit = SubBody(frame_clinit, [[decl for decl in ast.decls]])
        # evnList_init = SubBody(frame_init, [])
        evnList_func = SubBody(frame_func, [[decl for decl in ast.decls]])
        
        
        # Class declaration
        self.emit.printout(self.emit.emitPROLOG("MT22Class", "java.lang.Object"))
        
        # Static field (Global variables)
        for decl in ast.decls:
            if type(decl) == VarDecl:
                self.emit.printout(self.emit.emitSTATICFIELD(decl.name, decl.typ, False))
        
        # Static initializer
        self.emit.printout(self.emit.emitMETHOD("<clinit>", MType([], VoidType()), False, frame_clinit))
        frame_clinit.enterScope(True)
        self.emit.printout(self.emit.emitLABEL(frame_clinit.getStartLabel(), frame_clinit))
        ## Initializing all global variables
        for decl in ast.decls:
            if type(decl) == VarDecl:
                if decl.init:
                    if type(decl.typ) != ArrayType:
                        initValue, initType = self.visit(decl.init, evnList_clinit)
                        if type(decl.typ) == FloatType and type(initType) == IntegerType:
                            self.emit.printout(self.emit.emitI2F(frame_clinit))
                        self.emit.printout(self.emit.emitPUTSTATIC(f"MT22Class/{decl.name}", decl.typ, frame_clinit))
                    else:
                        initValue = self.visit(decl.init, evnList_clinit)
                        if len(decl.typ.dimensions) == 1:
                            self.emit.printout(self.emit.emitPUSHICONST(int(decl.typ.dimensions[0]), frame_clinit))
                            self.emit.printout(self.emit.emitANEWARRAY(decl.typ, len(decl.typ.dimensions)))
                            self.emit.printout(self.emit.emitPUTSTATIC(f"MT22Class/{decl.name}", decl.typ, frame_clinit))
                            
                            for i in range(int(decl.typ.dimensions[0])):
                                self.emit.printout(self.emit.emitGETSTATIC(f"MT22Class/{decl.name}", decl.typ, frame_clinit))
                                self.emit.printout(self.emit.emitPUSHICONST(i, frame_clinit))
                                eleValue, eleType = self.visit(initValue[i], evnList_clinit)
                                self.emit.printout(self.emit.emitASTORE(eleType, frame_clinit))
                        else:
                            self.emit.printout(self.emit.emitPUSHICONST(int(decl.typ.dimensions[0]), frame_clinit))
                            self.emit.printout(self.emit.emitANEWARRAY(decl.typ, len(decl.typ.dimensions)))
                            self.emit.printout(self.emit.emitPUTSTATIC(f"MT22Class/{decl.name}", decl.typ, frame_clinit))
                            for i in range(int(decl.typ.dimensions[0])):
                                self.emit.printout(self.emit.emitGETSTATIC(f"MT22Class/{decl.name}", decl.typ, frame_clinit))
                                self.emit.printout(self.emit.emitPUSHICONST(i, frame_clinit))
                                self.emit.printout(self.emit.emitPUSHICONST(int(decl.typ.dimensions[0]), frame_clinit))
                                self.emit.printout(self.emit.emitANEWARRAY(decl.typ, len(decl.typ.dimensions) - 1))
                                self.emit.printout(self.emit.emitASTORE(decl.typ, frame_clinit))

                                if len(decl.typ.dimensions) > 2:
                                    self.emit.printout(self.emit.emitGETSTATIC(f"MT22Class/{decl.name}", decl.typ, frame_clinit))
                                    self.emit.printout(self.emit.emitPUSHICONST(i, frame_clinit))
                                    self.emit.printout(self.emit.emitALOAD(decl.typ, frame_clinit))
                                    arrayTraversalBare(decl.name, decl.typ, decl.typ.dimensions[2:], frame_clinit)
                            
                            for i in range(int(decl.typ.dimensions[0])):
                                self.emit.printout(self.emit.emitGETSTATIC(f"MT22Class/{decl.name}", decl.typ, frame_clinit))
                                self.emit.printout(self.emit.emitPUSHICONST(i, frame_clinit))
                                self.emit.printout(self.emit.emitALOAD(decl.typ, frame_clinit))
                                arrayTraversalInit(decl.name, decl.typ, decl.typ.dimensions[1:], frame_clinit, initValue)
                else:
                    if type(decl.typ) == IntegerType:
                        initValue, initType = self.visit(IntegerLit(0), evnList_clinit)
                        self.emit.printout(self.emit.emitPUTSTATIC(f"MT22Class/{decl.name}", decl.typ, frame_clinit))
                    elif type(decl.typ) == FloatType:
                        initValue, initType = self.visit(FloatLit(0.0), evnList_clinit)
                        self.emit.printout(self.emit.emitPUTSTATIC(f"MT22Class/{decl.name}", decl.typ, frame_clinit))
                    elif type(decl.typ) == BooleanType:
                        initValue, initType = self.visit(BooleanLit(False), evnList_clinit)
                        self.emit.printout(self.emit.emitPUTSTATIC(f"MT22Class/{decl.name}", decl.typ, frame_clinit))
                    elif type(decl.typ) == StringType:
                        initValue, initType = self.visit(StringLit(""), evnList_clinit)
                        self.emit.printout(self.emit.emitPUTSTATIC(f"MT22Class/{decl.name}", decl.typ, frame_clinit))
                    elif type(decl.typ) == ArrayType:
                        if len(decl.typ.dimensions) == 1:
                            self.emit.printout(self.emit.emitPUSHICONST(int(decl.typ.dimensions[0]), frame_clinit))
                            self.emit.printout(self.emit.emitANEWARRAY(decl.typ, len(decl.typ.dimensions)))
                            self.emit.printout(self.emit.emitPUTSTATIC(f"MT22Class/{decl.name}", decl.typ, frame_clinit))
                        else:
                            self.emit.printout(self.emit.emitPUSHICONST(int(decl.typ.dimensions[0]), frame_clinit))
                            self.emit.printout(self.emit.emitANEWARRAY(decl.typ, len(decl.typ.dimensions)))
                            self.emit.printout(self.emit.emitPUTSTATIC(f"MT22Class/{decl.name}", decl.typ, frame_clinit))
                            for i in range(int(decl.typ.dimensions[0])):
                                self.emit.printout(self.emit.emitGETSTATIC(f"MT22Class/{decl.name}", decl.typ, frame_clinit))
                                self.emit.printout(self.emit.emitPUSHICONST(i, frame_clinit))
                                self.emit.printout(self.emit.emitPUSHICONST(int(decl.typ.dimensions[0]), frame_clinit))
                                self.emit.printout(self.emit.emitANEWARRAY(decl.typ, len(decl.typ.dimensions) - 1))
                                self.emit.printout(self.emit.emitASTORE(decl.typ, frame_clinit))

                                if len(decl.typ.dimensions) > 2:
                                    self.emit.printout(self.emit.emitGETSTATIC(f"MT22Class/{decl.name}", decl.typ, frame_clinit))
                                    self.emit.printout(self.emit.emitPUSHICONST(i, frame_clinit))
                                    self.emit.printout(self.emit.emitALOAD(decl.typ, frame_clinit))
                                    arrayTraversalBare(decl.name, decl.typ, decl.typ.dimensions[2:], frame_clinit)
        ## Done initializing                         
        self.emit.printout(self.emit.emitLABEL(frame_clinit.getEndLabel(), frame_clinit))
        self.emit.printout(self.emit.emitRETURN(VoidType(), frame_clinit))
        self.emit.printout(self.emit.emitENDMETHOD(frame_clinit))
        frame_clinit.exitScope()
        
        # Default constructor
        self.emit.printout(self.emit.emitMETHOD("<init>", MType([], VoidType()), False, frame_init))
        frame_init.enterScope(True)
        self.emit.printout(self.emit.emitVAR(frame_init.getNewIndex(), "this", "LMT22Class;", frame_init.getStartLabel(), frame_init.getEndLabel(), frame_init))
        self.emit.printout(self.emit.emitLABEL(frame_init.getStartLabel(), frame_init))
        self.emit.printout(self.emit.emitREADVAR("this", "LMT22Class;", 0, frame_init))
        self.emit.printout(self.emit.emitINVOKESPECIAL(frame_init))
        self.emit.printout(self.emit.emitLABEL(frame_init.getEndLabel(), frame_init))
        self.emit.printout(self.emit.emitRETURN(VoidType(), frame_init))
        self.emit.printout(self.emit.emitENDMETHOD(frame_init))
        frame_init.exitScope()
        
        # Other functions, including main
        for decl in ast.decls:
            if type(decl) == FuncDecl:
                self.visit(decl, evnList_func)

        # Generate .j file
        self.emit.emitEPILOG()
