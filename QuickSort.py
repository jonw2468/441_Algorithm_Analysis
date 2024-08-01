# Required functions for randomizing array A and getting elapsed time
import time
import random

# Sort array A of size n using the quick-sort algorithm
def QuickSort(A, n):
    # Do nothing for empty or single-value arrays
    if n <= 1:
        return A
    
    # Otherwise create, sort, and merge subarrays with the first element in between
    first_value = A[0]
    lesser_values = [x for x in A[1:] if x <= first_value]
    greater_values = [y for y in A[1:] if y > first_value]
    # Sort the two pivot arrays recursively and merge them on either side of the pivot
    return QuickSort(lesser_values, len(lesser_values)) + [first_value] + QuickSort(greater_values, len(greater_values))

# Generate and test 10 arrays of random values
n = 10
for i in range(10):
    A = [random.randint(0, 1000) for _ in range(n)]
    print("Sorting array", i+1, "...")
    # Runtime is now tracked in main since MergeSort() is recursive
    start_time = time.time()
    QuickSort(A, n)
    
