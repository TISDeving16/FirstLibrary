str="World"
b=2
c=3
def func():
    global b,c
    a=b+c
    return a
print("Hello：{0} return:{1}".format(str,func()))

      