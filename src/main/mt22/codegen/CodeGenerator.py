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
        
        # TODO Viet lai ham search
        for ele in sym:
            if ele.name == ast.name:
                return (ele.name, ele.mtype, ele.value)
    
    def visitArrayCell(self, ast, o): pass
    
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
        res = []
        for exp in explist:
            res += [self.visit(exp, o)]
        return res 
            
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
        # init = ast.init
        
        # sym = o.sym
        frame = o.frame
        
        idx = frame.getNewIndex()
        # start_label = frame.getStartLabel()
        # end_label = frame.getEndLabel()
        # self.emit.printout(self.emit.emitVAR(idx, name, typ, start_label, end_label, frame))
        return Symbol(name, typ, idx)
        
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
            
        return 0

    # Program
    def visitProgram(self, ast, o):
        frame_clinit = Frame("<clinit>", VoidType)
        frame_init = Frame("<init>", VoidType())
        frame_func = Frame("func", VoidType)
        
        evnList_clinit = SubBody(frame_clinit, [])
        evnList_init = SubBody(frame_init, [])
        # evnList in global = [[global_env]]
        # evnList in function = [[global_env], [local_env1], [local_env2], ...]
        evnList_func = SubBody(frame_func, [[decl for decl in ast.decls]])
        
        self.emit = Emitter(self.path + "/" + "MT22Class" +  ".j")
        
        self.emit.printout(self.emit.emitPROLOG("MT22Class", "java.lang.Object"))
        
        # Static field (Global variables)
        for decl in ast.decls:
            if type(decl) == VarDecl:
                self.emit.printout(self.emit.emitSTATICFIELD(decl.name, decl.typ, False))
        
        # Static initializer
        self.emit.printout(self.emit.emitMETHOD("<clinit>", MType([], VoidType()), False, frame_clinit))
        frame_clinit.enterScope(True)
        self.emit.printout(self.emit.emitLABEL(frame_clinit.getStartLabel(), frame_clinit))
        for decl in ast.decls:
            if type(decl) == VarDecl:
                if decl.init:
                    initValue, initType = self.visit(decl.init, evnList_clinit)
                    if type(decl.typ) == FloatType and type(initType) == IntegerType:
                        self.emit.printout(self.emit.emitI2F())
                    self.emit.printout(self.emit.emitPUTSTATIC(f"MT22Class/{decl.name}", decl.typ, frame_clinit))
                else:
                    pass
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
        
        # Other functions
        for decl in ast.decls:
            if type(decl) != VarDecl:
                evnList_func.sym[0] += [self.visit(decl, evnList_func)]
        
        self.emit.emitEPILOG()
