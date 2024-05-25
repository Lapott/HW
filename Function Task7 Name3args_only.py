def foo(*, var1, var2=None, var3=None):
    print("var1 =", var1)
    if var2 != None:
        print("var2 =", var2)
    if var3 != None:
        print("var3 =", var3)
    return
foo(var1=32)
foo(var1=32, var3="test")