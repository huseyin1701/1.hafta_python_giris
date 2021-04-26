x = 5

def fonk():
    y = 4
    print(y)

fonk()

def myfunc():
    print(x)
    print(y)  # değişken global olmadığı için ulaşamadı hata verdi

myfunc()