def factors(n):
    print("Factors of", n, "are")
    for i in range(1, int(n**(0.5)) + 1) :
        if n%i == 0 and i*i != n:
            print(i, n//i)
        elif i * i == n :
            print(i)
        else :
            pass
    return 
    
 
n = int(input("Enter a number"))
factors(n)
