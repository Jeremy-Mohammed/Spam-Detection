# CSCI 1030U Practice Final Exam - Programming Question #4

def getWordSize(word):
    if word == '':
        return 0

    return 1 + getWordSize(word[1:])

def processSentence(sentence, processWord):
    words = sentence.split(' ')
    result = []
    for word in words:
        result.append(processWord(word))
    return result

print(processSentence('the quick brown fox jumped over the lazy dog', getWordSize))
