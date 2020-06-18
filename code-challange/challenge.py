"""Print out all of the numbers in the following array that are divisible by 3:
[85, 46, 27, 81, 94, 9, 27, 38, 43, 99, 37, 63, 31, 42, 14]
The expected output for the above input is:
27
81
9
27
99
63
42
You may use whatever programming language you wish.
Verbalize your thought process as much as possible before writing any code. 
Run through the UPER problem solving framework while going through your thought process.
"""

# Step One: write for loop
# if num is divisible by 3 
#print num

myList = [85, 46, 27, 81, 94, 9, 27, 38, 43, 99, 37, 63, 31, 42, 14]

def div3(x):
    for num in x:
        if num %3 == 0:
            print(num)

div3(myList)