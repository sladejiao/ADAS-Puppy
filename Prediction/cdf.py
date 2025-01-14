import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

def plot_normal_distribution(mean, variance, x_value):
    std_dev = np.sqrt(variance)
    x = np.linspace(mean - 4*std_dev, mean + 4*std_dev, 1000)
    
    # PDF
    pdf = norm.pdf(x, mean, std_dev)
    
    # CDF
    cdf = norm.cdf(x, mean, std_dev)
    
    # CDF value at x_value
    cdf_value = norm.cdf(x_value, mean, std_dev)
    
    # Plotting
    plt.figure(figsize=(12, 6))
    
    # Plot PDF
    plt.subplot(1, 2, 1)
    plt.plot(x, pdf, label='PDF', color='blue')
    plt.axvline(x=x_value, color='red', linestyle='--', label=f'x = {x_value}')
    plt.title('Probability Density Function')
    plt.xlabel('x')
    plt.ylabel('Density')
    plt.grid(True)
    plt.legend()
    plt.text(mean + 3*std_dev, max(pdf)*0.7, f'Mean = {mean}\nVariance = {variance}\nx = {x_value}', fontsize=10, bbox=dict(facecolor='white', alpha=0.5))

    # Plot CDF
    plt.subplot(1, 2, 2)
    plt.plot(x, cdf, label='CDF', color='green')
    plt.axvline(x=x_value, color='red', linestyle='--', label=f'x = {x_value}')
    plt.axhline(y=cdf_value, color='purple', linestyle='--', label=f'CDF(x) = {cdf_value:.2f}')
    plt.title('Cumulative Distribution Function')
    plt.xlabel('x')
    plt.ylabel('Probability')
    plt.grid(True)
    plt.legend()
    plt.text(mean + 3*std_dev, 0.5, f'CDF(x) = {cdf_value:.2f}', fontsize=10, bbox=dict(facecolor='white', alpha=0.5))

    plt.tight_layout()
    plt.show()

# Example usage
mean = 0.16
variance = 0.05
x_value = 0.6
plot_normal_distribution(mean, variance, x_value)
