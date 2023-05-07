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

.method public static func(IF)V
.var 0 is a I from Label0 to Label1
.var 1 is b F from Label0 to Label1
.var 2 is o Ljava/lang/String; from Label0 to Label1
.var 3 is l Ljava/lang/String; from Label0 to Label1
.var 4 is c [I from Label0 to Label1
.var 5 is m I from Label0 to Label1
Label0:
	iconst_2
	newarray int
	astore 4
	aload 4
	iconst_0
	iconst_1
	iastore
	aload 4
	iconst_1
	iconst_2
	iastore
.var 6 is d I from Label2 to Label3
.var 7 is c Z from Label2 to Label3
Label2:
	aload 4
	iconst_0
	iaload
	istore 6
	iconst_1
	istore 7
.var 8 is f Ljava/lang/String; from Label4 to Label5
.var 9 is g I from Label4 to Label5
.var 10 is e [I from Label4 to Label5
Label4:
	iload 6
	istore 9
	iconst_2
	newarray int
	astore 10
	aload 10
	iconst_0
	iconst_1
	iastore
	aload 10
	iconst_1
	iconst_2
	iastore
.var 11 is x Z from Label6 to Label7
Label6:
	iload 7
	istore 11
Label7:
Label5:
Label3:
	return
Label1:
.limit stack 3
.limit locals 12
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	return
Label1:
.limit stack 0
.limit locals 1
.end method
