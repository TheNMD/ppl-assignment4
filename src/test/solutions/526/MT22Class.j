.source MT22Class.java
.class public MT22Class
.super java.lang.Object
.field static a Ljava/lang/String;
.field static b Ljava/lang/String;
.field static c Ljava/lang/String;

.method public <clinit>()V
Label0:
	ldc  "abc" 
	putstatic MT22Class/a Ljava/lang/String;
	ldc  "def" 
	putstatic MT22Class/b Ljava/lang/String;
	new java/lang/StringBuilder
	dup
	invokespecial java/lang/StringBuilder/<init>()V
	ldc  "123" 
	invokevirtual java/lang/StringBuilder/append(java/lang/String;)Ljava/lang/StringBuilder;
	ldc  "abc" 
	invokevirtual java/lang/StringBuilder/append;(java/lang/String;)Ljava/lang/StringBuilder;
	invokevirtual java/lang/StringBuilder/toString;()Ljava/lang/String;
	putstatic MT22Class/c Ljava/lang/String;
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
