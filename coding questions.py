#1. Write a Python program to reverse a string without using slicing.
from multiprocessing.reduction import duplicate

string1="Ganesh"
rev=""
for i in string1:
    rev= i + rev
print(rev)


#2. Write a program to check if a number is prime.
def prime(num):
    if num <= 1:
        print("Not a prime number")
    else:
        for i in range(2, num):
            if num % i == 0:
                print(num, "is not a prime number")
                break
            else:
                print(num, "is a prime number")

prime(5)


#3. Write a Python program to find the largest number in a list without using max().
list1=[1,2,3,5,4,6,7,99,88]

largest = list1[0]

for num in list1:
    if num > largest:
        largest = num

print(largest)


#4. Write a program to count the number of vowels in a given string.
vowel="aeiou"
string="ganesh"
count=0
for s in string:
    if s in vowel:
        count=count+1
print(count)


#5. Write a program to check if a string or number is a palindrome.
def palindrome(string2):
    rev2 = ""
    for i in string2:
        rev2 = i + rev2
    print(rev2)
    if rev2 == string2:
        print("palindrome")
    else:
        print("not palindrome")
palindrome("121")


#6. Write a Python program to print the first N Fibonacci numbers.
n = 10  # how many numbers

a = 0
b = 1
list4=[]
list5=[]
for i in range(n):
    list4.append(a)
    a, b = b, a + b
print(list4)

n = 10  # how many numbers

c = 0
d = 1
next=0
list5=[]
for i in range(n):
    list5.append(c)
    next=c+d
    c=d
    d=next

print(list5)

#7. Write a Python program to remove duplicate elements from a list.
dup=[1,1,2,3,4,5,6,6,5]
print(set(dup))
dup1=[]
for i in dup:
    if i not in dup1:
        dup1.append(i)
print(dup1)


#8. Write a program to calculate the factorial of a number using a loop.
def factorial1(n):
    if n<0:
        print("invalid numbers")
    elif n==0:
        return 1
    else:
        res = 1
        for i in range(1,n+1):
            res=i*res
        print(res)
factorial1(5)




#9. Write a Python program to count the number of words in a given sentence.
s1="Ganesh Hello Ganesh"
count1=1 # Because at least 1 word is there
for i in s1:
    if i == " ":
        count1=count1+1
print(count1)


#10. Write a program to compute the sum of digits of a number.
def summation(num10):
    res=0
    for i in range(1,num10+1):
        res=res+i
    print(res)
summation(4)




#11. Write a program to separate even and odd numbers in a list.
Numbers=[1,2,3,4,5,6,22,53]
even=[]
odd=[]

for i in Numbers:
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)
print(even)
print(odd)


#12. Write a Python program to sort a list without using sort() or sorted().
sorting2=[3,4,5,6,7,8,1,2]
for i in range(0,len(sorting2)):
    for j in range(len(sorting2)-1):
        if sorting2[j] < sorting2[j+1]:
            sorting2[j],sorting2[j + 1]= sorting2[j+1],sorting2[j]
print(sorting2)


#13. Write a program to find the second largest number in a list.
sorting1=[3,4,5,6,7,8,1,2]
for i in range(0,len(sorting1)):
    for j in range(len(sorting1)-1):
        if sorting1[j] < sorting1[j+1]:
            sorting1[j],sorting1[j + 1]= sorting1[j+1],sorting1[j]
print(sorting1[1])

#14. Write a program to check if two strings are anagrams of each other.
s1 = "listen"
s2 = "silent"

# Step 1: If lengths differ, not anagrams
if len(s1) != len(s2):
    print("Not Anagram")
else:
    dict1 = {}
    dict2 = {}

    # Step 2: Count characters in first string
    for ch in s1:
        dict1[ch] = dict1.get(ch, 0) + 1

    # Step 3: Count characters in second string
    for ch in s2:
        dict2[ch] = dict2.get(ch, 0) + 1

    # Step 4: Compare dictionaries
    if dict1 == dict2:
        print("Anagram")
    else:
        print("Not Anagram")



#15. Write a Python program to count occurrences of each character in a string.
s = "banana"
count_dict = {}

for ch in s:
    count_dict[ch] = count_dict.get(ch, 0) + 1
    #print(count_dict)
print(count_dict)



#16. Write a program to swap two variables without using a third variable.

def swap(y,x):
    x,y=y,x
    print(x,y)
swap(6,7)

#17. Write a program to find common elements between two lists.
l4 = [1, 4, 5, 6]
l5 = [1, 6, 5, 3]

common = []

for x in l4:
    if x in l5:
        common.append(x)

print(common)




#18. Write a Python program to convert a list of elements into a single string.
#19. Write a program to reverse a list without using reverse().
r1="Ganesh"
r2=""
for i in r1:
    r2=i+r2
print(r2)
#20. Write a program to find the missing number in a list from 1 to N.

l1 = [1, 2, 4, 5]
N = 5

for i in range(1, N+1):
    if i not in l1:
        print("Missing number:", i)
        break
