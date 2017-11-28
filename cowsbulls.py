import random
c=0             #cows
b=0             #bulls
gn=0            #no. of guesses

n=random.randint(1000,9999)
while(c!=4):
    c=0
    b=0
    g=int(input("Enter your guess!"))
    if(n==g):
        print("cows=4,bulls=0")
        print("Perfect guess!")
        exit()
    else:
        s=str(n)
        gs=str(g)

        for i in range(len(s)):
            for j in range(len(gs)):
                if((s[i]==gs[j]) and (i==j)):
                    c=c+1
                elif((s[i]==gs[j]) and (i!=j)):
                    b=b+1
                else:
                    continue
        gn=gn+1
        print("cows=",c,"bulls=",b,"Guess=",gn)
