#write an program to find the vowels in an given string or name
name=input("Enter your name to find how much vowels it contains ")
count=0
for i in name:
    if i in "aeiouAEIOU":
        count+=1
print("the no of vowels your name contains are ",count)
 