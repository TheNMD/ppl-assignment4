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
    
    # TODO
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
    def visitBinExpr(self, ast, o): pass
    
    def visitUnExpr(self, ast, o): pass
    
    def visitId(self, ast, o):
        sym = o.sym
        for ele in sym:
            if ele.name == ast.name:
                return (ele.name, ele.mtype, ele.value)
    
    def visitArrayCell(self, ast, o): pass
    
    def visitIntegerLit(self, ast, o):
        return (ast.val, IntegerType(), -1)
        
    def visitFloatLit(self, ast, o):
        return (str(ast.val), FloatType(), -1)
    
    def visitBooleanLit(self, ast, o):
        return (str(ast.val), BooleanType(), -1)
    
    def visitStringLit(self, ast, o):
        return (str(ast.val), StringType(), -1)
    
    def visitArrayLit(self, ast, o): pass
    
    def visitFuncCall(self, ast, o): pass
    

    # Statements
    def visitAssignStmt(self, ast, o):
        frame = o.frame
        lhs = ast.lhs
        rhs = ast.rhs
        # (value or name, type, index)
        left = self.visit(ast.lhs, o)
        right = self.visit(ast.rhs, o)
        
        if type(lhs) == Id:
            if type(rhs) == BinExpr:
                pass
            elif type(rhs) == UnExpr:
                pass
            elif type(rhs) == Id:
                pass
            elif type(rhs) == ArrayCell:
                pass
            elif type(rhs) == IntegerLit:
                self.emit.printout(self.emit.emitPUSHICONST(right[0], frame))
                if (type(left[1]) == FloatType):
                    self.emit.printout(self.emit.emitI2F(frame))
                self.emit.printout(self.emit.emitWRITEVAR(left[0], left[1], left[2], frame))
            elif type(rhs) == FloatLit:
                self.emit.printout(self.emit.emitPUSHFCONST(right[0], o.frame))
                self.emit.printout(self.emit.emitWRITEVAR(left[0], left[1], left[2], frame))
            elif type(rhs) == BooleanLit:
                self.emit.printout(self.emit.emitPUSHICONST(right[0], frame))
                self.emit.printout(self.emit.emitWRITEVAR(left[0], left[1], left[2], frame))
            elif type(rhs) == StringLit:   
                self.emit.printout(self.emit.emitPUSHICONST(right[0], frame))
                self.emit.printout(self.emit.emitWRITEVAR(left[0], left[1], left[2], frame))
            elif type(rhs) == ArrayLit:
                pass
            elif type(rhs) == FuncCall:
                pass
        elif type(lhs) == ArrayCell:
            pass
        
    
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
    def visitVarDecl(self, ast, o):
        name = ast.name
        typ = ast.typ
        frame = o.frame
        
        idx = frame.getNewIndex()
        start_label = frame.getStartLabel()
        end_label = frame.getEndLabel()
        
        self.emit.printout(self.emit.emitVAR(idx, name, typ, start_label, end_label, frame))
        
        return Symbol(name, typ, idx)
        
    def visitParamDecl(self, ast, o): pass
    
    def visitFuncDecl(self, ast, o): pass

    # Program
    def visitProgram(self, ast, o):
        frame = Frame("global_frame", None)
        self.emit = Emitter(self.path + "/" + "MT22Class" +  ".j")
        
        self.emit.printout(self.emit.emitPROLOG("MT22Class", "java.lang.Object"))
        
        self.emit.printout(self.emit.emitMETHOD("main", MType([ArrayType(0, StringType())], VoidType()), True, frame))
        
        frame.enterScope(True)
        
        global_evn = SubBody(frame, [])
        for decl in ast.decls:
            global_evn.sym += [self.visit(decl, global_evn)]
        
        self.emit.printout(self.emit.emitLABEL(frame.getStartLabel(), frame))
        
        for decl in ast.decls:
            if type(decl) == VarDecl and decl.init:
                self.visit(AssignStmt(Id(decl.name), decl.init), global_evn)
        
        self.emit.printout(self.emit.emitLABEL(frame.getEndLabel(), frame))
        
        self.emit.printout(self.emit.emitRETURN(VoidType(), frame))
        
        self.emit.printout(self.emit.emitENDMETHOD(frame))
        
        frame.exitScope()
            
        self.emit.emitEPILOG()
