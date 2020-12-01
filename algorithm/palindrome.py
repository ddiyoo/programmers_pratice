word = "racecar"
word = 'stars'
word = list(word)

answer = True
for i in range(len(word)//2):
    if word[i] == word[-(i + 1)]:
        print(i)
        print(word[i], word[-(i + 1)])
    else: answer = False
        # answer = True
