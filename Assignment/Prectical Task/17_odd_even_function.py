def fectorial(num):
    result=1
    for i in range(2,num+1):
        result*=i
    return result
def sum_odd_series(n):
    total=0
    for i in range(1,n+1,2):
        term=(i**2)/fectorial(i)
        total+=term
    return total

def sum_even_series(n):
    total=0
    for i in range(2,n+1,2):
        term=(i**2)/fectorial(i)
        total+=term
    return total

n_odd = 3
n_even = 10

print(f"sum of odd series {n_odd}: ",sum_odd_series(n_odd))

print(f"sum of even series {n_even}: ",sum_even_series(n_even))


