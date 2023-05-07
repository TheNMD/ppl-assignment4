.source MT22Class.java
.class public MT22Class
.super java.lang.Object
.field static x [I

.method public <clinit>()V
Label0:
	iconst_2
	newarray int
	putstatic MT22Class/x [I
	getstatic MT22Class/x [I
	iconst_0
	iconst_1
	iastore
	getstatic MT22Class/x [I
	iconst_1
	iconst_2
	iastore
Label1:
	return
.limit stack 3
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
.var 2 is z [F from Label0 to Label1
.var 3 is y F from Label0 to Label1
Label0:
	iconst_3
	newarray float
	astore_2
	aload_2
	iconst_0
	ldc 1.0
	fastore
	aload_2
	iconst_1
	ldc 2.0
	fastore
	aload_2
	iconst_2
	ldc 3.0
	fastore
	getstatic MT22Class/x [I
	iconst_0
	iaload
	i2f
	fstore_3
	return
Label1:
.limit stack 3
.limit locals 4
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	return
Label1:
.limit stack 0
.limit locals 1
.end method
