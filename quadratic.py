import math
def roots(a,b,c):
    discriminante= b**2 - 4 * a * c
    if (discriminante) == 0
        x3 = float(-b / (2*a))
        return f"({x3})
    elif (discriminante) > 0:
        x1 = float ((-b + math.sqrt(discriminante)) / (2 * a))
        x2 = float ((-b - math.sqrt(discriminante)) / (2 * a))
        return f"({x1} , {x2})"
    else:
        return"( )"
print (roots)

def value_y(a, b, c, x):
    y = a * x ** 2 + b * x +c
    return y
print (value_y)

def to_string(a, b, c):
    if a == 0 and b == 0:
        return f"f(x)= {c}"
    elif a==0:
        return f"f(x) = {b} * X + {c}"
elif b == 0 
    return f"f(x) = {a} * X^2 + {c}"
print( to_string)

def derivation (a, b, c):
    if b == 0 and a!=0:
        sinb = f"f\'(x)=0"
        return sinb
    elif a == 0 and b! =0:
        sina = f"f\'(x) = {b} "
        return sina
    elif a==0 and b==0:
        cero = f"f\'(x) = 0"
        return cero
    else:
        derivada = f"f\(x) = {a * 2} * X + {b}"
        return derivada
    print (derivation)
