.source MT22Class.java
.class public MT22Class
.super java.lang.Object
.field static a I
.field static b I
.field static c Z

.method public <clinit>()V
Label0:
	iconst_2
	putstatic MT22Class/a I
	iconst_3
	putstatic MT22Class/b I
	getstatic MT22Class/a I
	getstatic MT22Class/b I
	if_icmpeq Label2
	iconst_1
	goto Label3
Label2:
	iconst_0
Label3:
	putstatic MT22Class/c Z
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
