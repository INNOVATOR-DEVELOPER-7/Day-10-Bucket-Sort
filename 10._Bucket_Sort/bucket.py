def bucket_sort(array):
    # Determine the maximum value to know the range of the buckets
    max_val = max(array)
    size = len(array)

    # Create empty buckets
    buckets = [[] for _ in range(size)]

    # Put array elements into different buckets
    for num in array:
        index = num * size // (max_val + 1)
        buckets[index].append(num)

    # Sort individual buckets
    for bucket in buckets:
        bucket.sort()

    # Concatenate all sorted buckets into the original array
    sorted_array = []
    for bucket in buckets:
        sorted_array.extend(bucket)
    
    return sorted_array

# Get list of numbers from the user
user_input = input("Enter numbers separated by space: ")
array = list(map(int, user_input.split()))

# Perform bucket sort
sorted_array = bucket_sort(array)

# Print the sorted array
print("Sorted array:", sorted_array)
