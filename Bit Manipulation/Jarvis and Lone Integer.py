'''
Today Tony Stark is upset with Jarvis, as it blew the whole plan of him defeating the Flash in parallel universe by showing him two images of Flash. Tony couldn't identify the real one and ended up getting hit hard. Jarvis is upset too and he wants to prove that it was not his mistake. Help Jarvis to prove himself faithful and true AI.

To prove, that Jarvis is not at fault, he is given N non-negative integers and he has to identify a lone integer among them. A lone integer is defined as an integer in the given array of integers that is left alone after pairing each of the other integers. Two integers can be paired if they have same value in decimal number system and have different indices in the array. (Look at example case for better understanding and it is guaranteed that there is at most one such integer.)

    NOTE: An integer can't be paired with itself and once paired it can't be used to pair with other integers. (There are spaces after each input.)

INPUT:
First line will contain T, number of times Jarvis tests itself. For each test there will be two lines. First line of each test will contain number of integers N he takes, and next line will have N non-negative integers.

OUTPUT:
For each test output one lone integer or -1 if it doesn't exist.

SAMPLE INPUT

2  
7  
8 7 8 1 6 6 7  
2  
5 5

SAMPLE OUTPUT

1
-1

Explanation

1 In the first test, 8, 7 and 6 can be paired with respected same valued decimal integers, while 1 is left alone.
2 In the second test, 5 can be paired with other 5 hence there is no lonely integer. So, the output will be 1.

'''
from collections import Counter
t=int(input())
for i in range(t):
    n=int(input())
    a=[x for x in input().split(" ")]
    #a="".join(a)
    d=dict(Counter(a))
    for j in d:
        if d[j]%2!=0:
            print(j)
            break
    else:
        print(-1)
