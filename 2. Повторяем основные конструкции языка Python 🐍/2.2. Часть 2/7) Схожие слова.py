res = []
word = input()
result = []
for i in range(len(word)):
    if word[i] in 'ауоыиэяюёе':
        res.append(i)
n = int(input())
words = [input() for i in range(n)]
for el in words:
    tmp = []
    for letter in range(len(el)):
        if el[letter] in 'ауоыиэяюёе':
            tmp.append(letter)
    if res == tmp:
        result.append(el)
print(*result, sep='\n')