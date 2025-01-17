# Day-10-Bucket-Sort
Here Python Program for Bucket Sort. Day 10 of Day 365.
- Initial Setup: Determine the range and create a number of empty buckets.
- Distribution: Distribute the elements of the array into the appropriate buckets. Each bucket contains a range of values.
- Individual Sorting: Sort each bucket individually. This can be done using insertion sort or any other sorting algorithm.
- Concatenate Buckets: Concatenate the sorted buckets back into a single sorted array.

Here's a visual representation using the example array [0.42, 0.32, 0.23, 0.52, 0.25, 0.47, 0.51]:

1. Initial Array: [0.42, 0.32, 0.23, 0.52, 0.25, 0.47, 0.51]
2. Create Buckets: Assume we have 5 buckets for numbers ranging from 0 to 1:
   - Bucket 0: [ ]
   - Bucket 1: [ ]
   - Bucket 2: [ ]
   - Bucket 3: [ ]
   - Bucket 4: [ ]
3. Distribute Elements:
   - Bucket 0: [ ]
   - Bucket 1: [ ]
   - Bucket 2: [0.23, 0.25]
   - Bucket 3: [0.32]
   - Bucket 4: [0.42, 0.47, 0.52, 0.51]
4. Sort Each Bucket:
   - Bucket 0: [ ]
   - Bucket 1: [ ]
   - Bucket 2: [0.23, 0.25]
   - Bucket 3: [0.32]
   - Bucket 4: [0.42, 0.47, 0.51, 0.52]
5. Concatenate Buckets:
   - Combined: [0.23, 0.25, 0.32, 0.42, 0.47, 0.51, 0.52]

The final sorted array is [0.23, 0.25, 0.32, 0.42, 0.47, 0.51, 0.52].
