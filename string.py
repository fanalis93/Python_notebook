text = 'Hello, welcome to Software Testing Help. In this article: ”Loops in Python”, you’ll learn about loops with practical examples. Great right? Make sure to follow along as we learn together.Happy coding!'

for punc in '.,"\n?!':
    text = text.replace(punc,'')
text  = text.lower()
print(text)

wordsCount = {}
for j in range(len(text.split())):
    word = text.split()[j]
    if word not in wordsCount:
        wordsCount[word] = 1
    else:
        wordsCount[word] += 1
print(wordsCount)
wordsCount = {w:c for w,c in wordsCount.items()}
print(wordsCount)
wordsCount = {w: c for w, c in sorted(wordsCount.items(), key=lambda item: item[1], reverse=True)}
print(wordsCount)