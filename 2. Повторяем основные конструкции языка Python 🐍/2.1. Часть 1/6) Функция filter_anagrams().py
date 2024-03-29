def filter_anagrams(word, anagrams):
    return list(filter(lambda x: sorted(x) == sorted(word), anagrams))


word = 'abba'
anagrams = ['aabb', 'abcd', 'bbaa', 'dada']
print(filter_anagrams(word, anagrams))



