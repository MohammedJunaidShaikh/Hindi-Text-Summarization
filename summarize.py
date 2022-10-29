import nltk
nltk.download('punkt')
from nltk import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
import math

tex = open('0.txt', encoding='utf8')
sen = tex.read()
# print(sen)

stop = open('stopwords.txt', encoding='utf8')
stopwords = []
for x in stop:
    stopwords.append(x)


def createfrequencytable(text_string) -> dict:
    stopWords = set(stopwords)
    words = word_tokenize(text_string)
    ps = PorterStemmer()

    freqTable = dict()
    for word in words:
        word = str(word)
        word = ps.stem(word)
        if word in stopWords:
            continue
        if word in freqTable:
            freqTable[word] += 1
        else:
            freqTable[word] = 1
    return freqTable


ft = createfrequencytable(sen)
# print(ft)

text = open('0.txt', encoding='utf8')
sentences = sent_tokenize(text.read())
total_documents = len(sentences)
# print(sentences)
# print('these are total_documents:', total_documents)


def scoresentences(sentences, freqTable) -> dict:
    sentenceValue = dict()
    for sentence in sentences:
        word_count_in_sentence = (len(word_tokenize(sentence)))
        for wordValue in freqTable:
            if wordValue in sentence.lower():
                if sentence[:10] in sentenceValue:
                    sentenceValue[sentence[:10]] += freqTable[wordValue]
                else:
                    sentenceValue[sentence[:10]] = freqTable[wordValue]
    sentenceValue[sentence[:10]] = sentenceValue[sentence[:10]] // word_count_in_sentence
    return sentenceValue


sentence_val = scoresentences(sentences, ft)
# print('this is sentence val:', sentence_val)


def findaverage_score(sentenceValue) -> int:
    sumValues = 0
    for entry in sentenceValue:
        sumValues += sentenceValue[entry]
    # Average value of a sentence from original text
    average = int(sumValues / len(sentenceValue))
    return average


thresh = findaverage_score(sentence_val)


def _generate_summary(sentences, sentenceValue, threshold):
    sentence_count = 0
    summary = ''
    for sentence in sentences:
        if sentence[:10] in sentenceValue and sentenceValue[sentence[:10]] > (threshold):
            summary += " " + sentence
            sentence_count += 1
    return summary


summary = _generate_summary(sentences, sentence_val, 1.5 * thresh)
# print('\n \n this is the summary', summary)


def summarize(inp_str):
    ft = createfrequencytable(inp_str)
    sentences = sent_tokenize(inp_str)
    sentence_val = scoresentences(sentences, ft)
    thresh = findaverage_score(sentence_val)
    summary = _generate_summary(sentences, sentence_val, 1.5 * thresh)
    print("Summary of the Passage:", summary)
    return summary
# summarize(sen)