# importing numpy 
import numpy as np 

# number of elements
n = int(input("Enter number of elements : "))

# Below line read inputs from user using map() function
list1 = list(map(int, 
	input("\nEnter the numbers of the first vector : ").strip().split()))[:n]
# Below line read inputs from user using map() function
list2 = list(map(int, 
	input("\nEnter the numbers of the second vector : ").strip().split()))[:n]


# creating a vector1 
# vector as row 
vector1 = np.array(list1) 

# creating a vector2 
# vector as row 
vector2 = np.array(list2) 

# showing horizontal vector 1
print("Horizontal Vector 1: " + str(vector1)) 

# showing horizontal vector 2
print("Horizontal Vector 2: " + str(vector2)) 

# adding both the vector 
# a + b = (a1 + b1, a2 + b2, a3 + b3...) 
addition = vector1 + vector2 
  
# printing addition vector 
print("Vector Addition : " + str(addition)) 