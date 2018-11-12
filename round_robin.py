#defining the pairing of the round
def printpairing(r,A):
    print("\nRound",r,"\n")
    if r%2==1:
        for i in range(half):
            print(A[i],"-",A[n-1-i])
    else:
        print(A[n-1],"-",A[0])
        for i in range(1,half):
              print(A[i],"-",A[n-1-i])
        
#ask how many players will play
n=int(input("How many players will play?\t",))
if n%2==1:
    n+=1
    print(n,"\t is meant to be the bye")
half=int(n/2)

A=[x for x in range(1,n+1)]

printpairing(1,A)
for gyros in range(2,n):
    K=A[n-1]
    del A[n-1]
    A.extend(x for x in A[0:half])
    A[0:half-1]=A[half:n-1]
    del A[half-1:n-1]
    A.append(K)
    printpairing(gyros,A)
