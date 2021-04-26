liste= ["Elma", "Armut", "Ayva"]

liste.sort()
print(liste)

liste.reverse()
print(liste)
print("------------------")
def fonk(n):
    return abs(n-50)
sayi_listesi = [100, 50, 65, 82, 23]
sayi_listesi.sort(key=fonk)
print(sayi_listesi)