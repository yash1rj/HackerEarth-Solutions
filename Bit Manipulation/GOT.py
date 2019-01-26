'''
Jon Snow visits Dragonstone to meet Daenerys Targaryen. He asks for aid in defeating the White Walkers and Army of Dead. 
But Daenerys refuses to believe that white walkers are real. 
She puts a condition before Jon that if he solves the challenge given by her then she will send her army to fight White Walkers. 
She gives certain inputs and outputs , Jon needs to find the logic and predict the output for the corresponding inputs. 
Jon Snow is struggling with the challenge as he knows nothing!! Help Jon to find the logic and win this challenge.

INPUT : Input contains integers separated by a newline

OUTPUT : For the given input , Output the required answer.

NOTE : No. of input integers are unknown.

CONSTRAINTS :
0<= N (total inputs)<= 10^15

SAMPLE INPUT 
0
1
5
12
22
1424
SAMPLE OUTPUT 
0
1
1
4
2
16
'''

from sys import stdin 
lines = list(map(int,stdin.read().splitlines()))
lines=[bin(x)[2:] for x in lines]
#print(lines)
for i in lines:
    j=i[::-1]
    if "1" not in j:
        print("0")
    else:
        print(2**(j.find("1")))
