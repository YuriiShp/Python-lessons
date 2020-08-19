A = list(range(1, 60, 2))
print(A)
for i in range(len(A)):
    if i % 2 == 0 and i != len(A)-1:
        A.insert(i+1, A.pop(i))
print(A)
