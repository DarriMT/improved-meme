a = [ 5 , 1 ,4,3,1]

str1 = ""

for element in a:
    temp = str(element)
    str1+= temp

print(str1)

temp = "| "
for chr in str1:
   temp+= chr + " | "

print(temp)
