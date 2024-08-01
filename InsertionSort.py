# Required functions for randomizing array A and getting elapsed time
import random
import time

# Sort array A of size n using the insertion-sort algorithm
def InsertionSort(A, n):
    
    start_time = time.time()
    
    # Only perform the algorithm for arrays of at least 2 elements, otherwise no sorting needed
    if n > 1:
    # Traverse through A[1...n-1] starting at the first unvisited element
        for i in range(1, n):
            curr_key = A[i]
        
        # Move any elements of A[0...i-1] that are greater than the visited
        # element to 1 index ahead of their current one
            j = i - 1
            while j >= 0 and A[j] > curr_key:
                A[j + 1] = A[j]
                j -= 1
            # Place original element in index j+1; either 0 or 1 index ahead of
            # the first element that is less than it
            A[j + 1] = curr_key
    
    end_time = time.time()
    # Print how many seconds it took to sort the array
    print("Sort complete.\nElapsed time: ", end_time - start_time, " seconds")

# Generate and test 10 arrays of random values
n = 1000
for i in range(10):
    A = [random.randint(0, 1000) for _ in range(n)]
    print("Sorting array", i+1, "...")
    InsertionSort(A, n)
    
