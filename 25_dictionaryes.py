sozluk = {
    "marka": "Ford",
    "model": "Mustang",
    "year" : 1964
}
print(sozluk)
print(sozluk["marka"])
print(sozluk["year"])

sozluk["renk"] = "siyah"
print(sozluk["renk"])

print(sozluk.keys())
print(sozluk.values())
print("----------------")
for  i in sozluk.keys():
    print(i, ":", sozluk[i])
