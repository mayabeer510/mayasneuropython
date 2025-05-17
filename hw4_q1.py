import numpy as np
import matplotlib.pyplot as plt

def mandel(
    n: int,
    thresh: float = 50.0,
    xlims: np.ndarray = np.array([-2, 1]),
    nx: int = 1500,
    ylims: np.ndarray = np.array([-1.5, 1.5]),
    ny: int = 1500,
) -> np.ndarray:
    
    """Computes the Mandelbrot fractal on some given set of numbers."""

    x = np.linspace(xlims[0], xlims[1], nx)
    y = np.linspace(ylims[0], ylims[1], ny)
    X, Y = np.meshgrid(x, y)
    C = X + 1j * Y

    Z = np.zeros_like(C)
    mask = np.ones_like(C, dtype=bool)

    for _ in range(n):
        Z = Z**2 + C
        mask &= np.abs(Z) < thresh

    img = mask.astype(int)
    return img
