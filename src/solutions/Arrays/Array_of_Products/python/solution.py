 # Write a function that takes in a non-empty array of integers and returns an
 #   array of the same length, where each element in the output array is equal to
 #   the product of every other number in the input array.
 # 
 #   In other words, the value at output[i] is equal to the product of
 #   every number in the input array other than input[i].
 # Note that you're expected to solve this problem without using division.
 # Sample Input
 # array = [5, 1, 4, 2]
 # 
 # Sample Output
 # [8, 40, 10, 20]
 # // 8 is equal to 1 x 4 x 2
 # // 40 is equal to 5 x 4 x 2
 # // 10 is equal to 5 x 1 x 2
 # // 20 is equal to 5 x 1 x 4
 # 
 # Time: O(n) | Space: O(n) - where n is the length of the input array

# Time: O(n^2) | Space: O(n)
def arrayOfProducts(array):
    products = [1 for _ in range(len(array))]
    for i in range(0, len(array)):
        runningProduct = 1
        for j in range(0, len(array)):
            if i != j:
                products[i]*= array[j]
    return products

def arrayOfProducts1(array):
	products = [1 for _ in range(len(array))]
	leftRunningProduct = 1
	for i in range(0, len(array)):
		products[i] = leftRunningProduct
		leftRunningProduct*=array[i]
	
	rightRunningProduct = 1
	for i in reversed(range(0, len(array))):
		products[i]*=rightRunningProduct
		rightRunningProduct*=array[i]
	return products