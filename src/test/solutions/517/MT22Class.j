.source MT22Class.java
.class public MT22Class
.super java.lang.Object
.field static a F

.method public <clinit>()V
Label0:
	iconst_1
	ldc 2.2
	pop
	i2f
	ldc 2.2
	fadd
	putstatic MT22Class/a F
Label1:
	return
.limit stack 2
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
