#to check given numberr is palindrome or not
num=int(input("Enter a number:"))
temp=num
rev=0
while(num>0):
    dig=num%10
    rev=rev*10+dig
    num=num//10
if(temp==rev):
    print(temp,"The number is palindrome!")
else:
    print(temp,"Not a palindrome!")
