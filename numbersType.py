# print("Printing Odd Numbers from First 100 Natural Numbers")
# for i in range (0, 101):
#      if (i%2 != 0):
#          print(i, end=' ')
#
# print("Printing Even Numbers from First 100 Natural Numbers")
# for i in range(0, 101):
#     if (i%2 == 0):
#         print(i, end=' ')
#
# print("Printing Prime Numbers from First 100 Natural Numbers")
# counter=0   #intializing counter variable to 0
# for n in range(1, 101): #iterating for numbers between 2 and n/2+1
#     for i in range(2, int(n/2+1)):  #checking number of divisors for a number
#         if n%i==0:  #check for remainder is 0
#             counter=counter+1   #increase the counter if you find a divisor
#     if counter==0:  #decision to see if counter is 0 i.e. no divisors
#         print(n, end=" ")   #printing if the number is prime
#     counter=0

check = 0
sum = 0
print("Perfect Numbers from First 100 Natural Numbers")
for n in range (1, 101):
    for i in range (1, int((n/2)+1)):
        check=n%i
        if(check==0):
            sum=sum+i
if sum==n:
    print(n, end=' ')

