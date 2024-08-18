s = input("Enter a String: ")
s = s.replace(" ", "").lower()

start = 0
end = len(s) - 1
flag = True

while start < end:
    if s[start] != s[end]:
        flag = False
    start += 1
    end -= 1

if flag:
    print("The string is a Palindrome.")
else:
    print("The string is not a Palindrome.")