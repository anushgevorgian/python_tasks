textfile = open("peterrabbit.txt", "r")
stringfile = textfile.read()

words_to_find = ["example", "all", "word", "up", "did", "him"]

for word in words_to_find:
    print(word, stringfile.count(word))
