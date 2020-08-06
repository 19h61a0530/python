#program to check whether the given number is even or ood using functions
num=int(input("Enter a number for check odd or even: "))
def find_Evenodd(num):
    
    if(num%2==0):
        print(num," Is an even")
    else:
        print(num," is an odd")
find_Evenodd(num)
