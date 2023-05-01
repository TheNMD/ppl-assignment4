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
    
    # Literals
    def visitBinaryOp(self, ast, o):
        e1c, e1t = self.visit(ast.left, o)
        e2c, e2t = self.visit(ast.right, o)
        return e1c + e2c + self.emit.emitADDOP(ast.op, e1t, o.frame), e1t
    
    def visitIntegerLit(self, ast, o):
        return self.emit.emitPUSHICONST(ast.value, o.frame), IntegerType()

    # Statements
    def visitCallStmt(self, ast, o):
        ctxt = o
        frame = ctxt.frame
        nenv = ctxt.sym
        sym = next(filter(lambda x: ast.method.name == x.name, nenv), None)
        cname = sym.value.value
        ctype = sym.mtype
        in_ = ("", list())
        for x in ast.param:
            str1, typ1 = self.visit(x, Access(frame, nenv, False, True))
            in_ = (in_[0] + str1, in_[1].append(typ1))
        self.emit.printout(in_[0])
        self.emit.printout(self.emit.emitINVOKESTATIC(
            cname + "/" + ast.method.name, ctype, frame))
    
    # Declarations
    def visitVarDecl(self, ast, o):
        name = ast.name
        typ = ast.typ
        init = ast.init
        
        frame = Frame(name, typ)
        
        label = frame.getNewLabel()
        
        idx = frame.getNewIndex()
        
        res = self.emit.emitVAR(idx, name, typ, label, label, frame)
        
        self.emit.printout(res)
        
        self.emit.emitEPILOG()
        
    def visitParamDecl(self, ast, o): pass
    
    def visitFuncDecl(self, ast, o): pass

    def visitProgram(self, ast, c):
        self.emit = Emitter(self.path + "/" + "MT22Class" +  ".j")
        [self.visit(i, c)for i in ast.decls]
        return c
    
    # def visitIntegerType(self, ast, o): pass
    # def visitFloatType(self, ast, o): pass
    # def visitBooleanType(self, ast, o): pass
    # def visitStringType(self, ast, o): pass
    # def visitArrayType(self, ast, o): pass
    # def visitAutoType(self, ast, o): pass
    # def visitVoidType(self, ast, o): pass

    # def visitBinExpr(self, ast, o): pass
    # def visitUnExpr(self, ast, o): pass
    # def visitId(self, ast, o): pass
    # def visitArrayCell(self, ast, o): pass
    # def visitIntegerLit(self, ast, o): pass
    # def visitFloatLit(self, ast, o): pass
    # def visitStringLit(self, ast, o): pass
    # def visitBooleanLit(self, ast, o): pass
    # def visitArrayLit(self, ast, o): pass
    # def visitFuncCall(self, ast, o): pass

    # def visitAssignStmt(self, ast, o): pass
    # def visitBlockStmt(self, ast, o): pass
    # def visitIfStmt(self, ast, o): pass
    # def visitForStmt(self, ast, o): pass
    # def visitWhileStmt(self, ast, o): pass
    # def visitDoWhileStmt(self, ast, o): pass
    # def visitBreakStmt(self, ast, o): pass
    # def visitContinueStmt(self, ast, o): pass
    # def visitReturnStmt(self, ast, o): pass
    # def visitCallStmt(self, ast, o): pass

    # def visitVarDecl(self, ast, o): pass
    # def visitParamDecl(self, ast, o): pass
    # def visitFuncDecl(self, ast, o): pass

    # def visitProgram(self, ast, o): pass
