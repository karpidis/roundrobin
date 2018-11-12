#defining the pairing of the round
def printpairing(r,A):
    print("\nRound",r,"\n")
    """Here I check if the round is even or odd
       because in even round the biggest number player takes white"""
    if r%2==1: 
        for i in range(half):
        #In odd round pairs given by the the following algorithm
            print(A[i],"-",A[n-1-i])
    else:
#In even round pairs we have to seperate the 1st table and after use
#the same algorithm
        print(A[n-1],"-",A[0])
        for i in range(1,half):
            print(A[i],"-",A[n-1-i])
        
#ask how many players will play
n=int(input("How many players will play?\t",))
#check if players are even or odd number
if n%2==1:
    n+=1
    print(n,"is meant to be the bye")
half=int(n/2)
#Create the list of players
A=[x for x in range(1,n+1)]
#Print 1st round pairing
printpairing(1,A)
for gyros in range(2,n):
    """Remove and save the constant player"""
    K=A[n-1]
    del A[n-1]
    """Moving in the first half of the list to the end of it"""
    A.extend(x for x in A[0:half])
    """Saving the 2nd half to the first one"""
    A[0:half-1]=A[half:n-1]
    """Remove double entries"""
    del A[half-1:n-1]
    """Adding constant player"""
    A.append(K)
    """Make the pairing"""
    printpairing(gyros,A)
