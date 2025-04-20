import re
def password(a):
    reg = "[A-z0-9-_@]{6,18}"
    return print(re.findall(reg, a))


password("my-p@ssw0rd")
