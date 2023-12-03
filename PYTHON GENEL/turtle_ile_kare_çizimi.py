# turtle ile kare çizimi:
from turtle import*
pensize(5)
x=int(input("kaç kare olacak giriniz..:"))
for a in range(x):
    fd(100)
    rt(90)
    for i in range(1,5):
        fd(50)
        rt(90)
done()
