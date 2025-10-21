import numpy as np

def my_num_calc(f, a, b, n, option):
    x = np.linspace(a, b, n)
    h = (b - a) / (n - 1)
    
    if option == "rect":
        I = 0
        for i in range(1, n):
            I += f(x[i]) * h
            
    elif option == "trap":
        I = 0.5 * (f(x[0]) + f(x[-1]))
        for i in range(1, n - 1):
            I += f(x[i])
        I *= h
        
    elif option == "simp":
        if (n - 1) % 2 != 0:
            raise ValueError("n-1 must be even for Simpson's rule.")
        I = f(x[0]) + f(x[-1])
        for i in range(1, n - 1, 2):
            I += 4 * f(x[i])
        for i in range(2, n - 2, 2):
            I += 2 * f(x[i])
        I *= h / 3
        
    else:
        raise ValueError("Unknown option for numerical integration.")
    
    return I

# Test cases
f1 = lambda x: x**2
print(my_num_calc(f1, 0, 1, 3, "rect"))  
print(my_num_calc(f1, 0, 1, 3, "trap"))  
print(my_num_calc(f1, 0, 1, 3, "simp"))  

f2 = lambda x: np.exp(x**2)
print(my_num_calc(f2, -1, 1, 101, "simp"))  
print(my_num_calc(f2, -1, 1, 10001, "simp"))  
print(my_num_calc(f2, -1, 1, 100001, "simp"))