#We will be writing a program that taskes in a function and finds its roots.

#Function that computes numerical derivative of a function g at a point x
# g is assumed to be a differentiable function.
def deriv(g,x):
    dx = 0.001
    return (g(x + dx) - g(x))/dx

def checkIfRoot(f,x):
    epsilon = 0.0001
    if abs(f(x)) < epsilon:
        return True
    else:
        return False

    



def NewtonsMethod(f,seed,max_iter):
    count = 0
    while count <= max_iter:

        x = seed
        
        if checkIfRoot(f,x) == True:
            return f' Then function equals zero at {x}.'
        elif deriv(f,x) == 0:
            return f'Failure, derivative at{x} equals zero.'

        else:
            x = x - f(x)/deriv(f,x)
            count += 1
    



