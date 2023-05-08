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
    
    # Literals
    def visitBinExpr(self, ast, o):
        op = str(ast.op)
        left = ast.left
        right = ast.right
        frame = o.frame
        
        if op != "::":
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
                self.emit.printout(self.emit.emitADDOP(op, typ, frame))
                return ast, typ
            elif op == "*" or op == "/":
                self.emit.printout(self.emit.emitMULOP(op, typ, frame))
                return ast, typ
            elif op == "%":
                self.emit.printout(self.emit.emitMOD(frame))
                return ast, typ
            elif op == "&&":
                self.emit.printout(self.emit.emitANDOP(frame))
                return ast, typ
            elif op == "||":
                self.emit.printout(self.emit.emitOROP(frame))
                return ast, typ
            elif op == "==" or op == "!=" or op == "<" or op == ">" or op == "<=" or op == ">=":
                self.emit.printout(self.emit.emitREOP(op, typ, frame))
                return ast, typ
        else:
            # TODO String concat
            pass
            # self.emit.printout(self.emit.emitNEW("java/lang/StringBuilder", frame))
            # self.emit.printout(self.emit.emitDUP(frame))
            # self.emit.printout(self.emit.emitINVOKESPECIAL(frame, "java/lang/StringBuilder/<init>", "()V"))
            # leftValue, leftType = self.visit(left, o)
            # self.emit.printout(self.emit.emitINVOKEVIRTUAL("java/lang/StringBuilder/append", "(java/lang/String;)Ljava/lang/StringBuilder;", frame))
            # rightValue, rightType = self.visit(right, o)
            # self.emit.printout(self.emit.emitINVOKEVIRTUAL("java/lang/StringBuilder/append", "(java/lang/String;)Ljava/lang/StringBuilder;", frame))
            # self.emit.printout(self.emit.emitINVOKEVIRTUAL("java/lang/StringBuilder/toString", "()Ljava/lang/String;", frame))
            # return None, leftType
    
    def visitUnExpr(self, ast, o):
        op = str(ast.op)
        val = ast.val
        frame = o.frame
        
        value, typ = self.visit(val, o)
        
        if op == "-":
            self.emit.printout(self.emit.emitNEGOP(typ, frame))
            return ast, typ
        elif op == "!":
            self.emit.printout(self.emit.emitNOT(typ, frame))
            return ast, typ
    
    def visitId(self, ast, o):
        name = ast.name
        frame = o.frame
        sym = o.sym
        
        for i in range(len(sym) - 1, -1 , -1):
            for j in range(len(sym[i])):
                if i == 0:
                    if sym[i][j].name == name and type(sym[i][j]) == VarDecl:
                        self.emit.printout(self.emit.emitGETSTATIC(f"MT22Class/{sym[i][j].name}", sym[i][j].typ, frame))
                        return sym[i][j].init, sym[i][j].typ
                else: 
                    if sym[i][j].name == name and type(sym[i][j]) == VarDecl:
                        total_length = 0
                        for k in range(1, i):
                            total_length += len(sym[k])
                        idx = j + total_length
                        self.emit.printout(self.emit.emitREADVAR(sym[i][j].name, sym[i][j].typ, idx, frame))
                        return sym[i][j].init, sym[i][j].typ
    
    def visitArrayCell(self, ast, o):
        name = ast.name
        cell = ast.cell
        frame = o.frame
        sym = o.sym
        
        for i in range(len(sym) - 1, -1 , -1):
            for j in range(len(sym[i])):
                if i == 0:
                    if sym[i][j].name == name and type(sym[i][j]) == VarDecl:
                        self.emit.printout(self.emit.emitGETSTATIC(f"MT22Class/{sym[i][j].name}", sym[i][j].typ, frame))
                        for k in range(len(cell)):
                            cellValue, cellType = self.visit(cell[k], o)
                            if k == len(cell) - 1:
                                self.emit.printout(self.emit.emitALOAD(sym[i][j].typ.typ, frame))
                            else:
                                self.emit.printout(self.emit.emitALOAD(sym[i][j].typ, frame))
                        return sym[i][j].init, sym[i][j].typ.typ
                else: 
                    if sym[i][j].name == name and type(sym[i][j]) == VarDecl:
                        total_length = 0
                        for k in range(1, i):
                            total_length += len(sym[k])
                        idx = j + total_length
                        self.emit.printout(self.emit.emitREADVAR(sym[i][j].name, sym[i][j].typ, idx, frame))
                        for k in range(len(cell)):
                            cellValue, cellType = self.visit(cell[k], o)
                            if k == len(cell) - 1:
                                self.emit.printout(self.emit.emitALOAD(sym[i][j].typ.typ, frame))
                            else:
                                self.emit.printout(self.emit.emitALOAD(sym[i][j].typ, frame))
                        return sym[i][j].init, sym[i][j].typ.typ
    
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
            if type(exp) == ArrayLit:
                res += self.visit(exp, o)
            else:
                res += [exp]
        return res
        
    def visitFuncCall(self, ast, o): pass # TODO

    # Statements
    def visitAssignStmt(self, ast, o):
        lhs = ast.lhs
        rhs = ast.rhs
        frame = o.frame

        if type(lhs) == Id:
            name = lhs.name
            frame = o.frame
            sym = o.sym
            
            for i in range(len(sym) - 1, -1 , -1):
                for j in range(len(sym[i])):
                    if i == 0:
                        if sym[i][j].name == name and type(sym[i][j]) == VarDecl:
                            rightValue, rightType = self.visit(rhs, o)
                            if type(sym[i][j].typ) == FloatType and type(rightType) == IntegerType:
                                self.emit.printout(self.emit.emitI2F(frame))
                            self.emit.printout(self.emit.emitPUTSTATIC(f"MT22Class/{sym[i][j].name}", sym[i][j].typ, frame))
                            return
                    else: 
                        if sym[i][j].name == name and (type(sym[i][j]) == VarDecl or type(sym[i][j]) == ParamDecl):
                            total_length = 0
                            for k in range(1, i):
                                total_length += len(sym[k])
                            idx = j + total_length
                            rightValue, rightType = self.visit(rhs, o)
                            if type(sym[i][j].typ) == FloatType and type(rightType) == IntegerType:
                                self.emit.printout(self.emit.emitI2F(frame))
                            self.emit.printout(self.emit.emitWRITEVAR(sym[i][j].name, sym[i][j].typ, idx, frame))
                            return
                        
        elif type(lhs) == ArrayCell:
            name = lhs.name
            cell = lhs.cell
            frame = o.frame
            sym = o.sym
            for i in range(len(sym) - 1, -1 , -1):
                for j in range(len(sym[i])):
                    if i == 0:
                        if sym[i][j].name == name and type(sym[i][j]) == VarDecl:
                            self.emit.printout(self.emit.emitGETSTATIC(f"MT22Class/{sym[i][j].name}", sym[i][j].typ, frame))
                            for k in range(len(cell)):
                                cellValue, cellType = self.visit(cell[k], o)
                                if k != len(cell) - 1:
                                    self.emit.printout(self.emit.emitALOAD(sym[i][j].typ, frame))
                            rightValue, rightType = self.visit(rhs, o)
                            self.emit.printout(self.emit.emitASTORE(rightType, frame))
                            return
                    else: 
                        if sym[i][j].name == name and (type(sym[i][j]) == VarDecl or type(sym[i][j]) == ParamDecl):
                            total_length = 0
                            for k in range(1, i):
                                total_length += len(sym[k])
                            idx = j + total_length
                            self.emit.printout(self.emit.emitREADVAR(sym[i][j].name, sym[i][j].typ, idx, frame))
                            for k in range(len(cell)):
                                cellValue, cellType = self.visit(cell[k], o)
                                if k != len(cell) - 1:
                                    self.emit.printout(self.emit.emitALOAD(sym[i][j].typ, frame))
                            rightValue, rightType = self.visit(rhs, o)
                            self.emit.printout(self.emit.emitASTORE(rightType, frame))
                            return
        
    def visitBlockStmt(self, ast, o):
        body = ast.body
        frame = o.frame
        
        frame.enterScope(False)
        
        # Variables in inner block
        evnList = SubBody(frame, o.sym.copy())
        local_var = SubBody(frame, [])
        for ele in body:
            if type(ele) == VarDecl:
                local_var.sym += [self.visit(ele, local_var)]
        
        # Statements
        self.emit.printout(self.emit.emitLABEL(frame.getStartLabel(), frame))
        
        counter = 0
        for ele in body:
            if type(ele) == VarDecl:
                if body.index(ele) == 0:
                    evnList.sym += [[local_var.sym[counter]]]
                    counter += 1
                else:
                    evnList.sym[-1] += [local_var.sym[counter]]
                    counter += 1
                if ele.init:
                    total_length = 0
                    for i in range(1, len(evnList.sym) - 1):
                        total_length += len(evnList.sym[i])
                    idx = body.index(ele) + total_length
                    if type(ele.typ) != ArrayType:
                        initValue, initType = self.visit(ele.init, evnList)
                        if type(ele.typ) == FloatType and type(initType) == IntegerType:
                            self.emit.printout(self.emit.emitI2F(frame))
                        self.emit.printout(self.emit.emitWRITEVAR(ele.name, ele.typ, idx, frame))
                    else:
                        initValue = self.visit(ele.init, evnList)
                        if len(ele.typ.dimensions) == 1:
                            self.emit.printout(self.emit.emitPUSHICONST(int(ele.typ.dimensions[0]), frame))
                            self.emit.printout(self.emit.emitANEWARRAY(ele.typ, len(ele.typ.dimensions), frame))
                            self.emit.printout(self.emit.emitWRITEVAR(ele.name, ele.typ, idx, frame))
                            
                            for i in range(int(ele.typ.dimensions[0])):
                                self.emit.printout(self.emit.emitREADVAR(ele.name, ele.typ, idx, frame))
                                self.emit.printout(self.emit.emitPUSHICONST(i, frame))
                                cellValue, cellType = self.visit(initValue[i], evnList)
                                self.emit.printout(self.emit.emitASTORE(cellType, frame))
                        else:
                            self.emit.printout(self.emit.emitPUSHICONST(int(ele.typ.dimensions[0]), frame))
                            self.emit.printout(self.emit.emitANEWARRAY(ele.typ, len(ele.typ.dimensions), frame))
                            self.emit.printout(self.emit.emitWRITEVAR(ele.name, ele.typ, idx, frame))
                            for i in range(int(ele.typ.dimensions[0])):
                                self.emit.printout(self.emit.emitREADVAR(ele.name, ele.typ, idx, frame))
                                self.emit.printout(self.emit.emitPUSHICONST(i, frame))
                                self.emit.printout(self.emit.emitPUSHICONST(int(ele.typ.dimensions[1]), frame))
                                self.emit.printout(self.emit.emitANEWARRAY(ele.typ, len(ele.typ.dimensions) - 1, frame))
                                self.emit.printout(self.emit.emitASTORE(ele.typ, frame))

                                if len(ele.typ.dimensions) > 2:
                                    self.emit.printout(self.emit.emitREADVAR(ele.name, ele.typ, idx, frame))
                                    self.emit.printout(self.emit.emitPUSHICONST(i, frame))
                                    self.emit.printout(self.emit.emitALOAD(ele.typ, frame))
                                    self.arrayTraversalBare(ele.name, ele.typ, ele.typ.dimensions[1:], frame)
                            
                            for i in range(int(ele.typ.dimensions[0])):
                                self.emit.printout(self.emit.emitREADVAR(ele.name, ele.typ, idx, frame))
                                self.emit.printout(self.emit.emitPUSHICONST(i, frame))
                                self.emit.printout(self.emit.emitALOAD(ele.typ, frame))
                                self.arrayTraversalInit(ele.name, ele.typ, ele.typ.dimensions[1:], frame, initValue, evnList)
                else:
                    # TODO Var trong function ma ko co init thi ko tao default value, chi khoi tao array
                    total_length = 0
                    for i in range(1, len(evnList.sym) - 1):
                        total_length += len(evnList.sym[i])
                    idx = body.index(ele) + total_length
                    if type(ele.typ) == ArrayType:
                        if len(ele.typ.dimensions) == 1:
                            self.emit.printout(self.emit.emitPUSHICONST(int(ele.typ.dimensions[0]), frame))
                            self.emit.printout(self.emit.emitANEWARRAY(ele.typ, len(ele.typ.dimensions), frame))
                            self.emit.printout(self.emit.emitWRITEVAR(ele.name, ele.typ, idx, frame))
                        else:
                            self.emit.printout(self.emit.emitPUSHICONST(int(ele.typ.dimensions[0]), frame))
                            self.emit.printout(self.emit.emitANEWARRAY(ele.typ, len(ele.typ.dimensions), frame))
                            self.emit.printout(self.emit.emitWRITEVAR(ele.name, ele.typ, idx, frame))
                            for i in range(int(ele.typ.dimensions[0])):
                                self.emit.printout(self.emit.emitREADVAR(ele.name, ele.typ, idx, frame))
                                self.emit.printout(self.emit.emitPUSHICONST(i, frame))
                                self.emit.printout(self.emit.emitPUSHICONST(int(ele.typ.dimensions[1]), frame))
                                self.emit.printout(self.emit.emitANEWARRAY(ele.typ, len(ele.typ.dimensions) - 1, frame))
                                self.emit.printout(self.emit.emitASTORE(ele.typ, frame))

                                if len(ele.typ.dimensions) > 2:
                                    self.emit.printout(self.emit.emitREADVAR(ele.name, ele.typ, idx, frame))
                                    self.emit.printout(self.emit.emitPUSHICONST(i, frame))
                                    self.emit.printout(self.emit.emitALOAD(ele.typ, frame))
                                    self.arrayTraversalBare(ele.name, ele.typ, ele.typ.dimensions[1:], frame)
            else:
                self.visit(ele, evnList)
        
        self.emit.printout(self.emit.emitLABEL(frame.getEndLabel(), frame))
        
        frame.exitScope()
        
    def visitIfStmt(self, ast, o): pass
    
    def visitForStmt(self, ast, o): pass
    
    def visitWhileStmt(self, ast, o): pass
    
    def visitDoWhileStmt(self, ast, o): pass
    
    def visitBreakStmt(self, ast, o): pass
    
    def visitContinueStmt(self, ast, o): pass
    
    def visitReturnStmt(self, ast, o):
        expr = ast.expr
        frame = o.frame
        
        funcList = [func for func in o.sym[0] if type(func) == FuncDecl]
        return_type = funcList[self.func_counter].return_type
        
        if expr:
            exprValue, exprType = self.visit(expr, o)
            if type(return_type) == FloatType and type(exprType) == IntegerType:
                self.emit.printout(self.emit.emitI2F(frame))
                self.emit.printout(self.emit.emitRETURN(return_type, frame))
            else:
                self.emit.printout(self.emit.emitRETURN(exprType, frame))
        else:
            self.emit.printout(self.emit.emitRETURN(VoidType(), frame))
    
    def visitCallStmt(self, ast, o): pass
    
    # Declarations
    def visitVarDecl(self, ast, o):
        name = ast.name
        typ = ast.typ
        init = ast.init
        frame = o.frame

        idx = frame.getNewIndex()
        self.emit.printout(self.emit.emitVAR(idx, name, typ, frame.getStartLabel(), frame.getEndLabel(), frame))
        
        return ast
        
    def visitParamDecl(self, ast, o):
        name = ast.name
        typ = ast.typ
        out = ast.out
        inherit = ast.inherit
        frame = o.frame
        
        idx = frame.getNewIndex()
        self.emit.printout(self.emit.emitVAR(idx, name, typ, frame.getStartLabel(), frame.getEndLabel(), frame))
        
        return ast
    
    def visitFuncDecl(self, ast, o):
        name = ast.name
        return_type = ast.return_type
        params = ast.params
        inherit = ast.inherit
        body = ast.body.body
        frame =  Frame(name, return_type)
        
        isMain = name == "main" and type(return_type) == VoidType and len(params) == 0
        in_type = [ArrayType(0, StringType())] if isMain else list(map(lambda para: para.typ, params))
        mtype =  MType(in_type, return_type)
        
        self.emit.printout(self.emit.emitMETHOD(name, mtype, True, frame))
        
        frame.enterScope(True)
        
        # Parameters, and Variables in outer block
        evnList = SubBody(frame, o.sym.copy())
        if isMain:
            self.emit.printout(self.emit.emitVAR(frame.getNewIndex(), "args", ArrayType(0, StringType()), frame.getStartLabel(), frame.getEndLabel(), frame))
        else:
            local_para = SubBody(frame, [])
            for ele in params:
                local_para.sym += [self.visit(ele, local_para)]
            evnList.sym += [local_para.sym]
        
        local_var = SubBody(frame, [])
        for ele in body:
            if type(ele) == VarDecl:
                local_var.sym += [self.visit(ele, local_var)]
        
        # Statements
        self.emit.printout(self.emit.emitLABEL(frame.getStartLabel(), frame))
        counter = 0
        for ele in body:
            if type(ele) == VarDecl:
                if body.index(ele) == 0:
                    evnList.sym += [[local_var.sym[counter]]]
                    counter += 1
                else:
                    evnList.sym[-1] += [local_var.sym[counter]]
                    counter += 1
                if ele.init:
                    idx = body.index(ele) + len(params)
                    if type(ele.typ) != ArrayType:
                        initValue, initType = self.visit(ele.init, evnList)
                        if type(ele.typ) == FloatType and type(initType) == IntegerType:
                            self.emit.printout(self.emit.emitI2F(frame))
                        self.emit.printout(self.emit.emitWRITEVAR(ele.name, ele.typ, idx, frame))
                    else:
                        initValue = self.visit(ele.init, evnList)
                        if len(ele.typ.dimensions) == 1:
                            self.emit.printout(self.emit.emitPUSHICONST(int(ele.typ.dimensions[0]), frame))
                            self.emit.printout(self.emit.emitANEWARRAY(ele.typ, len(ele.typ.dimensions), frame))
                            self.emit.printout(self.emit.emitWRITEVAR(ele.name, ele.typ, idx, frame))
                            
                            for i in range(int(ele.typ.dimensions[0])):
                                self.emit.printout(self.emit.emitREADVAR(ele.name, ele.typ, idx, frame))
                                self.emit.printout(self.emit.emitPUSHICONST(i, frame))
                                cellValue, cellType = self.visit(initValue[i], evnList)
                                self.emit.printout(self.emit.emitASTORE(cellType, frame))
                        else:
                            self.emit.printout(self.emit.emitPUSHICONST(int(ele.typ.dimensions[0]), frame))
                            self.emit.printout(self.emit.emitANEWARRAY(ele.typ, len(ele.typ.dimensions), frame))
                            self.emit.printout(self.emit.emitWRITEVAR(ele.name, ele.typ, idx, frame))
                            for i in range(int(ele.typ.dimensions[0])):
                                self.emit.printout(self.emit.emitREADVAR(ele.name, ele.typ, idx, frame))
                                self.emit.printout(self.emit.emitPUSHICONST(i, frame))
                                self.emit.printout(self.emit.emitPUSHICONST(int(ele.typ.dimensions[1]), frame))
                                self.emit.printout(self.emit.emitANEWARRAY(ele.typ, len(ele.typ.dimensions) - 1, frame))
                                self.emit.printout(self.emit.emitASTORE(ele.typ, frame))

                                if len(ele.typ.dimensions) > 2:
                                    self.emit.printout(self.emit.emitREADVAR(ele.name, ele.typ, idx, frame))
                                    self.emit.printout(self.emit.emitPUSHICONST(i, frame))
                                    self.emit.printout(self.emit.emitALOAD(ele.typ, frame))
                                    self.arrayTraversalBare(ele.name, ele.typ, ele.typ.dimensions[1:], frame)
                            
                            for i in range(int(ele.typ.dimensions[0])):
                                self.emit.printout(self.emit.emitREADVAR(ele.name, ele.typ, idx, frame))
                                self.emit.printout(self.emit.emitPUSHICONST(i, frame))
                                self.emit.printout(self.emit.emitALOAD(ele.typ, frame))
                                self.arrayTraversalInit(ele.name, ele.typ, ele.typ.dimensions[1:], frame, initValue, evnList)
                else:
                    # TODO Var trong function ma ko co init thi ko tao default value, chi khoi tao array
                    idx = body.index(ele) + len(local_para.sym)
                    if type(ele.typ) == ArrayType:
                        if len(ele.typ.dimensions) == 1:
                            self.emit.printout(self.emit.emitPUSHICONST(int(ele.typ.dimensions[0]), frame))
                            self.emit.printout(self.emit.emitANEWARRAY(ele.typ, len(ele.typ.dimensions), frame))
                            self.emit.printout(self.emit.emitWRITEVAR(ele.name, ele.typ, idx, frame))
                        else:
                            self.emit.printout(self.emit.emitPUSHICONST(int(ele.typ.dimensions[0]), frame))
                            self.emit.printout(self.emit.emitANEWARRAY(ele.typ, len(ele.typ.dimensions), frame))
                            self.emit.printout(self.emit.emitWRITEVAR(ele.name, ele.typ, idx, frame))
                            for i in range(int(ele.typ.dimensions[0])):
                                self.emit.printout(self.emit.emitREADVAR(ele.name, ele.typ, idx, frame))
                                self.emit.printout(self.emit.emitPUSHICONST(i, frame))
                                self.emit.printout(self.emit.emitPUSHICONST(int(ele.typ.dimensions[1]), frame))
                                self.emit.printout(self.emit.emitANEWARRAY(ele.typ, len(ele.typ.dimensions) - 1, frame))
                                self.emit.printout(self.emit.emitASTORE(ele.typ, frame))

                                if len(ele.typ.dimensions) > 2:
                                    self.emit.printout(self.emit.emitREADVAR(ele.name, ele.typ, idx, frame))
                                    self.emit.printout(self.emit.emitPUSHICONST(i, frame))
                                    self.emit.printout(self.emit.emitALOAD(ele.typ, frame))
                                    self.arrayTraversalBare(ele.name, ele.typ, ele.typ.dimensions[1:], frame)
            elif type(ele) == CallStmt and ele.name == "super":
                # TODO Super
                pass
            else:
                self.visit(ele, evnList)
        
        self.emit.printout(self.emit.emitLABEL(frame.getEndLabel(), frame))
        
        frame.exitScope()
            
        self.emit.printout(self.emit.emitENDMETHOD(frame))
        
        return ast

    # Program
    def visitProgram(self, ast, o):
        self.func_counter = 0
        
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
        
        ## Initializing all global variables
        self.emit.printout(self.emit.emitLABEL(frame_clinit.getStartLabel(), frame_clinit))
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
                            self.emit.printout(self.emit.emitANEWARRAY(decl.typ, len(decl.typ.dimensions), frame_clinit))
                            self.emit.printout(self.emit.emitPUTSTATIC(f"MT22Class/{decl.name}", decl.typ, frame_clinit))
                            
                            for i in range(int(decl.typ.dimensions[0])):
                                self.emit.printout(self.emit.emitGETSTATIC(f"MT22Class/{decl.name}", decl.typ, frame_clinit))
                                self.emit.printout(self.emit.emitPUSHICONST(i, frame_clinit))
                                cellValue, cellType = self.visit(initValue[i], evnList_clinit)
                                self.emit.printout(self.emit.emitASTORE(cellType, frame_clinit))
                        else:
                            self.emit.printout(self.emit.emitPUSHICONST(int(decl.typ.dimensions[0]), frame_clinit))
                            self.emit.printout(self.emit.emitANEWARRAY(decl.typ, len(decl.typ.dimensions), frame_clinit))
                            self.emit.printout(self.emit.emitPUTSTATIC(f"MT22Class/{decl.name}", decl.typ, frame_clinit))
                            for i in range(int(decl.typ.dimensions[0])):
                                self.emit.printout(self.emit.emitGETSTATIC(f"MT22Class/{decl.name}", decl.typ, frame_clinit))
                                self.emit.printout(self.emit.emitPUSHICONST(i, frame_clinit))
                                self.emit.printout(self.emit.emitPUSHICONST(int(decl.typ.dimensions[1]), frame_clinit))
                                self.emit.printout(self.emit.emitANEWARRAY(decl.typ, len(decl.typ.dimensions) - 1, frame_clinit))
                                self.emit.printout(self.emit.emitASTORE(decl.typ, frame_clinit))

                                if len(decl.typ.dimensions) > 2:
                                    self.emit.printout(self.emit.emitGETSTATIC(f"MT22Class/{decl.name}", decl.typ, frame_clinit))
                                    self.emit.printout(self.emit.emitPUSHICONST(i, frame_clinit))
                                    self.emit.printout(self.emit.emitALOAD(decl.typ, frame_clinit))
                                    self.arrayTraversalBare(decl.name, decl.typ, decl.typ.dimensions[1:], frame_clinit)
                            
                            for i in range(int(decl.typ.dimensions[0])):
                                self.emit.printout(self.emit.emitGETSTATIC(f"MT22Class/{decl.name}", decl.typ, frame_clinit))
                                self.emit.printout(self.emit.emitPUSHICONST(i, frame_clinit))
                                self.emit.printout(self.emit.emitALOAD(decl.typ, frame_clinit))
                                self.arrayTraversalInit(decl.name, decl.typ, decl.typ.dimensions[1:], frame_clinit, initValue, evnList_clinit)
                else:
                    # if type(decl.typ) == IntegerType:
                    #     initValue, initType = self.visit(IntegerLit(0), evnList_clinit)
                    #     self.emit.printout(self.emit.emitPUTSTATIC(f"MT22Class/{decl.name}", decl.typ, frame_clinit))
                    # elif type(decl.typ) == FloatType:
                    #     initValue, initType = self.visit(FloatLit(0.0), evnList_clinit)
                    #     self.emit.printout(self.emit.emitPUTSTATIC(f"MT22Class/{decl.name}", decl.typ, frame_clinit))
                    # elif type(decl.typ) == BooleanType:
                    #     initValue, initType = self.visit(BooleanLit(False), evnList_clinit)
                    #     self.emit.printout(self.emit.emitPUTSTATIC(f"MT22Class/{decl.name}", decl.typ, frame_clinit))
                    # elif type(decl.typ) == StringType:
                    #     initValue, initType = self.visit(StringLit(""), evnList_clinit)
                    #     self.emit.printout(self.emit.emitPUTSTATIC(f"MT22Class/{decl.name}", decl.typ, frame_clinit))
                    if type(decl.typ) == ArrayType:
                        if len(decl.typ.dimensions) == 1:
                            self.emit.printout(self.emit.emitPUSHICONST(int(decl.typ.dimensions[0]), frame_clinit))
                            self.emit.printout(self.emit.emitANEWARRAY(decl.typ, len(decl.typ.dimensions), frame_clinit))
                            self.emit.printout(self.emit.emitPUTSTATIC(f"MT22Class/{decl.name}", decl.typ, frame_clinit))
                        else:
                            self.emit.printout(self.emit.emitPUSHICONST(int(decl.typ.dimensions[0]), frame_clinit))
                            self.emit.printout(self.emit.emitANEWARRAY(decl.typ, len(decl.typ.dimensions), frame_clinit))
                            self.emit.printout(self.emit.emitPUTSTATIC(f"MT22Class/{decl.name}", decl.typ, frame_clinit))
                            for i in range(int(decl.typ.dimensions[0])):
                                self.emit.printout(self.emit.emitGETSTATIC(f"MT22Class/{decl.name}", decl.typ, frame_clinit))
                                self.emit.printout(self.emit.emitPUSHICONST(i, frame_clinit))
                                self.emit.printout(self.emit.emitPUSHICONST(int(decl.typ.dimensions[1]), frame_clinit))
                                self.emit.printout(self.emit.emitANEWARRAY(decl.typ, len(decl.typ.dimensions) - 1, frame_clinit))
                                self.emit.printout(self.emit.emitASTORE(decl.typ, frame_clinit))

                                if len(decl.typ.dimensions) > 2:
                                    self.emit.printout(self.emit.emitGETSTATIC(f"MT22Class/{decl.name}", decl.typ, frame_clinit))
                                    self.emit.printout(self.emit.emitPUSHICONST(i, frame_clinit))
                                    self.emit.printout(self.emit.emitALOAD(decl.typ, frame_clinit))
                                    self.arrayTraversalBare(decl.name, decl.typ, decl.typ.dimensions[1:], frame_clinit)
                       
        self.emit.printout(self.emit.emitLABEL(frame_clinit.getEndLabel(), frame_clinit))
        self.emit.printout(self.emit.emitRETURN(VoidType(), frame_clinit))
        frame_clinit.exitScope()
        self.emit.printout(self.emit.emitENDMETHOD(frame_clinit))
        
        # Default constructor
        self.emit.printout(self.emit.emitMETHOD("<init>", MType([], VoidType()), False, frame_init))
        frame_init.enterScope(True)
        self.emit.printout(self.emit.emitVAR(frame_init.getNewIndex(), "this", "LMT22Class;", frame_init.getStartLabel(), frame_init.getEndLabel(), frame_init))
        self.emit.printout(self.emit.emitLABEL(frame_init.getStartLabel(), frame_init))
        self.emit.printout(self.emit.emitREADVAR("this", "LMT22Class;", 0, frame_init))
        self.emit.printout(self.emit.emitINVOKESPECIAL(frame_init))
        self.emit.printout(self.emit.emitLABEL(frame_init.getEndLabel(), frame_init))
        self.emit.printout(self.emit.emitRETURN(VoidType(), frame_init))
        frame_init.exitScope()
        self.emit.printout(self.emit.emitENDMETHOD(frame_init))
        
        # Other functions, including main
        for decl in ast.decls:
            if type(decl) == FuncDecl:
                self.visit(decl, evnList_func)
                self.func_counter += 1

        # Generate .j file
        self.emit.emitEPILOG()
        
    def arrayTraversalBare(self, name, typ, dim, frame):
        if len(dim) == 2:
            for i in range(int(dim[0])):
                self.emit.printout(self.emit.emitDUP(frame))
                
                self.emit.printout(self.emit.emitPUSHICONST(i, frame))
                self.emit.printout(self.emit.emitPUSHICONST(int(dim[1]), frame))
                self.emit.printout(self.emit.emitANEWARRAY(typ, len(dim) - 1, frame))
                self.emit.printout(self.emit.emitASTORE(typ, frame))
                
            self.emit.printout(self.emit.emitPOP(frame))
        else:
            for i in range(int(dim[0])):
                self.emit.printout(self.emit.emitDUP(frame))

                self.emit.printout(self.emit.emitPUSHICONST(i, frame))
                self.emit.printout(self.emit.emitPUSHICONST(int(dim[1]), frame))
                self.emit.printout(self.emit.emitANEWARRAY(typ, len(dim) - 1, frame))
                self.emit.printout(self.emit.emitASTORE(typ, frame))

                self.emit.printout(self.emit.emitDUP(frame))
                self.emit.printout(self.emit.emitPUSHICONST(i, frame))
                self.emit.printout(self.emit.emitALOAD(typ, frame))
                self.arrayTraversalBare(name, typ, dim[1:], frame)
                
            self.emit.printout(self.emit.emitPOP(frame))
    
    def arrayTraversalInit(self, name, typ, dim, frame, init, evn):
        if len(dim) == 1:
            for i in range(int(dim[0])):
                self.emit.printout(self.emit.emitDUP(frame))
                
                self.emit.printout(self.emit.emitPUSHICONST(i, frame))
                eleValue, eleType = self.visit(init[0], evn)
                self.emit.printout(self.emit.emitASTORE(eleType, frame))
                
                init.pop(0)
                    
            self.emit.printout(self.emit.emitPOP(frame))
        else:
            for i in range(int(dim[0])):
                self.emit.printout(self.emit.emitDUP(frame))
                
                self.emit.printout(self.emit.emitPUSHICONST(i, frame))
                self.emit.printout(self.emit.emitALOAD(typ, frame))
                self.arrayTraversalInit(name, typ, dim[1:], frame, init, evn)
                
            self.emit.printout(self.emit.emitPOP(frame))
