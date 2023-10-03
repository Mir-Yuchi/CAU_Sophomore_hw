import numpy as np
import matplotlib.pyplot as plt


def f(x):
    # the function to be integrated
    return np.exp(-x ** 2)


def simpson(a, b, n):
    # a, b: the interval of integration
    h = (b - a) / n
    x = np.linspace(a, b, n + 1)
    y = f(x)
    s = y[0] + y[-1]
    for i in range(1, n, 2):
        s += 4 * y[i]
    for i in range(2, n - 1, 2):
        s += 2 * y[i]
    return s * h / 3


def main():
    # get input
    a = float(input("Enter a: "))
    b = float(input("Enter b: "))
    n = int(input("Enter n: "))
    print("Result: ", simpson(a, b, n))

    # show the graph
    x = np.linspace(a, b, 100)
    y = f(x)
    plt.plot(x, y)
    plt.show()


if __name__ == "__main__":
    main()
