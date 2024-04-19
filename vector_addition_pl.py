# Importuje bibliotekę NumPy
import numpy as np 

# Pyta o liczbę elementów wektorze
n = int(input("Enter number of elements : "))

# Wiersz poniżej odczytuje dane wejściowe od użytkownika za pomocą funkcji map() dla pierszego wektora
list1 = list(map(int, 
	input("\nEnter the numbers of the first vector : ").strip().split()))[:n]
# Wiersz poniżej odczytuje dane wejściowe od użytkownika za pomocą funkcji map() dla drugiego wektora
list2 = list(map(int, 
	input("\nEnter the numbers of the second vector : ").strip().split()))[:n]


# Tworzy wektor 1
# Wektor jako szereg
vector1 = np.array(list1) 

# Tworzy wektor 2
# Wektor jako szereg
vector2 = np.array(list2) 

# Pokazuje poziomy wektor 1
print("Horizontal Vector 1: " + str(vector1)) 

# Pokazuje poziomy wektor 2
print("Horizontal Vector 2: " + str(vector2)) 

# Dodaje oba wektory
# a + b = (a1 + b1, a2 + b2, a3 + b3...) 
addition = vector1 + vector2 
  
# Drukuje wynik dodanych wektorów 
print("Vector Addition : " + str(addition)) 