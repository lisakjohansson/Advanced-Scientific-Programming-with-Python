# Program to multiply two matrices
import random

# Imported numpy to create matrices and handle matrix multiplication
import numpy as np

N = 250

@profile
def make_matrices(N):

    # Optimized to give full matrix of random integers in one go

    rng = np.random.default_rng()

    X = rng.integers(0, 101, size=(N, N), dtype=np.int64)
    Y = rng.integers(0, 101, size=(N, N+1), dtype=np.int64)

    return X, Y

@profile
def matmult(X, Y, N):

    # Removed everything inside this function and replaced with numpy 
    return np.matmul(X, Y)


def main():
    
    X, Y = make_matrices(N)
    result = matmult(X, Y, N)
    
    # Removed print statement

if __name__ == "__main__":
    main()