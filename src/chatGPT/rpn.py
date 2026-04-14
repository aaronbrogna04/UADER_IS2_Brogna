#!/usr/bin/env python3
"""
Calculadora RPN (Reverse Polish Notation).
Soporta operaciones básicas, funciones matemáticas,
trigonométricas, memorias y manejo de errores.
"""
import sys, math

class RPNError(Exception):
    pass

def rpn_eval(expr):
    stack = []
    mem = [0.0]*10
    tokens = expr.split()

    def pop():
        if not stack:
            raise RPNError("pila insuficiente")
        return stack.pop()

    for t in tokens:
        t = t.lower()
        try:
            stack.append(float(t))
            continue
        except ValueError:
            pass
        if t == "p": stack.append(math.pi)
        elif t == "e": stack.append(math.e)
        elif t == "j": stack.append((1+math.sqrt(5))/2)
        elif t in "+-*/":
            b, a = pop(), pop()
            if t == "+": stack.append(a+b)
            elif t == "-": stack.append(a-b)
            elif t == "*": stack.append(a*b)
            elif t == "/":
                if b == 0: raise RPNError("division por cero")
                stack.append(a/b)
        elif t == "dup": stack.append(stack[-1])
        elif t == "swap":
            a, b = pop(), pop()
            stack.extend([a,b])
        elif t == "drop": pop()
        elif t == "clear": stack.clear()
        elif t == "sqrt":
            x = pop()
            if x < 0: raise RPNError("raíz de número negativo")
            stack.append(math.sqrt(x))
        elif t == "log": stack.append(math.log10(pop()))
        elif t == "ln": stack.append(math.log(pop()))
        elif t == "ex": stack.append(math.exp(pop()))
        elif t == "10x": stack.append(10**pop())
        elif t == "1/x":
            x = pop()
            if x == 0: raise RPNError("division por cero")
            stack.append(1/x)
        elif t == "chs": stack.append(-pop())
        elif t == "sin": stack.append(math.sin(math.radians(pop())))
        elif t == "cos": stack.append(math.cos(math.radians(pop())))
        elif t == "tg": stack.append(math.tan(math.radians(pop())))
        elif t == "asin": stack.append(math.degrees(math.asin(pop())))
        elif t == "acos": stack.append(math.degrees(math.acos(pop())))
        elif t == "atg": stack.append(math.degrees(math.atan(pop())))
        elif t == "yx":
            b, a = pop(), pop()
            stack.append(a**b)
        elif t == "sto":
            idx = int(pop())
            mem[idx] = pop()
        elif t == "rcl":
            idx = int(pop())
            stack.append(mem[idx])
        else:
            raise RPNError(f"token inválido: {t}")

    if len(stack) != 1:
        raise RPNError("la pila debe quedar con exactamente un valor")
    return stack[0]

def main():
    try:
        expr = " ".join(sys.argv[1:]) if len(sys.argv)>1 else input("RPN> ")
        result = rpn_eval(expr)
        print(f"{result:g}")
    except RPNError as e:
        print("Error:", e)

if __name__ == "__main__":
    main()