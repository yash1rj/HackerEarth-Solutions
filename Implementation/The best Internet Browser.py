'''
In the race for the best Internet browser, there's now a new contender for it, this browser 
is called the: "The Semantic Mind-Reader!" After its promo on the world wide web, everyone's been desperately waiting for 
the browser to be released. And why shouldn't they be curious about it, after all, it's the new project of our 
very own genius "Little Jhool!" He's worked very hard for this browser, and to add new mind reading features to it.

Apart from the various security powers it possesses, it's called the mind-reader for a reason. Here's why:

You don't need to type 'www.' to open a website anymore.
Though, you still need to type '.com' to open a website.
The browser predicts ALL THE VOWELS in the name of the website. (Not '.com', though. Again!)
Obviously, this means you can type the name of a website faster and save some time.
Now to convince users that his browser will indeed save A LOT of time for users to open a particular 
website, Little Jhool has asked you to prepare a report on the same.

Input format:
The first line contains tc, the number of test cases.
The second line contains the name of websites, as a string.

Output format:
You have to print the ratio of characters you would have typed in Jhool's browser, to your normal browser.

Constraints:
1 <= tc <= 100
1 <= Length of the website <= 200

NOTE: You do NOT need to print the output in its lowest format. You should print in its original fraction format.
The names of all the websites will be in small case only.

Every string will start from *www. and end with *.com, so well!**

SAMPLE INPUT 
2
www.google.com
www.hackerearth.com
SAMPLE OUTPUT 
7/14
11/19
Explanation
Consider the first case:

In Jhool's browser, you'll only have to type: ggl.com (7 characters) while in a normal browser, 
you'll have to type www.google.com, which is 14 characters.
'''

tc=int(input())
for i in range(tc):
    web=input()
    ol=len(web)
    a=[x for x in web.split(".")]
    a[1]=list(a[1])
    b=[]
    for j in a[1]:
        if j not in "aeiou":
            b.append(j)
    b.append(".")
    for k in a[2]:
        b.append(k)
    nl=len(b)
    print(nl,ol,sep="/")