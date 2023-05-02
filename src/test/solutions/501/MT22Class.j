.source MT22Class.java
.class public MT22Class
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is a I from Label0 to Label1
.var 1 is b F from Label0 to Label1
.var 2 is b1 F from Label0 to Label1
.var 3 is c Z from Label0 to Label1
.var 4 is c1 Z from Label0 to Label1
.var 5 is d Ljava/lang/String; from Label0 to Label1
Label0:
	ldc 32768
	istore_0
	ldc 13.2
	fstore_1
	bipush 13
	i2f
	fstore_2
	iconst_1
	istore_3
	iconst_0
	istore 4
	ldc  "abc" 
	astore 5
Label1:
	return
.limit stack 1
.limit locals 6
.end method
