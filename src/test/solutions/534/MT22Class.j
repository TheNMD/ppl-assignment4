.source MT22Class.java
.class public MT22Class
.super java.lang.Object
.field static c I

.method public <clinit>()V
Label0:
	iconst_3
	putstatic MT22Class/c I
Label1:
	return
.limit stack 1
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
.var 2 is x Ljava/lang/String; from Label0 to Label1
.var 3 is y Ljava/lang/String; from Label0 to Label1
.var 4 is z Ljava/lang/String; from Label0 to Label1
.var 5 is d F from Label0 to Label1
.var 6 is f I from Label0 to Label1
.var 7 is d Ljava/lang/String; from Label0 to Label1
Label0:
.var 8 is x F from Label2 to Label3
.var 9 is y F from Label2 to Label3
.var 10 is z F from Label2 to Label3
.var 11 is d F from Label2 to Label3
Label2:
Label4:
	iconst_2
	i2f
	fstore 11
Label5:
Label3:
	return
Label1:
.limit stack 1
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
