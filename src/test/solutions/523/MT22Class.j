.source MT22Class.java
.class public MT22Class
.super java.lang.Object
.field static a Z
.field static b Z
.field static c Z

.method public <clinit>()V
Label0:
	iconst_0
	putstatic MT22Class/a Z
	iconst_1
	putstatic MT22Class/b Z
	getstatic MT22Class/a Z
	getstatic MT22Class/b Z
	if_icmpeq Label2
	iconst_1
	goto Label3
Label2:
	iconst_0
Label3:
	getstatic MT22Class/a Z
	getstatic MT22Class/b Z
	if_icmpne Label4
	iconst_1
	goto Label5
Label4:
	iconst_0
Label5:
	if_icmpne Label6
	iconst_1
	goto Label7
Label6:
	iconst_0
Label7:
	putstatic MT22Class/c Z
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

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
Label1:
	return
.limit stack 0
.limit locals 1
.end method
