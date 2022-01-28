sentence = 'the quick brown fox jumped over the lazy dog'
words = sentence.split(' ')
print (words)
wordsReverse =[]
for word in words:
    wordsReverse.insert(0,word)
reverseSentence = ' '.join(wordsReverse)
print(reverseSentence)    