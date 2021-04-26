import nltk
from nltk import word_tokenize
from nltk import bigrams, trigrams

unigrams = word_tokenize("The quick brown fox jumps over the lazy dog")
bigrams = bigrams(unigrams)
trigrams = trigrams(unigrams)
