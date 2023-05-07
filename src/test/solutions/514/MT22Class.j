.source MT22Class.java
.class public MT22Class
.super java.lang.Object
.field static a [[[Ljava/lang/String;
.field static b Ljava/lang/String;

.method public <clinit>()V
Label0:
	iconst_2
	anewarray [[Ljava/lang/String;
	putstatic MT22Class/a [[[Ljava/lang/String;
	getstatic MT22Class/a [[[Ljava/lang/String;
	iconst_0
	iconst_2
	anewarray [Ljava/lang/String;
	aastore
	getstatic MT22Class/a [[[Ljava/lang/String;
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
	getstatic MT22Class/a [[[Ljava/lang/String;
	iconst_1
	iconst_2
	anewarray [Ljava/lang/String;
	aastore
	getstatic MT22Class/a [[[Ljava/lang/String;
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
	getstatic MT22Class/a [[[Ljava/lang/String;
	iconst_0
	aaload
	dup
	iconst_0
	aaload
	dup
	iconst_0
	ldc  "true" 
	aastore
	dup
	iconst_1
	ldc  "false" 
	aastore
	pop
	dup
	iconst_1
	aaload
	dup
	iconst_0
	ldc  "false" 
	aastore
	dup
	iconst_1
	ldc  "true" 
	aastore
	pop
	pop
	getstatic MT22Class/a [[[Ljava/lang/String;
	iconst_1
	aaload
	dup
	iconst_0
	aaload
	dup
	iconst_0
	ldc  "false" 
	aastore
	dup
	iconst_1
	ldc  "true" 
	aastore
	pop
	dup
	iconst_1
	aaload
	dup
	iconst_0
	ldc  "true" 
	aastore
	dup
	iconst_1
	ldc  "false" 
	aastore
	pop
	pop
	getstatic MT22Class/a [[[Ljava/lang/String;
	iconst_0
	aaload
	iconst_0
	aaload
	iconst_0
	aaload
	putstatic MT22Class/b Ljava/lang/String;
Label1:
	return
.limit stack 5
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

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	return
Label1:
.limit stack 0
.limit locals 1
.end method
