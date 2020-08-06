# function to check number is palindrome or not  
n=int(input("enter number:"))
def findpalin(n):
    x=n
    rev=0
    while(n>0):
        d=n%10
        rev=rev*+d
        n=n//10
        if(x==rev):
            print("no is palindrome")
        else:
            print("no is not palindrome")
findpalin(n);
