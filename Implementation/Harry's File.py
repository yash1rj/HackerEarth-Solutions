'''
Harry Potter got a challenge to unlock the path and tell its filename and extension.

He uses "Alohomora"  to unlock the file path and break the code just like Hermione used to unlock the door.

Help him to unlock the path and extract the file path, file name and its extension as shown below:

Input:
First line of input contains path of string type.

Output:
First line displays path ,second line displays file name,Third line displays extension

SAMPLE INPUT 
C:\Users\admin\Pictures\flower.jpg
SAMPLE OUTPUT 
Path: C:\Users\admin\Pictures\
File name: flower
Extension: jpg
Explanation
The input String can be divided into three parts, the path, file name and extension. 
These three parts are separated by a backslash character and a dot as shown in the figure below.

***Check Harry's File.png***
'''

s=input()
#print(s)

fn= s.split('\\')[-1].split('.')[0]
pth=s.split(fn)[0]
ext=s.split(".")

print("Path:",pth)
print("File name:",fn)
print("Extension:",ext[1])
