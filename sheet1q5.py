text=input("enter string: ")
words =text.split()

print("word Frequency")
for i in words:
    print(i,":", words.count(i))

print("Character Frequency")
for ch in text :
    if ch!=" ":
        print(ch,":", text.count(ch))    