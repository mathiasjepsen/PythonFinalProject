myDict = {
    "male": ["fuck", "her", "she", "gun", "car", "lol"],
    "female": ["him", "he", "skirt", "shop", "love"]
}
string = "gun car lol"

key_list = []
for key in myDict.keys():
    for value in myDict[key]:
        if value in string:
            key_list.append(key)
print(key_list)
if key_list.count("male") > key_list.count("female"):
    print("it contains more male shit")
else:
    print("contains more female shit")