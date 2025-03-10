username = "Codewithanvesha"

def func():
    
    print(username)

print(username)
func()


x = 89
# def func2(y):
#     z = x + y
#     return z

# result = func2(1)
# print(result)

# def func3():
#     global x
#     x = 12
    
# func3()
# print(x)



def f1():
    x = 86
    def f2():
        print(x)
    return f2
myResult = f1()
myResult()


def anvesha(num):
    def actual(x):
        return x ** num
    return actual



f = anvesha(2)
g = anvesha(3)

print(f(3))
print(g(3))