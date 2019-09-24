textA = "We have developed speed, but we have shut ourselves in. Machinery that gives abundance has left us in want. Our knowledge has made us cynical. Our cleverness, hard and unkind. We think too much and feel too little. More than machinery we need humanity. More than cleverness we need kindness and gentleness. "


noCaps = textA.lower()
splitByWord = noCaps.split( )
wordList = [word.translate(None, ",.;@#?!&$") for word in splitByWord]
wordListUnique = list(set(wordList))

splitBySentence = textA.split(".")
noPunctuation = [sentence.translate(None, ",.;@#?!&$") for sentence in splitBySentence]
noWhiteSpace = [string.strip() for string in noPunctuation]
sentenceList = filter(None,noWhiteSpace)


numberWords = len(wordList)
numberSentences =len(sentenceList)

wordsPerSentence = []
for sentence in sentenceList:
  wordsValue = sentence.split( )
  wordsPerSentence.append(wordsValue)

sentenceLengths = map(len,wordsPerSentence)
sentenceLengths.sort(reverse=True)



def longest_sentences(arrayOfSentenceLengths):
  for i in range(len(arrayOfSentenceLengths)):
    x = arrayOfSentenceLengths[i]
    if x == max(arrayOfSentenceLengths):
       adjective = "longest"
    elif x == min(arrayOfSentenceLengths):
      adjective = "shortest"
    else:
      adjective = "next longest"
    print ("The {adjective} sentence has {xxx} words".format(adjective = adjective, xxx=x))


def longest_words(listOfWords, integer):
  listOfWords.sort 
  listOfWords.sort(key=len, reverse=True)
  print ("The {number} longest unique words in this list are {list}".format(number = integer, list = listOfWords[:integer]))


print ("There are {words} words in this piece of text".format(words=numberWords))
print ("There are {sentences} sentences in this piece of text".format(sentences=numberSentences))
longest_sentences(sentenceLengths)
longest_words(wordListUnique,5)
