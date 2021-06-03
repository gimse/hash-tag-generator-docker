from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
import nltk

def generateHashtag(sentence):

    hash_tags = set()
    words = word_tokenize(sentence)
    word_tokens = [word for word in words if word.isalnum()]
    stop_words = set(stopwords.words('english'))
    filtered_sentence = []

    for word in word_tokens:
        if word not in stop_words:
            filtered_sentence.append(word)

    tagged_words = nltk.pos_tag(filtered_sentence)
    grammer = "NNP NNS NN VBG VB VBD VBN VBP NNPS JJ"

    for word in tagged_words:
        if (word[1] in grammer):
            hash_tags.add('#' + word[0])

    return hash_tags