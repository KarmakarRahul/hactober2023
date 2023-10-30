# A naive Python implementation of LIS problem


# Global variable to store the maximum
global maximum


# To make use of recursive calls, this function must return
# two things:
# 1) Length of LIS ending with elent arr[n-1]. We use
# max_ending_here for this purpose
# 2) Overall maximum as the LIS may end with an element
# before arr[n-1] max_ref is used this purpose.
# The value of LIS of full array of size n is stored in
# *max_ref which is our final result
def _lis(arr, n):

	# To allow the access of global variable
	global maximum

	# Base Case
	if n == 1:
		return 1

	# maxEndingHere is the length of LIS ending with arr[n-1]
	maxEndingHere = 1

	# Recursively get all LIS ending with
	# arr[0], arr[1]..arr[n-2]
	# If arr[i-1] is smaller than arr[n-1], and
	# max ending with arr[n-1] needs to be updated,
	# then update it
	for i in range(1, n):
		res = _lis(arr, i)
		if arr[i-1] < arr[n-1] and res+1 > maxEndingHere:
			maxEndingHere = res + 1

	# Compare maxEndingHere with overall maximum. And
	# update the overall maximum if needed
	maximum = max(maximum, maxEndingHere)

	return maxEndingHere

<!DOCTYPE html> 
<html lang="en"> 
<head> 
	<meta charset="UTF-8"> 
	<meta http-equiv="X-UA-Compatible"
		content="IE=edge"> 
	<meta name="viewport"
		content="width=device-width, initial-scale=1.0"> 
	<title>Geeks for Geeks</title> 
	<link rel="stylesheet" href="style.css"> 
</head> 
<style> 
	#image-container { 
		display: flex; 
		justify-content: center; 
		align-items: center; 
		height: 100vh; 
	} 

	img { 
		max-width: 100%; 
	} 

	#image-container img:hover { 
		cursor: zoom-in; 
	} 
</style> 

<body> 
	<div id="image-container"> 
		<img src= 
"https://media.geeksforgeeks.org/wp-content/uploads/20230405173803/gfg3-300x300.png"
			alt="Geeks for Geeks"> 
	</div> 
</body> 
<script src="script.js"></script> 

</html>

def lis(arr):

	# To allow the access of global variable
	global maximum

	# Length of arr
	n = len(arr)

	# Maximum variable holds the result
	maximum = 1

	# The function _lis() stores its result in maximum
	_lis(arr, n)
	return maximum


# Driver program to test the above function
if __name__ == '__main__':
	arr = [10, 22, 9, 33, 21, 50, 41, 60]
	n = len(arr)

	# Function call
	print("Length of lis is", lis(arr))

# This code is contributed by NIKHIL KUMAR SINGH
