"""
Programmer: Daniel Paddock
Program: numbersType
Program Version: 3.10.2
Created On: 9/26/2022 08:11:00
Last Modified: 9/30/2022 08:11:00

"""
print("Welcome to Mathematical Operations")
print("1) Odd Numbers\n"
      "2) Even Numbers\n"
      "3) Prime Numbers\n"
      "4) Perfect Numbers\n"
      "5) Palindrome")
choice = int(input("Select an Operation by Entering a Number:\t"))

match choice:
    case 1:
        print("Printing Odd Numbers from First 100 Natural Numbers")
        for i in range (0, 101):
            if (i%2 != 0):
                print(i, end=' ')

    case 2:
        print("Printing Even Numbers from First 100 Natural Numbers")
        for i in range(0, 101):
            if (i%2 == 0):
                print(i, end=' ')

    case 3:
        print("Printing Prime Numbers from First 100 Natural Numbers")
        counter=0   #intializing counter variable to 0
        for n in range(1, 101): #iterating for numbers between 2 and n/2+1
            for i in range(2, int(n/2+1)):  #checking number of divisors for a number
                if n%i==0:  #check for remainder is 0
                    counter=counter+1   #increase the counter if you find a divisor
            if counter==0:  #decision to see if counter is 0 i.e. no divisors
                print(n, end=" ")   #printing if the number is prime
            counter=0

    case 4:
        check = 0
        sum = 0
        print("Perfect Numbers from First 100 Natural Numbers")
        for n in range(1, 101):
            for i in range(1, int((n/2)+1)):
                check=n%i
                if(check==0):
                    sum=sum+i
            if sum==n:
                print(n, end=' ')
            sum=0

    case 5:
        print("Palindrome Numbers")
        number=int(input("Please Enter number\t"))
        reverse=0
        originalNumber=number
        while number > 0:
            remainder=int(number%10)
            reverse=int(reverse*10+remainder)
            number=int(number/10)
            if originalNumber==reverse:
                print(originalNumber, "Is a Palindrome Number")
            else:
                print(originalNumber, "Is not a Palindrome Number")

