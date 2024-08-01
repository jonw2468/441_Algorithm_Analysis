# Required functions for randomizing array A and getting elapsed time
import time
import random

# Sort array A of size n using the merge-sort algorithm
def MergeSort(A, n):
    # This sort only works if the array is more than 1 element
    if n > 1:
        # Make the left-half and right-half subarrays
        l = n // 2
        A_left = A[:l]
        A_right = A[l:]

        # Recursively sort the subarrays
        MergeSort(A_right, len(A_right))
        MergeSort(A_right, len(A_right))

        i = j = k = 0

        # Merge the subarrays back into A
        while i < len(A_left) and j < len(A_right):
            # Check which visited element is lower and put it in index k of A
            if A_left[i] < A_right[j]:
                A[k] = A_left[i]
                i += 1
            else:
                A[k] = A_right[j]
                j += 1
            k += 1
        
        # Copy remaining subarray elements (if any) back to A
        while i < len(A_left):
            A[k] = A_left[i]
            i += 1
            k += 1
        while j < len(A_right):
            A[k] = A_right[j]
            j += 1
            k += 1

# Generate and test 10 arrays of random values
n = 1000
for i in range(10):
    A = [random.randint(0, 1000) for _ in range(n)]
    print("Sorting array", i+1, "...")
    # Runtime is now tracked in main since MergeSort() is recursive
    start_time = time.time()
    MergeSort(A, n)
    end_time = time.time()
    # Print how many seconds it took to sort the array
    print("Sort complete.\nElapsed time: ", end_time - start_time, " seconds")
