liste= ["Elma", "Armut", "Ayva"]
print(liste)

print(liste[1])
print(len(liste))

list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, 2, "asdas"]

print(list3)

print(liste[1:3])

if "Elma" in liste:
    print("listede elma da var")

liste[1] = "Kiraz"
print(liste)

liste.insert(0, "Ananas") #belirtilen indekse ekler
print(liste)

liste.append("Çilek") #sona ekler
print(liste)

liste.remove("Ananas")
print(liste)

liste.pop(3)
print(liste)

del liste[0]
print(liste)

liste.clear() #listeyi temizler
print(liste)