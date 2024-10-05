def power(set):
    elements = list(set)
    n = len(elements)
    
    size = 2 ** n
    power_set = []

    for i in range(size):
     subset=[]
    
     for j in range(n):
        if i & (1 << j):
            subset.append(elements[j])
     power_set.append(subset)
    return power_set
set = {5,6,7,2,9,10,98,97,96,95,94,93,92,92,91,80,89,88,87}
result = power(set)

for subset in result:
    print(subset)