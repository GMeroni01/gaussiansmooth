import numpy as np
from scipy import signal
import matplotlib.pyplot as plt


def fdata(x, L):
    
    A = L / 10.0

    return (2 * np.sin(2 * np.pi * x / L) + x * (L - x) ** 2 / L**3 * np.cos(x)
        + 5 * x * (L - x) / L**2 + A / 2 + 0.1 * A * np.sin(13 * np.pi * x / L))


def gaussian_smooth(data, sigma):
    
    window_size = int(5 * sigma)

    gauss = signal.windows.gaussian(window_size, sigma)
    gauss /= np.sum(gauss)

    smooth = signal.convolve(data, gauss, mode="same")

    return smooth


def generate_noisy_data(N=2048, L=50, noise_level=0.5):
    
    x = np.linspace(0, L, N, endpoint=False)

    original = fdata(x, L)
    noisy = original + noise_level * np.random.randn(N)

    return x, original, noisy

def plot_smoothing(x, original, noisy, smoothed):

    plt.figure(figsize=(8,5))
    plt.plot(x, noisy, alpha=0.4, label="Noisy")
    plt.plot(x, original, label="Original")
    plt.plot(x, smoothed, label="Smoothed")
    plt.xlabel("x")
    plt.ylabel("Data")
    plt.title("Gaussian smoothing")
    plt.legend()
    plt.grid()
    plt.show()