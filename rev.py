n = int(input())#547
rev = 0
while n !=0:#T T T
    rem = n%10 #7 4 5
    rev = rev*10 + rem#7 74 745 
    n = n//10#54 5 0
print(rev)