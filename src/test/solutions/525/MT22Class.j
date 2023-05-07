.source MT22Class.java
.class public MT22Class
.super java.lang.Object
.field static a F
.field static b I
.field static c [[I
.field static d Z

.method public <clinit>()V
Label0:
	iconst_2
	i2f
	putstatic MT22Class/a F
	iconst_3
	putstatic MT22Class/b I
	iconst_3
	anewarray [I
	putstatic MT22Class/c [[I
	getstatic MT22Class/c [[I
	iconst_0
	iconst_2
	newarray int
	aastore
	getstatic MT22Class/c [[I
	iconst_1
	iconst_2
	newarray int
	aastore
	getstatic MT22Class/c [[I
	iconst_2
	iconst_2
	newarray int
	aastore
	getstatic MT22Class/c [[I
	iconst_0
	aaload
	dup
	iconst_0
	iconst_1
	iastore
	dup
	iconst_1
	iconst_2
	iastore
	pop
	getstatic MT22Class/c [[I
	iconst_1
	aaload
	dup
	iconst_0
	iconst_3
	iastore
	dup
	iconst_1
	iconst_4
	iastore
	pop
	getstatic MT22Class/c [[I
	iconst_2
	aaload
	dup
	iconst_0
	iconst_5
	iastore
	dup
	iconst_1
	bipush 6
	iastore
	pop
	getstatic MT22Class/a F
	getstatic MT22Class/c [[I
	iconst_0
	aaload
	iconst_0
	iaload
	i2f
	fcmpl
	ifle Label2
	iconst_1
	goto Label3
Label2:
	iconst_0
Label3:
	putstatic MT22Class/d Z
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
