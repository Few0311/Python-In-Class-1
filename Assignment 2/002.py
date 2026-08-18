num = int(input("Enter a number : "))
d1 = num// 1000
d2 = num// 100 % 10
d3 = num// 10 % 10
d4 = num % 10
total = d1 + d2 + d3 + d4
print()
print("The digit are : ",d1, d2, d3, d4)
print("The sum of the digit is : ",total)
