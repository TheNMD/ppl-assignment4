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
.var 2 is c [Ljava/lang/String; from Label0 to Label1
.var 3 is d Ljava/lang/String; from Label0 to Label1
Label0:
	iconst_3
	anewarray java/lang/String
	astore_2
	aload_2
	iconst_0
	ldc  "1" 
	aastore
	aload_2
	iconst_1
	ldc  "2" 
	aastore
	aload_2
	iconst_2
	ldc  "3" 
	aastore
	aload_2
	iconst_2
	aaload
	astore_3
Label1:
	return
.limit stack 3
.limit locals 4
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
Label1:
	return
.limit stack 0
.limit locals 1
.end method
