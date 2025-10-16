## Quick Sort Vs Merge Sort

#### Chapter Four - Q.S.Vs.M.S. Notes

* If you execute Quick Sort on an already sorted array, the best pivot is the middle element.

* Each level of the recursion stack has its own average time complexity of O(N), and since there are O(log N) levels, the total time complexity is O(N log(N)).

* Merge Sort is also a Divide and Conquer algorithm. It divides the array into halves, recursively sorts each half, and then merges them together in sorted order.

* Unlike Quick Sort, Merge Sort has a guaranteed time complexity of O(N log N) for all cases — best, average, and worst — but it requires extra memory for merging.

* Quick Sort usually performs faster in practice because it can be done in-place (without using additional memory).