import numpy as np
import sympy as sp


def calculate_eigenvalues(matrix):
    """
    Calculate eigenvalues of a square matrix.
    """
    # Write code here

    # Helper Functions

    # Check documentation for it

    def c(A, n):

        def power(A, pow):
            return np.linalg.matrix_power(A, pow)

        arr = [1] + [0] * n

        for k in range(1, n + 1):
            arr[k] = (1 / k) * sum(
                (-1) ** (i - 1)
                * arr[k - i]
                * np.trace(power(A, i))
                for i in range(1, k + 1)
            )

        return arr

    def is_homogeneous(A):

        if A == []:
            return False

        n = len(A)

        

        for a in A:
            if isinstance(a, list):
                if len(a) != n:
                    return False

            else:
                return False

        return True

    # Check matrix conformity to be homogeneous to matrices

    if not is_homogeneous(matrix):
        return None

    # List --------------> NumPy array
    matrix = np.asarray(matrix)

    # Check for squareness
    if len(set(matrix.shape)) != 1:
        return None

    # The matrix dimension
    n = matrix.shape[0]

    # The array coefficients
    arr = c(matrix, n)

    # Computation of mathematical equation
    x = sp.symbols('x')

    equation = sum(
        (-1) ** i * arr[i] * x ** (n - i)
        for i in range(n + 1)
    )

    # Solution of the equation in the IC domain
    # so we will have exactly n solutions
    return np.asarray(sp.solve(equation, x))