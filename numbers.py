#ask user to enter three different integers
#create variables for the three integers; num1, num2, num3
#print sum of the three integers
#print num1 - num2
#print num3 multiply by num1
#sum of (num1,num2,num3) divide by num3


num1 = int(input("any number"))
num2 = int(input("any number"))
num3 = int(input("any number"))

sum = num1 + num2 + num3
print(sum)

sub = num1 - num2

print(sub)

product = num3 * num1
print(product)

sum2 = ((sum)/ num3)
print(sum2)

# I had to cast the variables num1, num2,num3  to intergers 
# because I got errors when I ran my code to do the calculations