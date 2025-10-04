# day 02
#recursion

"""def printN(n):
        if n== 0:
            return       
        printN(n-1)
        print(n,end=' ')     
printN(10)"""

#print gfg n times:-

"""def gfg(n):
    if n==0:
        return
    print("gfg")
    gfg(n-1)
    
        
gfg(10)   """


#print n to 1
"""def printN(n):
        if n== 0:
            return       
        
        print(n,end=' ')
        printN(n-1)
        
printN(10)"""

#sum of first n digits:-

"""def sumN(n):
    sum = 0
    if n==0:
        return
    sum += n**3
    sumN(n-1)
    return (sum)
print(sumN(5))"""

#sum of first n digits:-
"""def sumN(n):
    if n == 0:
        return 0
    prev = sumN(n - 1)
    total = prev + n**3
    return(total)   
print(sumN(5))"""

"""sum =0
n= int(input("enter a number : "))
for i in range(n+1):
    sum += (i**3)
print(sum)"""


#factorail less than or equal to:-

def factN(n):
    fact = []
    if n == 0 :
        return 1
    fact = n* factN(n-1)
    if fact <=n:
        print(fact, end=' ')
    return fact

print(factN(3))
    


"""fact =1
n = 6
for i in range(1,n): 
        fact = fact*i
        if fact <= n:
            print(fact,end=' ')
        else:
            break
print(fact)
    """