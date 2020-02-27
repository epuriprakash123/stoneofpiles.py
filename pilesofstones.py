from itertools import permutations
def perm(arr):
    k=[]
    count=0
    l=permutations(arr)
    for i in list(l):
        k.append(i)
    k=list(set(k))
    for i in k:
        if(len(i)%2==0):
            if(i[-2]>1):
                count=count+1
        else:
            if(i[-2]==1):
                count=count+1
    return count
arr=[4,3,1]        
print(perm(arr))
