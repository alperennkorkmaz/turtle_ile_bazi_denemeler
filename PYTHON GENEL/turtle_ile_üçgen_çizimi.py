from turtle import*
# turtle ile üçgen çizimi:
pensize(5)
x=int(input("kaç üçgen istiyorsunuz..:"))
for a in range(x):
    fd(100)
    lt(120)
    for i in range(1,4):
        fd(50)
        lt(120)
done()