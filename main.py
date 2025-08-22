import pandas as pd
import json
import re


def data_prep(text):
    data = []
    for sentence in text:
        # removing numbers from sentence
        sentence = re.sub("[0-9]{1,}", "", sentence)
        sentence = sentence.replace(",", "")
        sentence = sentence.replace("(", "")
        sentence = sentence.replace(")", "")
        sentence = sentence.replace(".", "")
        sentence = sentence.replace("−", "")
        sentence = sentence.replace("!", "")
        sentence = sentence.replace("?", "")
        sentence = sentence.replace("\"", "")
        sentence = sentence.replace(":-:", "")
        sentence = sentence.replace(":", "")
        sentence = sentence.strip()
        data.append(sentence)
    return data


def calc_bigram():
    word_bigrams = {}
    for sentence in word_bigrams:
        tmp = sentence.split(" ")
        for i in range(1, len(tmp)):
            word = tmp[i]
            previous_word = tmp[i-1]
            if not (word in word_bigrams):
                word_bigrams[word] = []
            word_bigrams[word].append(previous_word)
    return word_bigrams


def Reading_dev_v1():
    df = pd.read_json("dev-v1.1.json")
    data = []
    for item in df['data']:
        for paragraph in item['paragraphs']:
            if (paragraph["context"] in data):
                continue
            data.append(paragraph['context'])
    return data


text = Reading_dev_v1()
cleaned_data = data_prep(text)
for i in range(len(cleaned_data)):
    print(cleaned_data[i], "\n")
