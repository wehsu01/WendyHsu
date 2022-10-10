#operators 
#arithmetic +, -, *, **, /, //, %

a = 3475.12
b = 12

print (a + b)
print (a - b) 
print (a * b)
print (a ** b)
print (a / b)
print (a // b)
print (a % b)

#assignment 
b1 = 'apple'

b1 += 's'
print (b1)
b -= 1
print (b)
b *= 3
print (b)
b /= 3
print (b)
b %= 3
print (b)

#comparison

#if, elif, else 
score = 70

if score >=80:
    print ('pass')
elif score > 70:
    print ('accept')
else: 
    print ('did not pass')