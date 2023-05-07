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
.var 2 is c [[[Ljava/lang/String; from Label0 to Label1
Label0:
	iconst_2
	anewarray [[Ljava/lang/String;
	astore_2
	aload_2
	iconst_0
	iconst_2
	anewarray [Ljava/lang/String;
	aastore
	aload_2
	iconst_0
	aaload
	dup
	iconst_0
	iconst_2
	anewarray java/lang/String
	aastore
	dup
	iconst_1
	iconst_2
	anewarray java/lang/String
	aastore
	pop
	aload_2
	iconst_1
	iconst_2
	anewarray [Ljava/lang/String;
	aastore
	aload_2
	iconst_1
	aaload
	dup
	iconst_0
	iconst_2
	anewarray java/lang/String
	aastore
	dup
	iconst_1
	iconst_2
	anewarray java/lang/String
	aastore
	pop
	aload_2
	iconst_0
	aaload
	dup
	iconst_0
	aaload
	dup
	iconst_0
	ldc  "10" 
	aastore
	dup
	iconst_1
	ldc  "20" 
	aastore
	pop
	dup
	iconst_1
	aaload
	dup
	iconst_0
	ldc  "30" 
	aastore
	dup
	iconst_1
	ldc  "40" 
	aastore
	pop
	pop
	aload_2
	iconst_1
	aaload
	dup
	iconst_0
	aaload
	dup
	iconst_0
	ldc  "50" 
	aastore
	dup
	iconst_1
	ldc  "60" 
	aastore
	pop
	dup
	iconst_1
	aaload
	dup
	iconst_0
	ldc  "70" 
	aastore
	dup
	iconst_1
	ldc  "90" 
	aastore
	pop
	pop
	return
Label1:
.limit stack 5
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
