"""
Julia set generate without optinonal PIL-based image drawing
"""
import time
import logging
import numpy as np
import matplotlib.pyplot as plt

logging.basicConfig()
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# Area of complex space to compute
x1, x2, y1, y2 = -1.8, 1.8, -1.8, 1.8
c_real, c_imag = -0.62772, -0.42193
max_radius = 2
max_iter = 300
desired_width = 1000

def calc_pure_python(desired_width, max_iterations):
    """
    Crate a list of complex coordinates (zs) and complex parameters (cs), and build julia set
    """
    x_step = (x2 - x1) / desired_width
    y_step = (y2 - y1) / desired_width
    x = []
    y = []
    ycoord = y1
    while ycoord < y2:
        y.append(ycoord)
        ycoord += y_step
    xcoord = x1
    while xcoord < x2:
        x.append(xcoord)
        xcoord += x_step
    # Build a list of coordinates and the initial condition for each cell.
    # Note that our initial condition is a constant and could easily be removed.
    # We use it to simulate a real-word scenario with several inputs to our function
    zs = []
    cs = []
    for ycoord in y:
        for xcoord in x:
            zs.append(complex(xcoord, ycoord))
            cs.append(complex(c_real, c_imag))
    logger.debug(f"Length of x: {len(x)}")
    logger.debug(f"Total elements: {len(zs)}")
    start_time = time.time()
    output = calculate_z_serial_purepython(max_iterations, zs, cs)
    end_time = time.time()
    secs = end_time - start_time
    logger.debug(f"{calculate_z_serial_purepython.__name__} took {secs} seconds.")
    # This sum is expected for a 1000^2 grid with 300 iterations
    # It ensures that our code evolves exactly as we'd intended
    
    plt.ion()
    fig, ax = plt.subplots()
    im = ax.imshow(np.array(output).reshape(int(np.sqrt(len(output))), -1))
    fig.savefig("julia.png")
    logger.debug(f"Max output value: {max(output)}")
    assert sum(output) == 33219980

def calculate_z_serial_purepython(maxiter, zs, cs):
    """Calculate output list using Julia update rule
    """
    output = [0] * len(zs)
    for i in range(len(zs)):
        n = 0
        z = zs[i]
        c = cs[i]
        while abs(z) < max_radius and n < maxiter:
            z = z * z + c
            n +=1
        output [i] = n
    return output

if __name__ == "__main__":
    #Calculate the Julia se uisng a pure Python solution with reasonable defaults for a laptop
    calc_pure_python(desired_width=desired_width, max_iterations=max_iter)
