# Program to multiply two matrices
import random

N = 250

@profile
def make_matrices(N):

    # NxN matrix
    X = []
    for _ in range(N):
        X.append([random.randint(0, 100) for _ in range(N)])

    # Nx(N+1) matrix
    Y = []
    for _ in range(N):
        Y.append([random.randint(0, 100) for _ in range(N+1)])

    return X, Y

@profile
def matmult(X, Y, N):

    # result is Nx(N+1)
    result = []
    for i in range(N):
        result.append([0] * (N+1))

    # iterate through rows of X
    for i in range(len(X)):

        # iterate through columns of Y
        for j in range(len(Y[0])):

            # iterate through rows of Y
            for k in range(len(Y)):
                result[i][j] += X[i][k] * Y[k][j]

    return result


def main():
    
    X, Y = make_matrices(N)
    result = matmult(X, Y, N)

    for r in result:
        print(r)


if __name__ == "__main__":
    main()