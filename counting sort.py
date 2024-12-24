def counting_sort(arr):
    # Find the maximum value in the array
    max_val = max(arr)
    count = [0] * (max_val + 1)
    output = [-1] * len(arr)
    
    # Count occurrences of each element
    for num in arr:
        count[num] += 1
    
    # Update the count array
    for i in range(1, len(count)):
        count[i] += count[i - 1]
    
    # Build the output array
    for num in reversed(arr):
        output[count[num] - 1] = num
        count[num] -= 1
    
    return output

# Example usage
arr = [4, 2, 2, 8, 3, 3, 1]
sorted_arr = counting_sort(arr)
print("Sorted Array:", sorted_arr)