# VERSION 1.0

#!/usr/bin/env python3
import sys
import math


class RPNError(Exception):
    pass


def eval_rpn(tokens):
    stack = []
    mem = [0.0] * 10

    def pop():
        if not stack:
            raise RPNError("Pila insuficiente")
        return stack.pop()

    def push(x):
        stack.append(float(x))

    for t in tokens:
        # NÚMEROS
        try:
            push(float(t))
            continue
        except ValueError:
            pass

        # CONSTANTES
        if t == "p":
            push(math.pi)
        elif t == "e":
            push(math.e)
        elif t == "j":
            push((1 + 5**0.5) / 2)

        # OPERADORES
        elif t in ("+", "-", "*", "/"):
            b, a = pop(), pop()
            if t == "+":
                push(a + b)
            elif t == "-":
                push(a - b)
            elif t == "*":
                push(a * b)
            elif t == "/":
                if b == 0:
                    raise RPNError("División por cero")
                push(a / b)

        # FUNCIONES
        elif t == "sqrt":
            a = pop()
            if a < 0:
                raise RPNError("Raíz negativa")
            push(math.sqrt(a))
        elif t == "log":
            a = pop()
            if a <= 0:
                raise RPNError("Log inválido")
            push(math.log10(a))
        elif t == "ln":
            a = pop()
            if a <= 0:
                raise RPNError("Ln inválido")
            push(math.log(a))
        elif t == "ex":
            push(math.exp(pop()))
        elif t == "10x":
            push(10 ** pop())
        elif t == "1/x":
            a = pop()
            if a == 0:
                raise RPNError("División por cero")
            push(1 / a)
        elif t == "yx":
            b, a = pop(), pop()
            push(a**b)

        # TRIG (grados)
        elif t in ("sin", "cos", "tg"):
            a = math.radians(pop())
            if t == "sin":
                push(math.sin(a))
            elif t == "cos":
                push(math.cos(a))
            elif t == "tg":
                push(math.tan(a))
        elif t in ("asin", "acos", "atg"):
            a = pop()
            if t == "asin":
                push(math.degrees(math.asin(a)))
            elif t == "acos":
                push(math.degrees(math.acos(a)))
            elif t == "atg":
                push(math.degrees(math.atan(a)))

        # PILA
        elif t == "dup":
            stack.append(stack[-1])
        elif t == "swap":
            if len(stack) < 2:
                raise RPNError("Pila insuficiente")
            stack[-1], stack[-2] = stack[-2], stack[-1]
        elif t == "drop":
            pop()
        elif t == "clear":
            stack.clear()

        # CHS
        elif t == "chs":
            stack.append(-pop())

        # MEMORIA
        elif t == "sto":
            idx = int(pop())
            if not 0 <= idx <= 9:
                raise RPNError("Memoria inválida")
            mem[idx] = pop()
        elif t == "rcl":
            idx = int(pop())
            if not 0 <= idx <= 9:
                raise RPNError("Memoria inválida")
            push(mem[idx])

        # ÍNDICES 00–09
        elif t.isdigit() and len(t) == 2:
            push(int(t))

        else:
            raise RPNError(f"Token inválido: {t}")

    if len(stack) != 1:
        raise RPNError("La pila final debe tener exactamente un valor")

    return stack[0]


def main():
    try:
        if len(sys.argv) > 1:
            expr = " ".join(sys.argv[1:])
        else:
            expr = input("RPN> ")

        tokens = expr.strip().split()
        result = eval_rpn(tokens)
        print(result)

    except RPNError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Error inesperado: {e}")


if __name__ == "__main__":
    main()
