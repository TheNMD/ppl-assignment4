.source MT22Class.java
.class public MT22Class
.super java.lang.Object
.field static a [[Z
.field static b Z

.method public <clinit>()V
Label0:
	iconst_2
	anewarray [Z
	putstatic MT22Class/a [[Z
	getstatic MT22Class/a [[Z
	iconst_0
	iconst_2
	newarray boolean
	aastore
	getstatic MT22Class/a [[Z
	iconst_1
	iconst_2
	newarray boolean
	aastore
	getstatic MT22Class/a [[Z
	iconst_0
	aaload
	dup
	iconst_0
	iconst_1
	bastore
	dup
	iconst_1
	iconst_0
	bastore
	pop
	getstatic MT22Class/a [[Z
	iconst_1
	aaload
	dup
	iconst_0
	iconst_0
	bastore
	dup
	iconst_1
	iconst_1
	bastore
	pop
	getstatic MT22Class/a [[Z
	iconst_0
	aaload
	iconst_1
	baload
	putstatic MT22Class/b Z
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

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	return
Label1:
.limit stack 0
.limit locals 1
.end method
