#  Trims Whitespaces


# lstrip(): This method is used to remove leading(left) whitespaces characters from a string including \t. It returns a new string with the leading whitespace characters removed.

text = "\tHello, how are you?"

print(text)     # prints (        Hello, how are you?)

print(text.lstrip())     # prints (Hello, how are you?)





# rstrip(): This method is used to remove trailing(right) whitespaces characters from a string including \t. It returns a new string with the trailing whitespace characters removed.

text = "Hello, how are you?\t"

print(text)     # prints (Hello, how are you?       )

print(text.rstrip())     # prints (Hello, how are you?)





# strip(): This method is used to remove both leading an trailing whitespace characters from a string including \t.

text = "\tHello, how are you?\t"

print(text)     # prints (        Hello, how are you?        )

print(text.strip())     # prints (Hello, how are you?)