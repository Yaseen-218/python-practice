#program to check that the word is present in given sentence or not 
a=input("Enter the sentence ")
b=input("Enter the word to check it is in given sentence or not ")
c=a.lower()
d=b.lower()
if b in c:
    print("yes this word is present ",b)
else:
    print("no the searched word is not present ",b)