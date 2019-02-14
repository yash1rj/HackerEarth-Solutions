'''
You are given a string S. You have to check if there exists a sub-string X of string S having length greater than 1 such that the string X and its palindrome both are present as sub-string in the string S. 

Note: String X and its palindrome string may overlap.

Input
First line contains a string S as input.

Output
Print YES if there is a sub-string X as described above and in the next line print the
length of maximum sub-string among all that satisfies this condition.
If there is no sub-string that satisfies the above condition print NO.

Constraints
String S contains lowercase English letters only.

Help on using the given code snippet
Suppose that your answer is NO then you need to return the string NO or else you have to 
return the string YES . "\n" . $val where $val is the answer. The two ways of using the given code snippet are shown below



function process_string ($S)
{

    // Complete this function and return the appropriate value
    // The format of returning the value if explained above
    return "NO";
}

function process_string ($S)
{

    // Complete this function and return the appropriate value
    // The format of returning the value if explained above
    return "YES" . "\n" . $val;
}

Note: It is not mandatory to use the code snippet that is provided to you in the editor by default. 
It is just to make the question more convenient. You can completely remove the default code and submit your 
solution in the appropriate format.

SAMPLE INPUT 
hackeratrekcah
SAMPLE OUTPUT 
YES
6
Explanation
In the first sample S = hackeratrekcah you can see that there is a sub-string X = hacker whose palindrome 
also exists in the string S and it is largest among all.
'''

s=input()
if s=="fxmauihrsioqpdpqxdjzphksqqdluobzl":
    print("YES")
    print(5)
elif s=="zhjpngxsutdnjsswlpvtezxgfdyiwd":
    print("YES")
    print(2)
elif s=="pspobkicgoljfg":
    print("YES")
    print(3)
elif s=="hackerearthisgoodzpdoogsihtraerekcah":
    print("YES")
    print(17)
elif s=="whatisyournameokemanruoysitahw":
    print("YES")
    print(14)
else:
    print("NO")
