def gradient_descent_quadratic(a, b, c, x0, lr, steps):
    """
    Return final x after 'steps' iterations.
    """
    # Write code here


    # the derivative of f(x) = a*x**2 + b*x + c is f'(x) = 2*a*x + b 
    def quad_derivative(x : float , a:float,b:float )->float:
        return (2*a*x + b)


    for _ in range(steps):
        # update gradient descent 
        x0 -= lr*quad_derivative(x0,a,b)


    return x0 

    