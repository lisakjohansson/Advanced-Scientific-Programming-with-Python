from mpi4py import MPI

comm = MPI.COMM_WORLD # communicator (all processes)
rank = comm.Get_rank() # ID of this process
size = comm.Get_size() # total number of processes

print(f"Hello from rank {rank} out of {size}")