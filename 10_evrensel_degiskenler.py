x = "awesome"

def func():
    global x
    x="adasdas"

func()

print("Python is "+ x) # string olduğu için x + ile kullanıldı
