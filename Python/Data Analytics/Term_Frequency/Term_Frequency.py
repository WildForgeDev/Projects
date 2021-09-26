
#Christopher Lakey - Foundations of Big Data Analytics - CS356T - Unit 2 Individual Project
import pandas as pd
import csv
import math
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize 
nltk.download('stopwords')
set(stopwords.words('english'))

file = open("C:/Users/lakey/Downloads/28667_36536_bundle_archive/Tweets.csv", encoding="utf8")
reader = csv.reader(file)
writer = csv.writer(file)

def computeTF(wordDict, bow):
    tfDict = {}
    bowCount = len(data)
    for word, count in wordDict.items():
        tfDict[word] = count / float(bowCount)
    return tfDict

def computeIDF(docList):
    idfDict = {}
    N = len(data)
    
    idfDict = dict.fromkeys(docList[0].keys(),0)
    for doc in docList:
        for word, val in doc.items():
            if val > 0:
                idfDict[word] += 1
    for word, val in idfDict.items():
        idfDict[word] = math.log(N / float(val))
    
    return idfDict   

def computeTFIDF(tfBow, idfs):
    tfidf = {}
    for word, val in tfBow.items():
        tfidf[word] = val * idfs[word]
    return tfidf

data = [
    [(word.replace(",", "")
          .replace(".", "")
          .replace("(", "")
          .replace(")", "")
          .replace(' ', " ")
          .replace('  ', "")
          .replace('amp', "")
          .replace('americanair', "")
          .translate({ord(c): "" for c in "!@#$%^&*()[]{};:',./<>?\|`~-=_+``''"})
          .translate({ord(c): "" for c in "0123456789"})
          .encode('ascii','ignore').decode('ascii')
          .strip())
    for word in row[10].lower().split()]
    for row in reader]

#Removes header
data = data[1:]

stop_words = stopwords.words('english')
stop_words.append('get')
stop_words.append('im')
stop_words.append('us')
stop_words.append('cant')
stop_words.append('ive')
stop_words.append('u')
stop_words.append('cant')
stop_words.append('even')
stop_words.append('aa')
stop_words.append('see')
stop_words.append('could')
stop_words.append('thats')

dataFix = [" ".join(x) for x in data]

str1 = ''.join(dataFix)
str2 = ''.join(dataFix)

text_tokens = word_tokenize(str1)
text_tokens2 = word_tokenize(str2)

tokens_without_sw = [word for word in text_tokens if not word in stop_words]
tokens_without_sw2 = [word for word in text_tokens2 if not word in stop_words]

str1 = ' '.join(tokens_without_sw)
str2 = ' '.join(tokens_without_sw2)

wordset1 = str1.split(' ')
wordset2 = str2.split(' ')

wordset3 = set(wordset1).union(set(wordset2))

wordDict = dict.fromkeys(wordset3, 0)

for word in wordset1:
    wordDict[word]+=1

tfBow = computeTF(wordDict, wordset1)

idfs = computeIDF([wordDict, wordDict])

tfidfBow = computeTFIDF(tfBow, idfs)

pd.DataFrame([wordDict])

sort_order = sorted(tfidfBow.items(), key=lambda x: x[1], reverse=True)

a = sort_order

tweetData=pd.read_csv("C:/Users/lakey/Downloads/28667_36536_bundle_archive/Tweets.csv")

my_df = pd.DataFrame(a, columns = ['Word', 'tfidf Relevance Score'])
final_csv = pd.concat([tweetData, my_df ], axis=1)
final_csv.to_csv('Tweets.csv')


#print("\n===Words - IFIDF Frequencies===")
#for l in tfidfBow:
    #print(l,tfidfBow[l])
print("-----Program Complete-----")

NewData = tweetData=pd.read_csv("C:/Users/lakey/Desktop/Tweets.csv")

print(NewData)
