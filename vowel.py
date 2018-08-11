#to check the given input is vowel or constant

n = input("Enter the character: ")

if n in ('a','e','i','o','u','A','E','I','O','U'):
    print("The given %s alphabet is vowel" % n)
else:
    print("The given %s alphabet is consonant" %n)

