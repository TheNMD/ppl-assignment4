from Utils import *
# from StaticCheck import *
# from StaticError import *
import CodeGenerator as cgen
from MachineCode import JasminCode
from AST import *


class Emitter():
    def __init__(self, filename):
        self.filename = filename
        self.buff = list()
        self.jvm = JasminCode()

    def getJVMType(self, inType):
        typeIn = type(inType)
        if typeIn is IntegerType:
            return "I"
        elif typeIn is FloatType:
            return "F"
        elif typeIn is BooleanType:
            return "Z"
        elif typeIn is StringType:
            return "Ljava/lang/String;"
        elif typeIn is VoidType:
            return "V"
        elif typeIn is ArrayType:
            if inType.dimensions == 0:
                return "[" + "Ljava/lang/String;"
            else:
                bracket = ""
                for i in range(len(inType.dimensions)):
                    bracket += "["
                if type(inType.typ) == IntegerType:
                    return bracket + "I"
                elif type(inType.typ) == FloatType:
                    return bracket + "F"
                elif type(inType.typ) == BooleanType:
                    return bracket + "Z"
                elif type(inType.typ) == StringType:
                    return bracket + "Ljava/lang/String;"
        elif typeIn is cgen.MType:
            return "(" + "".join(list(map(lambda x: self.getJVMType(x), inType.partype))) + ")" + self.getJVMType(inType.rettype)

    def getFullType(self, inType):
        typeIn = type(inType)
        if typeIn is IntegerType:
            return "int"
        elif typeIn is FloatType:
            return "float"
        elif typeIn is BooleanType:
            return "boolean"
        elif typeIn is StringType:
            return "java/lang/String"
        elif typeIn is VoidType:
            return "void"
    
    def emitPUSHICONST(self, in_, frame):
        # in: Int or Sring
        # frame: Frame

        frame.push()
        
        if type(in_) is int:
            i = in_
            if i >= -1 and i <= 5:
                return self.jvm.emitICONST(i)
            elif i >= -128 and i <= 127:
                return self.jvm.emitBIPUSH(i)
            elif i >= -32768 and i <= 32767:
                return self.jvm.emitSIPUSH(i)
            else:
                return self.jvm.emitLDC(str(i))
        elif type(in_) is str:
            if in_ == "True":
                return self.jvm.emitICONST(1)
            elif in_ == "False":
                return self.jvm.emitICONST(0)
            else:
                return self.jvm.emitLDC(f""" "{in_}" """)

    def emitPUSHFCONST(self, in_, frame):
        # in_: String
        # frame: Frame

        f = float(in_)
        frame.push()
        rst = "{0:.4f}".format(f)
        if rst == "0.0" or rst == "1.0" or rst == "2.0":
            return self.jvm.emitFCONST(rst)
        else:
            return self.jvm.emitLDC(in_)
    
    ''' 
    *    generate code to push a constant onto the operand stack.
    *    @param in the lexeme of the constant
    *    @param typ the type of the constant
    '''
    
    def emitALOAD(self, in_, frame):
        # in_: Type
        # frame: Frame
        # ..., arrayref, index -> ...
        frame.pop()
        if type(in_) is IntegerType:
            return self.jvm.emitIALOAD()
        elif type(in_) is FloatType:
            return self.jvm.emitFALOAD()
        elif type(in_) is BooleanType:
            return self.jvm.emitBALOAD()
        elif type(in_) is StringType:
            return self.jvm.emitAALOAD()
        elif type(in_) is ArrayType:
            return self.jvm.emitAALOAD()

    def emitASTORE(self, in_, frame):
        # in_: Type
        # frame: Frame
        # ..., arrayref, index, value -> ...

        frame.pop()
        frame.pop()
        frame.pop()
        if type(in_) is IntegerType:
            return self.jvm.emitIASTORE()
        elif type(in_) is FloatType:
            return self.jvm.emitFASTORE()
        elif type(in_) is BooleanType:
            return self.jvm.emitBASTORE()
        elif type(in_) is StringType:
            return self.jvm.emitAASTORE()
        elif type(in_) is ArrayType:
            return self.jvm.emitAASTORE()

    '''    generate the var directive for a local variable.
    *   @param in the index of the local variable.
    *   @param varName the name of the local variable.
    *   @param inType the type of the local variable.
    *   @param fromLabel the starting label of the scope where the variable is active.
    *   @param toLabel the ending label  of the scope where the variable is active.
    '''

    def emitVAR(self, in_, varName, inType, fromLabel, toLabel, frame):
        # in_: Int
        # varName: String
        # inType: Type
        # fromLabel: Int
        # toLabel: Int
        # frame: Frame

        if type(inType) == str and inType == "LMT22Class;":
            return self.jvm.emitVAR(in_, varName, inType, fromLabel, toLabel)
        else:
            return self.jvm.emitVAR(in_, varName, self.getJVMType(inType), fromLabel, toLabel)

    def emitREADVAR(self, name, inType, index, frame):
        # name: String
        # inType: Type
        # index: Int
        # frame: Frame
        # ... -> ..., value

        frame.push()
        if type(inType) is IntegerType:
            return self.jvm.emitILOAD(index)
        elif type(inType) is FloatType:
            return self.jvm.emitFLOAD(index)
        elif type(inType) is BooleanType:
            return self.jvm.emitILOAD(index)
        elif type(inType) is StringType:
            return self.jvm.emitALOAD(index)
        elif type(inType) is ArrayType:
            return self.jvm.emitALOAD(index) 
        elif type(inType) == str and inType == "LMT22Class;":
            return self.jvm.emitALOAD(index)
        else:
            raise IllegalOperandException(name)

    ''' generate the second instruction for array cell access
    *
    '''

    # def emitREADVAR2(self, name, typ, frame):
    #     # name: String
    #     # typ: Type
    #     # frame: Frame
    #     # ... -> ..., value

    #     # TODO
    #     # frame.push()
    #     raise IllegalOperandException(name)

    '''
    *   generate code to pop a value on top of the operand stack and store it to a block-scoped variable.
    *   @param name the symbol entry of the variable.
    '''

    def emitWRITEVAR(self, name, inType, index, frame):
        # name: String
        # inType: Type
        # index: Int
        # frame: Frame
        # ..., value -> ...
        frame.pop()
        if type(inType) is IntegerType:
            return self.jvm.emitISTORE(index)
        elif type(inType) is FloatType:
            return self.jvm.emitFSTORE(index)
        elif type(inType) is BooleanType:
            return self.jvm.emitISTORE(index)
        elif type(inType) is StringType:
            return self.jvm.emitASTORE(index)
        elif type(inType) is ArrayType:
            return self.jvm.emitASTORE(index)
        else:
            raise IllegalOperandException(name)

    ''' generate the second instruction for array cell access
    *
    '''

    # def emitWRITEVAR2(self, name, typ, frame):
    #     # name: String
    #     # typ: Type
    #     # frame: Frame
    #     # ..., value -> ...
        
    #     # TODO
    #     # frame.push()
    #     raise IllegalOperandException(name)

    ''' generate the field (static) directive for a class mutable or immutable attribute.
    *   @param lexeme the name of the attribute.
    *   @param in the type of the attribute.
    *   @param isFinal true in case of constant; false otherwise
    '''

    def emitSTATICFIELD(self, lexeme, in_, isFinal):
        # lexeme: String
        # in_: Type
        # isFinal: Boolean
        return self.jvm.emitSTATICFIELD(lexeme, self.getJVMType(in_), False)

    def emitGETSTATIC(self, lexeme, in_, frame):
        # lexeme: String
        # in_: Type
        # frame: Frame

        frame.push()
        return self.jvm.emitGETSTATIC(lexeme, self.getJVMType(in_))

    def emitPUTSTATIC(self, lexeme, in_, frame):
        # lexeme: String
        # in_: Type
        # frame: Frame

        frame.pop()
        return self.jvm.emitPUTSTATIC(lexeme, self.getJVMType(in_))

    def emitGETFIELD(self, lexeme, in_, frame):
        # lexeme: String
        # in_: Type
        # frame: Frame

        return self.jvm.emitGETFIELD(lexeme, self.getJVMType(in_))

    def emitPUTFIELD(self, lexeme, in_, frame):
        # lexeme: String
        # in_: Type
        # frame: Frame

        frame.pop()
        frame.pop()
        return self.jvm.emitPUTFIELD(lexeme, self.getJVMType(in_))

    ''' generate code to invoke a static method
    *   @param lexeme the qualified name of the method(i.e., class-name/method-name)
    *   @param in the type descriptor of the method.
    '''

    def emitINVOKESTATIC(self, lexeme, in_, frame):
        # lexeme: String
        # in_: Type
        # frame: Frame

        typ = in_
        list(map(lambda x: frame.pop(), typ.partype))
        if not type(typ.rettype) is VoidType:
            frame.push()
        return self.jvm.emitINVOKESTATIC(lexeme, self.getJVMType(in_))

    ''' generate code to invoke a special method
    *   @param lexeme the qualified name of the method(i.e., class-name/method-name)
    *   @param in the type descriptor of the method.
    '''

    def emitINVOKESPECIAL(self, frame, lexeme=None, in_=None):
        # lexeme: String
        # in_: Type
        # frame: Frame

        if lexeme == "java/lang/StringBuilder/<init>":
            return self.jvm.emitINVOKESPECIAL(lexeme, in_)
        else:
            if not lexeme is None and not in_ is None:
                typ = in_
                list(map(lambda x: frame.pop(), typ.partype))
                frame.pop()
                if not type(typ.rettype) is VoidType:
                    frame.push()
                return self.jvm.emitINVOKESPECIAL(lexeme, self.getJVMType(in_))
            elif lexeme is None and in_ is None:
                frame.pop()
                return self.jvm.emitINVOKESPECIAL()

    ''' generate code to invoke a virtual method
    * @param lexeme the qualified name of the method(i.e., class-name/method-name)
    * @param in the type descriptor of the method.
    '''

    def emitINVOKEVIRTUAL(self, lexeme, in_, frame):
        # lexeme: String
        # in_: Type
        # frame: Frame

        if lexeme == "java/lang/StringBuilder/append" or lexeme == "java/lang/StringBuilder/toString":
            return self.jvm.emitINVOKEVIRTUAL(lexeme, in_)
        else:
            typ = in_
            list(map(lambda x: frame.pop(), typ.partype))
            frame.pop()
            if not type(typ) is VoidType:
                frame.push()
            return self.jvm.emitINVOKEVIRTUAL(lexeme, self.getJVMType(in_))

    def emitNEW(self, lexeme, frame):
        
        frame.push()
        return self.jvm.emitNEW(lexeme)
    
    '''
    *   generate ineg, fneg.
    *   @param in the type of the operands.
    '''

    def emitNEGOP(self, in_, frame):
        # in_: Type
        # frame: Frame
        # ..., value -> ..., result

        frame.pop()
        if type(in_) is IntegerType:
            return self.jvm.emitINEG()
        elif type(in_) is FloatType:
            return self.jvm.emitFNEG()

    def emitNOT(self, in_, frame):
        # in_: Type
        # frame: Frame

        label1 = frame.getNewLabel()
        label2 = frame.getNewLabel()
        result = list()
        result.append(self.emitIFTRUE(label1, frame))
        result.append(self.emitPUSHICONST(1, frame))
        result.append(self.emitGOTO(label2, frame))
        result.append(self.emitLABEL(label1, frame))
        result.append(self.emitPUSHICONST(0, frame))
        result.append(self.emitLABEL(label2, frame))
        return ''.join(result)

    '''
    *   generate iadd, isub, fadd or fsub.
    *   @param lexeme the lexeme of the operator.
    *   @param in the type of the operands.
    '''

    def emitADDOP(self, lexeme, in_, frame):
        # lexeme: String
        # in_: Type
        # frame: Frame
        # ..., value1, value2 -> ..., result

        frame.pop()
        if lexeme == "+":
            if type(in_) is IntegerType:
                return self.jvm.emitIADD()
            elif type(in_) is FloatType:
                return self.jvm.emitFADD()
        elif lexeme == "-":
            if type(in_) is IntegerType:
                return self.jvm.emitISUB()
            elif type(in_) is FloatType:
                return self.jvm.emitFSUB()

    '''
    *   generate imul, idiv, fmul or fdiv.
    *   @param lexeme the lexeme of the operator.
    *   @param in the type of the operands.
    '''

    def emitMULOP(self, lexeme, in_, frame):
        # lexeme: String
        # in_: Type
        # frame: Frame
        # ..., value1, value2 -> ..., result

        frame.pop()
        if lexeme == "*":
            if type(in_) is IntegerType:
                return self.jvm.emitIMUL()
            elif type(in_) is FloatType:
                return self.jvm.emitFMUL()
        else:
            if type(in_) is IntegerType:
                return self.jvm.emitIDIV()
            elif type(in_) is FloatType:
                return self.jvm.emitFDIV()

    def emitMOD(self, frame):
        # frame: Frame
        frame.pop()
        return self.jvm.emitIREM()

    '''
    *   generate iand
    '''

    def emitANDOP(self, frame):
        # frame: Frame

        frame.pop()
        return self.jvm.emitIAND()

    '''
    *   generate ior
    '''

    def emitOROP(self, frame):
        # frame: Frame

        frame.pop()
        return self.jvm.emitIOR()

    def emitREOP(self, op, in_, frame):
        # op: String
        # in_: Type
        # frame: Frame
        # ..., value1, value2 -> ..., result

        result = list()
        labelF = frame.getNewLabel()
        labelO = frame.getNewLabel()

        frame.pop()
        frame.pop()
        if type(in_) == FloatType:
            result.append(self.jvm.emitFCMPL())
            if op == "==":
                result.append(self.jvm.emitIFNE(labelF))
            elif op == "!=":
                result.append(self.jvm.emitIFEQ(labelF))
            elif op == "<":
                result.append(self.jvm.emitIFGE(labelF))
            elif op == "<=":
                result.append(self.jvm.emitIFGT(labelF))
            elif op == ">":
                result.append(self.jvm.emitIFLE(labelF))
            elif op == ">=":
                result.append(self.jvm.emitIFLT(labelF))
        else:
            if op == "==":
                result.append(self.jvm.emitIFICMPNE(labelF))
            elif op == "!=":
                result.append(self.jvm.emitIFICMPEQ(labelF))
            elif op == "<":
                result.append(self.jvm.emitIFICMPGE(labelF))
            elif op == "<=":
                result.append(self.jvm.emitIFICMPGT(labelF))
            elif op == ">":
                result.append(self.jvm.emitIFICMPLE(labelF))
            elif op == ">=":
                result.append(self.jvm.emitIFICMPLT(labelF))
                
        result.append(self.emitPUSHICONST(1, frame))
        frame.pop()
        result.append(self.emitGOTO(labelO, frame))
        result.append(self.emitLABEL(labelF, frame))
        result.append(self.emitPUSHICONST(0, frame))
        result.append(self.emitLABEL(labelO, frame))
        return ''.join(result)

    def emitRELOP(self, op, in_, trueLabel, falseLabel, frame):
        # op: String
        # in_: Type
        # trueLabel: Int
        # falseLabel: Int
        # frame: Frame
        # ..., value1, value2 -> ..., result

        result = list()

        frame.pop()
        frame.pop()
        if op == ">":
            result.append(self.jvm.emitIFICMPLE(falseLabel))
            result.append(self.emitGOTO(trueLabel))
        elif op == ">=":
            result.append(self.jvm.emitIFICMPLT(falseLabel))
        elif op == "<":
            result.append(self.jvm.emitIFICMPGE(falseLabel))
        elif op == "<=":
            result.append(self.jvm.emitIFICMPGT(falseLabel))
        elif op == "!=":
            result.append(self.jvm.emitIFICMPEQ(falseLabel))
        elif op == "==":
            result.append(self.jvm.emitIFICMPNE(falseLabel))
        result.append(self.jvm.emitGOTO(trueLabel))
        return ''.join(result)

    '''   generate the method directive for a function.
    *   @param lexeme the qualified name of the method(i.e., class-name/method-name).
    *   @param in the type descriptor of the method.
    *   @param isStatic <code>true</code> if the method is static; <code>false</code> otherwise.
    '''

    def emitMETHOD(self, lexeme, in_, isStatic, frame):
        # lexeme: String
        # in_: Type
        # isStatic: Boolean
        # frame: Frame

        return self.jvm.emitMETHOD(lexeme, self.getJVMType(in_), isStatic)

    '''   generate the end directive for a function.
    '''

    def emitENDMETHOD(self, frame):
        # frame: Frame

        buffer = list()
        buffer.append(self.jvm.emitLIMITSTACK(frame.getMaxOpStackSize()))
        buffer.append(self.jvm.emitLIMITLOCAL(frame.getMaxIndex()))
        buffer.append(self.jvm.emitENDMETHOD())
        return ''.join(buffer)

    '''   generate code to initialize a local array variable.<p>
    *   @param index the index of the local variable.
    *   @param in the type of the local array variable.
    '''
    
    def emitANEWARRAY(self, typ, dim, frame):
        buffer = list()
        bracket = ""
        for i in range(0, dim - 1):
            bracket += "["
        if bracket == "":
            if type(typ.typ) == StringType:
                buffer.append(self.jvm.emitANEWARRAY(self.getFullType(typ.typ)))
            else:
                buffer.append(self.jvm.emitNEWARRAY(self.getFullType(typ.typ)))
        else:
            buffer.append(self.jvm.emitANEWARRAY(bracket + self.getJVMType(typ.typ)))
        return ''.join(buffer)

    '''   generate code to initialize local array variables.
    *   @param in the list of symbol entries corresponding to local array variable.    
    '''

    '''   generate code to jump to label if the value on top of operand stack is true.<p>
    *   ifgt label
    *   @param label the label where the execution continues if the value on top of stack is true.
    '''

    def emitIFTRUE(self, label, frame):
        # label: Int
        # frame: Frame

        frame.pop()
        return self.jvm.emitIFGT(label)

    '''
    *   generate code to jump to label if the value on top of operand stack is false.<p>
    *   ifle label
    *   @param label the label where the execution continues if the value on top of stack is false.
    '''

    def emitIFFALSE(self, label, frame):
        # label: Int
        # frame: Frame

        frame.pop()
        return self.jvm.emitIFLE(label)

    def emitIFICMPGT(self, label, frame):
        # label: Int
        # frame: Frame

        frame.pop()
        return self.jvm.emitIFICMPGT(label)

    def emitIFICMPLT(self, label, frame):
        # label: Int
        # frame: Frame

        frame.pop()
        return self.jvm.emitIFICMPLT(label)

    '''   generate code to duplicate the value on the top of the operand stack.<p>
    *   Stack:<p>
    *   Before: ...,value1<p>
    *   After:  ...,value1,value1<p>
    '''

    def emitDUP(self, frame):
        # frame: Frame

        frame.push()
        return self.jvm.emitDUP()

    def emitPOP(self, frame):
        # frame: Frame

        frame.pop()
        return self.jvm.emitPOP()

    '''   generate code to exchange an integer on top of stack to a floating-point number.
    '''

    def emitI2F(self, frame):
        # frame: Frame

        return self.jvm.emitI2F()

    ''' generate code to return.
    *   <ul>
    *   <li>ireturn if the type is IntegerType or BooleanType
    *   <li>freturn if the type is RealType
    *   <li>return if the type is null
    *   </ul>
    *   @param in the type of the returned expression.
    '''

    def emitRETURN(self, in_, frame):
        # in_: Type
        # frame: Frame

        if type(in_) is IntegerType:
            frame.pop()
            return self.jvm.emitIRETURN()
        elif type(in_) is FloatType:
            frame.pop()
            return self.jvm.emitFRETURN()
        elif type(in_) is BooleanType:
            frame.pop()
            return self.jvm.emitIRETURN()
        elif type(in_) is StringType:
            frame.pop()
        elif type(in_) is ArrayType:
            return self.jvm.emitARETURN()
        elif type(in_) is VoidType:
            return self.jvm.emitRETURN()

    ''' generate code that represents a label	
    *   @param label the label
    *   @return code Label<label>:
    '''

    def emitLABEL(self, label, frame):
        # label: Int
        # frame: Frame

        return self.jvm.emitLABEL(label)

    ''' generate code to jump to a label	
    *   @param label the label
    *   @return code goto Label<label>
    '''

    def emitGOTO(self, label, frame):
        # label: Int
        # frame: Frame

        return self.jvm.emitGOTO(label)

    ''' generate some starting directives for a class.<p>
    *   .source MPC.CLASSNAME.java<p>
    *   .class public MPC.CLASSNAME<p>
    *   .super java/lang/Object<p>
    '''

    def emitPROLOG(self, name, parent):
        # name: String
        # parent: String

        result = list()
        result.append(self.jvm.emitSOURCE(name + ".java"))
        result.append(self.jvm.emitCLASS("public " + name))
        result.append(self.jvm.emitSUPER(
            "java/land/Object" if parent == "" else parent))
        return ''.join(result)

    def emitLIMITSTACK(self, num):
        # num: Int

        return self.jvm.emitLIMITSTACK(num)

    def emitLIMITLOCAL(self, num):
        # num: Int

        return self.jvm.emitLIMITLOCAL(num)

    def emitEPILOG(self):
        file = open(self.filename, "w")
        file.write(''.join(self.buff))
        file.close()

    ''' print out the code to screen
    *   @param in the code to be printed out
    '''

    def printout(self, in_):
        # in_: String
        self.buff.append(in_)

    def clearBuff(self):
        self.buff.clear()
