import numpy as np
from scipy.integrate import quad

def f(x):
    return x ** 2

# Monte Carlo integration method
def monte_carlo_integration(func, a, b, num_points=10000):
    # Generate random x values in the range [a, b]
    x_random = np.random.uniform(a, b, num_points)
    # Compute function values
    func_values = func(x_random)
    # Calculate the average value of the function and multiply by the interval length
    integral_value = (b - a) * np.mean(func_values)
    return integral_value

def main():
    # integartion interval
    a, b = 0, 1

    # Calcualte integral using Monte Carlo
    monte_carlo_result = monte_carlo_integration(f, a, b)

    # Step 3: Validate result with SciPy's quad method
    quad_result, _ = quad(f, a, b)

    # Prepare results and comparison
    results = {
        "Monte Carlo Result": monte_carlo_result,
        "Quad Result": quad_result,
        "Difference": abs(monte_carlo_result - quad_result)
    }

    print(results)

if __name__ == '__main__':
    main()