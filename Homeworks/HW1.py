#HW1

#Question 1:create a list and swap the 2nd half of the list with the first half of the list and print this list on screen.
A = [1, 2, 34, 56, "istanbul", "bodrum", 34325, "dnm"]
n = int(len(A))
m = int(n/2)
for i in range(0,n):
  if i < m :
    A[i]=A[m+i]
  else:
   A[i]=A[i-m]
i = i+1
print(A)
	
	
#Question 2:ask the user to input a single digit integer to a variable 'n'. Then, print out all of the even numbers from 0 to n (including n).
n = int(input("Please input a single digit integer:  "))
if n > 10:
    print ("Only single digit allowed!")
else:
  for num in range(0, n + 1):
    if num % 2 == 0:
        print(num, end = " ")
