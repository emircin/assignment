words = input("Write a word or sentences: ")
letters = list(words)
empty = []
for i in letters :
    
    x = keys.count(i)
    empty.append(x)
letters_count = dict(zip(letters, empty))

print(letters_count)
