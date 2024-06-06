def format(str):
    str = str[1:-1]
    str = str.replace('[', '(')
    str = str.replace(']', ')')
    return "".join(['['] + list(str) + [']'])