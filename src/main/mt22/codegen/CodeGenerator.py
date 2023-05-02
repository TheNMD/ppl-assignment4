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

    ############################################################################################

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
    
    def visitId(self, ast, o): pass
    
    def visitArrayCell(self, ast, o): pass
    
    def visitIntegerLit(self, ast, o):
        return self.emit.emitPUSHICONST(ast.value, o.frame), IntegerType()
    
    def visitFloatLit(self, ast, o): pass
    
    def visitStringLit(self, ast, o): pass
    
    def visitBooleanLit(self, ast, o): pass
    
    def visitArrayLit(self, ast, o): pass
    
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
    def visitVarDecl(self, ast, o):
        name = ast.name
        typ = ast.typ
        init = ast.init
        frame = self.frame
        
        idx = frame.getNewIndex()
        start_label = frame.getStartLabel()
        end_label = frame.getEndLabel()
        
        self.emit.printout(self.emit.emitVAR(idx, name, typ, start_label, end_label, frame))
        
    def visitParamDecl(self, ast, o): pass
    
    def visitFuncDecl(self, ast, o): pass

    def visitProgram(self, ast, o):
        self.frame = Frame("global", None)

        self.emit = Emitter(self.path + "/" + "MT22Class" +  ".j")
        
        self.emit.printout(self.emit.emitPROLOG("MT22Class", "java.lang.Object"))
        
        self.emit.printout(self.emit.emitMETHOD("main", MType([ArrayType(0, StringType())], VoidType()), True, self.frame))
        
        self.frame.enterScope(True)

        self.emit.printout(self.emit.emitLABEL(self.frame.getStartLabel(), self.frame))
        
        for decl in ast.decls:
            self.visit(decl, o)
        
        self.emit.printout(self.emit.emitLABEL(self.frame.getEndLabel(), self.frame))
        self.emit.printout(self.emit.emitRETURN(VoidType(), self.frame))
        self.emit.printout(self.emit.emitENDMETHOD(self.frame))
        
        self.frame.exitScope()
            
        self.emit.emitEPILOG()
