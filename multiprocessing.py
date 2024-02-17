import time
from multiprocessing import Pool, cpu_count


def factorize_sync(num):
  factors = [i for i in range(1, num + 1) if num % i == 0]
  return factors

def parallel_factorize(*numbers):
  with Pool(cpu_count()) as pool:
      result = pool.map(factorize_sync, numbers)
  return result

if __name__ == "__main__":
  numbers_to_factorize = [128, 255, 99999, 10651060]

  start_time_sync = time.time()
  results_sync = [factorize_sync(num) for num in numbers_to_factorize]
  end_time_sync = time.time()

  time_taken_sync = end_time_sync - start_time_sync

  print("Synchronous execution results:", results_sync)
  print("\nTime taken for synchronous execution:", time_taken_sync, "seconds")

  start_time_parallel = time.time()
  results_parallel = parallel_factorize(*numbers_to_factorize)
  end_time_parallel = time.time()
  
  time_taken_parallel = end_time_parallel - start_time_parallel
  
  print("\n\nParallel execution results:", results_parallel)
  print("\nTime taken for parallel execution:", time_taken_parallel, "seconds")

  