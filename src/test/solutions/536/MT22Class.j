.source MT22Class.java
.class public MT22Class
.super java.lang.Object
.field static c [[Ljava/lang/String;

.method public <clinit>()V
Label0:
	iconst_2
	anewarray [Ljava/lang/String;
	putstatic MT22Class/c [[Ljava/lang/String;
	getstatic MT22Class/c [[Ljava/lang/String;
	iconst_0
	iconst_2
	anewarray java/lang/String
	aastore
	getstatic MT22Class/c [[Ljava/lang/String;
	iconst_1
	iconst_2
	anewarray java/lang/String
	aastore
	getstatic MT22Class/c [[Ljava/lang/String;
	iconst_0
	aaload
	dup
	iconst_0
	ldc  "1" 
	aastore
	dup
	iconst_1
	ldc  "2" 
	aastore
	pop
	getstatic MT22Class/c [[Ljava/lang/String;
	iconst_1
	aaload
	dup
	iconst_0
	ldc  "3" 
	aastore
	dup
	iconst_1
	ldc  "4" 
	aastore
	pop
Label1:
	return
.limit stack 4
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
.var 2 is d [Ljava/lang/String; from Label0 to Label1
Label0:
	iconst_2
	anewarray java/lang/String
	astore_2
	aload_2
	iconst_0
	ldc  "123" 
	aastore
	aload_2
	iconst_1
	ldc  "456" 
	aastore
	getstatic MT22Class/c [[Ljava/lang/String;
	iconst_1
	aaload
	iconst_1
	aload_2
	iconst_1
	aaload
	aastore
	return
Label1:
.limit stack 4
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
