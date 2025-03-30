l1 = [i for i in range(10) if i%2==0]
l2 = [i for i in l1 if i in [1,2,3,4]]
print(l1,l2)