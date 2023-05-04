.source MT22Class.java
.class public MT22Class
.super java.lang.Object
.field static a [[[I

.method public <clinit>()V
Label0:
	iconst_3
	anewarray [[I
	putstatic MT22Class/a [[[I
	getstatic MT22Class/a [[[I
	iconst_0
	iconst_3
	anewarray [I
	aastore
	getstatic MT22Class/a [[[I
	iconst_0
	aaload
	dup
	iconst_0
	iconst_2
	newarray int
	aastore
	dup
	iconst_1
	iconst_2
	newarray int
	aastore
	pop
	getstatic MT22Class/a [[[I
	iconst_1
	iconst_3
	anewarray [I
	aastore
	getstatic MT22Class/a [[[I
	iconst_1
	aaload
	dup
	iconst_0
	iconst_2
	newarray int
	aastore
	dup
	iconst_1
	iconst_2
	newarray int
	aastore
	pop
	getstatic MT22Class/a [[[I
	iconst_2
	iconst_3
	anewarray [I
	aastore
	getstatic MT22Class/a [[[I
	iconst_2
	aaload
	dup
	iconst_0
	iconst_2
	newarray int
	aastore
	dup
	iconst_1
	iconst_2
	newarray int
	aastore
	pop
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
