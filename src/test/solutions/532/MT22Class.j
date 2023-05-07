.source MT22Class.java
.class public MT22Class
.super java.lang.Object
.field static c Ljava/lang/String;

.method public <clinit>()V
Label0:
	ldc  "true" 
	putstatic MT22Class/c Ljava/lang/String;
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
.var 2 is c Z from Label0 to Label1
.var 3 is d Z from Label0 to Label1
.var 4 is x Ljava/lang/String; from Label0 to Label1
.var 5 is y Ljava/lang/String; from Label0 to Label1
.var 6 is z Ljava/lang/String; from Label0 to Label1
Label0:
	iconst_0
	istore_2
	iconst_1
	istore_3
.var 7 is a I from Label2 to Label3
.var 8 is b F from Label2 to Label3
Label2:
	iconst_2
	istore 7
	ldc 3.5
	fstore 8
.var 9 is x Z from Label4 to Label5
.var 10 is d Z from Label4 to Label5
Label4:
	iload_2
	istore 9
	iconst_1
	istore 10
Label5:
Label3:
Label1:
	return
.limit stack 1
.limit locals 11
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
Label1:
	return
.limit stack 0
.limit locals 1
.end method
