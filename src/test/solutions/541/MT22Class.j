.source MT22Class.java
.class public MT22Class
.super java.lang.Object

.method public <clinit>()V
Label0:
Label1:
	return
.limit stack 0
.limit locals 0
.end method

.method public <init>()V
.var 0 is this LMT22Class; from Label0 to Label1
Label0:
	aload_0
	invokespecial java/lang/Object/<init>()V
Label1:
	return
.limit stack 1
.limit locals 1
.end method

.method public static func(IF)I
.var 0 is a I from Label0 to Label1
.var 1 is b F from Label0 to Label1
Label0:
.var 2 is i I from Label2 to Label4
Label2:
	iconst_0
	istore_2
	goto Label5
Label3:
	iload_2
	iconst_1
	iadd
	istore_2
Label5:
	iload_2
	iconst_2
	if_icmpge Label6
	iconst_1
	goto Label7
Label6:
	iconst_0
Label7:
	ifle Label4
Label8:
	iconst_1
	iconst_2
	if_icmple Label10
	iconst_1
	goto Label11
Label10:
	iconst_0
Label11:
	ifle Label12
	iconst_3
	ireturn
	goto Label13
Label12:
	iconst_5
	ireturn
Label13:
Label9:
	goto Label3
Label4:
	iconst_2
	ireturn
Label1:
.limit stack 2
.limit locals 3
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	return
Label1:
.limit stack 0
.limit locals 1
.end method
