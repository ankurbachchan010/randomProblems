count = 2
a = 0
b = 1
def fibonacci(a, b, integer, count):
    c = a+b
    count += 1
    if count == integer:
        print(c)
    else:
        a = b
        b = c
        fibonacci(a,b,integer, count)

fibonacci(a,b,10, count)