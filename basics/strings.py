""" a = "hello"
print(a[1])

b = "world"
print(b[0:3])

length = len(b)
print(b[1:length]) """

txt = "The rain in Spain stays mainly in the plain"
x = "ain" in txt
print(x)

a = "Hello, World!"
b = a.split(",")
print(b)

quantity = 3
itemno = 14
price = 23.45
myorder= "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))

