.source MT22Class.java
.class public MT22Class
.super java.lang.Object
.field static a I
.field static b F
.field static b1 F
.field static c Z
.field static c1 Z
.field static d Ljava/lang/String;

.method public <clinit>()V
Label0:
	iconst_2
	putstatic MT22Class/a I
	ldc 3.3
	putstatic MT22Class/b F
	iconst_3
	i2f
	putstatic MT22Class/b1 F
	iconst_1
	putstatic MT22Class/c Z
	iconst_0
	putstatic MT22Class/c1 Z
	ldc  "123" 
	putstatic MT22Class/d Ljava/lang/String;
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

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	return
Label1:
.limit stack 0
.limit locals 1
.end method
