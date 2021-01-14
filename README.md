#julia

## Intro
A project that generates a julia fraction image.
The implementation of the project aims to follow good python coding practice
as well as use profiling for gradual optimization.

## Description
**calc\_pure\_python(int desired width, int max\_iterations)**
    Generate grid and compute julia fraction given desired width and max_iteration. Other parameters are predefined in julia.py
**calculate_z_serial_purepython(int maxiter, list zs, list cs)**
    Loop over zs and cs, generate list of integera the same size as zs and cs by compute julia fraction bounded by maxiter
