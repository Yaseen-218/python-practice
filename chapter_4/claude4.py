#write an program to check whteher it is an palindrome or not
a=input("Enter the name or word to check to whether it is palindrome or not :")
b=a[::-1]
if a==b:
    print("Yes it is an palindrome and your word is ",b)
else:
    print("it is not an palindrome and your word is ",b)