import time
import numpy as np

N = 2048

if __name__ == '__main__':
    A = np.random.randn(N, N).astype(np.int8)
    B = np.random.randn(N, N).astype(np.int8)

    flop = N*N*2*N  # Corrected calculation of FLOPs

    print(f"{flop / 1e9} GFLOPS")  # Corrected unit to GFLOPS

    start_time = time.monotonic()

    C = A @ B
    end_time = time.monotonic()
    s = end_time - start_time

    if s > 0:  # Check if time taken is non-zero
        print(f"{flop / s * 1e-9:.5f} GFLOPS")  # Corrected calculation of GFLOPS
        print(f"{flop / s * 1e-12:.5f} TFLOPS")  # Corrected calculation of TFLOPS
    else:
        print("Operation completed too quickly to measure performance.")
