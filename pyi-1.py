# python program to reverse a number
n = int(input("enter the number:"))
rev = 0
while n!=0:
    rev = rev*10 + n%10
    n = n//10
print("reverse number:",rev)
    
