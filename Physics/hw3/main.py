import numpy as np
import matplotlib.pyplot as plt

R = float(input("Enter the radius of the circle: "))
f = float(input("Enter the frequency of the circle: "))
x0 = float(input("Enter the x-coordinate of the point: "))
y0 = float(input("Enter the y-coordinate of the point: "))

t = np.linspace(0, 2 * np.pi, 1000)

x = R * np.cos(2 * np.pi * f * t)
y = R * np.sin(2 * np.pi * f * t)


def main():
    plt.figure()
    plt.plot(x, y)
    plt.plot(x0, y0, 'ro')
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("Trajectory of a point at a rotating circle")
    plt.show()


if __name__ == "__main__":
    main()
