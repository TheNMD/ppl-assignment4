.source MT22Class.java
.class public MT22Class
.super java.lang.Object
.field static a F
.field static b I
.field static c F

.method public <clinit>()V
Label0:
	ldc 2.1
	putstatic MT22Class/a F
	iconst_3
	putstatic MT22Class/b I
	getstatic MT22Class/a F
	getstatic MT22Class/b I
	getstatic MT22Class/a F
	pop
	i2f
	getstatic MT22Class/a F
	fmul
	getstatic MT22Class/a F
	getstatic MT22Class/b I
	i2f
	fadd
	fdiv
	fsub
	putstatic MT22Class/c F
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
Label1:
	return
.limit stack 0
.limit locals 1
.end method
