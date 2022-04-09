# Implementation of a TF(IDF) algorithm
# Monday December 27th, 2021
# Modified Wednesday March 30th, 2022
#
import re
import sys
import nltk
from nltk.corpus import stopwords
from nltk.corpus import words


def load(path):
    # returns the whole text of file specified by path
    f = open(path, encoding='utf-8')
    text = f.read()
    f.close()
    return text


def tf(text, list_size=5):
    # tf - Token Frequency
    stopwords_ = [
        'i', 'the', 'a', 'an', 'and', 'or', 'in', 'on', 'is', 'are', 'was',
        'were', 'have', 'has', 'had', 'me', 'to', 'of', 'off', 'about', 'as',
        'with', 'it', 'my', 'your', 'his', 'her', 'our', 'their', 'some', 'any',
        'something', 'anything', 'nothing', 'myself', 'yourself', 'himself',
        'itself', 'themselves', 'herself', 'whenever', 'this', 'that', 'these',
        'those', 'get', 'got', 'gotten', 'find', 'ago', 'never', 'always',
        'before', 'after', 'who', 'no', 'be', 'all', 'into', 'not', 'by',
        'he', 'you', 'would', 'should', 'must', 'what', 'because', 'being',
        'we', 'one', 'out', 'so', 'its', 'us', 'them', 'do', 'put', 'how',
        'will', 'but', 'if', 'from', 'which', 'when', 'such', 'for', 'at',
        'good', 'am', 'they', 'than', 'man', 'men', 'cannot', 'own', 'both',
        'then', 'much', 'dr', 'based', 'there', 's', 'says', 'say', 'upon',
        'go', 'though', 'why', 'see', 'wa', 'way', 'can', 'take', 'type',
        'make', 'made', 'did', 'been', 'very', 'could', 'other', 'him',
        'many', 'more', 'might', 'now', 'come', 'came',
        'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight',
        'nine', 'ten',
        'little', 'find', 'found', 'great', 'time', 'thing', 'ha', 'again',
        'u', 't', 'd', 'm', 're', 'oh', 've', 'll', 'only', 'night', 'through',
        'place', 'went', 'well', 'day', 'up', 'down', 'said', 'she', 'over',
        'where', 'when', 'why', 'what', 'how', 'wa', 'sir',
        'mr', 'mrs', 'ms', 'like', 'just', 'know', 'knew', 'known',
        'first', 'second', 'third', 'fourth', 'fifth', 'sixth', 'seventh',
        'eighth', 'nineth', 'tenth',
        'about', 'above', 'across', 'after', 'against', 'along', 'among',
        'around', 'at', 'before', 'behind', 'between', 'beyond', 'but', 
        'by', 'concerning', 'despite', 'down', 'during', 'except', 'following',
        'for', 'from', 'in', 'including', 'into', 'like', 'near', 'of', 'off',
        'on', 'onto', 'out', 'over', 'past', 'plus', 'since', 'throughout',
        'to', 'towards', 'under', 'until', 'up', 'upon', 'up to', 'with', 'within',
        'without',
        '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10'

    ]

    # stopwords
    # sw = stopwords.words('english')
    # TODO: add regexp to exclude all numbers, stopwords + that
    # that should ensure better results than NLTK
    sw = stopwords_

    tokens = re.split(r'\W+', text.lower())

    # lemmatize
    wnl = nltk.WordNetLemmatizer()
    tokens = [wnl.lemmatize(t) for t in tokens]

    frequency = dict()
    for token in tokens:
        frequency[token] = frequency.get(token, 0) + 1

    if len(frequency) == 0:
        print('provide a non-empty text')
        return None

    frequency = sorted(frequency.items(), key=lambda kv: kv[1], reverse=True)

    results = list()
    count = 0
    i = 0

    while count <= list_size:
        tag = frequency[i][0]
        i += 1
        if not (tag in sw) and not tag.isdigit() and tag in words.words():
            results.append(tag)
            count += 1

    return results


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('usage: tf <path>')
    else:
        text = load(sys.argv[1])
        print(tf(text))
