
def factorial(num):
    if num == 1:
        return 1
    else:
        return num*factorial(num-1)
    

def combination(n,r):
    return factorial(n)/(factorial(r)*factorial(n-r))


def permutation(n,r):
    return factorial(n)/factorial(n-1)



