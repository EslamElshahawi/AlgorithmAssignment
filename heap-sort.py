def max_heapify(arr, n, i):
    largest = i  # Assume root is the largest
    left = 2 * i + 1  # Left child index
    right = 2 * i + 2  # Right child index

    # Check if left child exists and is greater than root
    if left < n and arr[left] > arr[largest]:
        largest = left

    # Check if right child exists and is greater than the largest so far
    if right < n and arr[right] > arr[largest]:
        largest = right

    # If largest is not root, swap with the largest and continue heapifying
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        max_heapify(arr, n, largest)

def build_max_heap(arr):
    n = len(arr)
    # Start from the last non-leaf node and heapify each node
    for i in range(n//2 - 1, -1, -1):
        max_heapify(arr, n, i)

def heapsort(arr):
    n = len(arr)
    
    # Step 1: Build a max heap
    build_max_heap(arr)
    
    # Step 2: Extract elements from the heap one by one
    for i in range(n-1, 0, -1):
        # Swap the root (maximum element) with the last element
        arr[i], arr[0] = arr[0], arr[i]
        
        # Call max_heapify on the reduced heap
        max_heapify(arr, i, 0)

# Example usage
arr = [12, 11, 13, 5, 6, 7]
print("Original array:", arr)
heapsort(arr)
print("Sorted array:", arr)
