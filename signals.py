import numpy as np
import matplotlib.pyplot as plt
import os

def plot_iq_signal(A=1, f=5, fs=1000, duration=1, phi=0, save=False):
    num_samples = int(fs * duration)
    t = np.linspace(0, duration, num_samples)

    # define I/Q data 
    I = A * np.cos(2 * np.pi * f * (t + phi)) # In-phase - real
    Q = A * np.sin(2 * np.pi * f * (t + phi)) # Quadrature - imaginary

    # IQ
    IQ = I + 1j*Q
    # Plot
    plt.figure(figsize=(12,4))

    plt.subplot(1,2,1)
    plt.plot(t, I, label="I")
    plt.plot(t, Q, label="Q")
    plt.title("I and Q vs Time")
    plt.xlabel("Time (s)")
    plt.legend()
    plt.grid(True)

    plt.subplot(1,2,2)
    plt.plot(I, Q)
    plt.title("I/Q Constellation")
    plt.xlabel("I")
    plt.ylabel("Q")
    plt.grid(True)

    if save:
        os.makedirs("output", exist_ok=True)
        filename = f"output/iq_plot_f{f}Hz.png"
        plt.savefig(filename)
        print(f"Plot saved to {filename}")

    plt.show()
