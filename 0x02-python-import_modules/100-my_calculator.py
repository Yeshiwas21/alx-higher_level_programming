#!/usr/bin/python3
if __name__ == "__main__":
    from Calculator import add, sub, mul, div
    import sys

    count = len(sys.argv) - 1
    if count != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    a = int(sys.argv[1])
    operator = sys.argv[2]
    b = int(sys.argv[3])

    result = None

    # Perform the calculation based on the operator
    operator_functions = {
        '+': add,
        '-': sub,
        '*': mul,
        '/': div
    }

    if operator in operator_functions:
        result = operator_functions[operator](a, b)
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

    print("{} {} {} = {}".format(a, operator, b, result))


