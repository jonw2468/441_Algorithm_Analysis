# Required functions for randomizing array A and getting elapsed time
import random
import time

# Sort array A of size n using the selection-sort algorithm
def SelectionSort(A, n):
    
    start_time = time.time()
    
    # Traverse through the array starting at the first unsorted element
    for i in range(n):
        
        # Find the index of the lowest element in the unsorted part of the array
        lowest_index = i
        for j in range(i+1, n):
            if A[j] < A[lowest_index]:
                lowest_index = j
        
        # Swap the lowest unsorted element with the first unsorted element
        A[i], A[lowest_index] = A[lowest_index], A[i]

    end_time = time.time()
    # Print how many seconds it took to sort the array
    print("Sort complete.\nElapsed time: ", end_time - start_time, " seconds")

# Generate and test 10 arrays of random values
n = 10
for i in range(10):
    A = [random.randint(0, 1000) for _ in range(n)]
    print("Sorting array", i+1, "...")
    SelectionSort(A, n)
