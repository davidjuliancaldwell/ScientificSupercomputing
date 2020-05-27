#!/usr/bin/python 

def mergeSort(a):
    aux = [0] * len(a)
    sort(a,aux,0,len(a)-1)

def sort(a,aux,lo,hi):
    if (hi <= lo):
        return a
    mid = lo + (hi-lo)//2
        
    sort(a,aux,lo,mid)
    sort(a,aux,mid+1,hi)
        
    merge(a,aux,lo,mid,hi)
    
def merge(a,aux,lo,mid,hi):
    i = lo
    j = mid+1
    for k in range(lo,hi+1):
        aux[k] = a[k]
    k = lo
    while (k<=hi):
        while((i <= mid) and (j <= hi)):
            if (aux[j]<aux[i]):
                a[k] = aux[j]
                j = j+1
                k = k+1
            else:
                a[k] = aux[i]
                i = i + 1
                k = k + 1
            
        while(i<=mid):
            a[k] = aux[i]
            i = i+1
            k = k+1
                
        while(j<=hi):
            a[k] = aux[j]
            j = j + 1
            k = k + 1

#if __name__ == "__main__":
#    import sys
#    mergeSort((sys.argv[1]))
#            