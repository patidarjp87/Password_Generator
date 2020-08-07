import random
lower_case="abcdefghijklmnopqrstuvwxyz"
upper_case="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers="0123456789"
special_symbols="<>*@#$%^&"
everything=lower_case+upper_case+numbers+special_symbols
length=11
password="".join(random.sample(everything,length))
print(password)
input()