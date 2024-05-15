str = input()[1:-1]
str = str.replace('[', '(')
str = str.replace(']', ')')
new_s = "".join(['['] + list(str) + [']'])
print(new_s)