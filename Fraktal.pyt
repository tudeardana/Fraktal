import numpy as np
import matplotlib.pyplot as plt
from concurrent.futures import ThreadPoolExecutor

def mandelbrot(c, max_iter=256):
    z = 0
    n = 0
    while abs(z) <= 2 and n < max_iter:
        z = z*z + c
        n += 1
    return n

def compute_fractal(width, height, x_min, x_max, y_min, y_max, max_iter=256):
    real = np.linspace(x_min, x_max, width)
    imag = np.linspace(y_min, y_max, height)
    fractal = np.zeros((height, width))
    
    def calculate_pixel(x, y):
        c = complex(real[x], imag[y])
        return mandelbrot(c, max_iter)
    
    with ThreadPoolExecutor() as executor:
        for x in range(width):
            results = list(executor.map(lambda y: calculate_pixel(x, y), range(height)))
            fractal[:, x] = results
    return fractal

def plot_fractal(fractal, colormap='inferno'):
    plt.imshow(fractal, cmap=colormap, extent=(-2.0, 1.0, -1.5, 1.5))
    plt.colorbar()
    plt.title("Mandelbrot Fractal Set")
    plt.show()

if __name__ == "__main__":
    width, height = 800, 600
    x_min, x_max = -2.0, 1.0
    y_min, y_max = -1.5, 1.5
    fractal = compute_fractal(width, height, x_min, x_max, y_min, y_max)
    plot_fractal(fractal)
