thistuple = ("яблоко", "банан", "вишня", "ананас", "апельсин", "мандарин")
y = list(thistuple)
y[2] = "киви"
x = tuple(y)
print(x)
if "киви" in x:
    print("Да, 'киви' в кортеже присутствует")