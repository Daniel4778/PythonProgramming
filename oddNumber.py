# programmer: Daniel Paddock
# program: Odd Numbers
# created on: 09/21/2022 08:20:00 AM
# last modified: 0/21/2022 08:20:00 AM
# version: 3.7.9

# print("Printing Odd Number from First 100 Natural Numbers")
# for i in range (0, 101):
#     if (i%2 != 0):
#         print(i, end=' ')

print("Alternate Approach")
counter = 10
for k in range(1, 51):
    # if (2*k-1 == 0):
    print(2*k-1, end=' ')
    counter=counter-1
    if (counter == 0):
        print("\n")
        counter = 10
